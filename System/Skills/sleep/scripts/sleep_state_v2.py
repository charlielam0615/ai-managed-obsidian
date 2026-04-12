#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import re
import uuid
from datetime import datetime
from pathlib import Path


STATE_VERSION = 2

CANONICAL_QUEUE_SOURCES = {
    "query-resolution",
    "inbox-triage",
    "document-ingestion",
    "ai-writing",
    "sleep",
    "user",
    "agent",
}

LEGACY_QUEUE_SOURCE_ALIASES = {
    "paper-ingestion": "document-ingestion",
}

QUEUE_SIGNAL_ACTIONS = {
    "resolved_queue_signal",
    "deferred_queue_signal",
    "superseded_queue_signal",
}

HEX_64_RE = re.compile(r"^[0-9a-f]{64}$")


def repo_root_from(file_path: str | Path) -> Path:
    return Path(file_path).resolve().parents[4]


def parse_root_arg(file_path: str | Path, description: str) -> Path:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--root",
        default=str(repo_root_from(file_path)),
        help="Repository root to operate on.",
    )
    args = parser.parse_args()
    return Path(args.root).resolve()


def sleep_state_dir(root: Path) -> Path:
    return root / "System" / "State" / "sleep"


def queue_root(state_dir: Path) -> Path:
    return state_dir / "queue"


def queue_pending_dir(state_dir: Path) -> Path:
    return queue_root(state_dir) / "pending"


def queue_deferred_dir(state_dir: Path) -> Path:
    return queue_root(state_dir) / "deferred"


def archive_resolved_dir(state_dir: Path) -> Path:
    return state_dir / "archive" / "resolved"


def history_root(state_dir: Path) -> Path:
    return state_dir / "history"


def runs_dir(state_dir: Path) -> Path:
    return state_dir / "runs"


def targets_dir(state_dir: Path) -> Path:
    return state_dir / "targets"


def clusters_dir(state_dir: Path) -> Path:
    return state_dir / "clusters"


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def json_files(directory: Path, recursive: bool = False) -> list[Path]:
    if not directory.exists():
        return []
    iterator = directory.rglob("*.json") if recursive else directory.glob("*.json")
    return sorted(path for path in iterator if path.is_file())


def directory_has_json(directory: Path) -> bool:
    return any(json_files(directory))


def ensure_gitkeep(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    gitkeep = directory / ".gitkeep"
    if not any(directory.iterdir()):
        gitkeep.write_text("", encoding="utf-8")
    elif gitkeep.exists() and any(path.name != ".gitkeep" for path in directory.iterdir()):
        gitkeep.unlink()


def normalize_source(source: str) -> str:
    return LEGACY_QUEUE_SOURCE_ALIASES.get(source, source)


def canonical_signal_material(payload: dict) -> dict:
    return {
        "note_path": payload["note_path"],
        "follow_up_kind": payload["follow_up_kind"],
        "context_note": payload.get("context_note") or "",
        "seed_query": payload.get("seed_query") or "",
    }


def compute_dedupe_key(payload: dict) -> str:
    canonical = canonical_signal_material(payload)
    serialized = json.dumps(canonical, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def is_uuid4(value: str) -> bool:
    try:
        parsed = uuid.UUID(value)
    except (ValueError, AttributeError, TypeError):
        return False
    return parsed.version == 4 and str(parsed) == value.lower()


def make_signal_id() -> str:
    return str(uuid.uuid4())


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def timestamp_filename_prefix(value: str) -> str:
    dt = parse_timestamp(value)
    return dt.strftime("%Y-%m-%dT%H-%M-%SZ")


def year_month(value: str) -> tuple[str, str]:
    dt = parse_timestamp(value)
    return dt.strftime("%Y"), dt.strftime("%m")


def slugify(text: str) -> str:
    lowered = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug


def short_slug(payload: dict, dedupe_key: str) -> str:
    note_stem = slugify(Path(payload["note_path"]).stem)
    follow_up = slugify(payload["follow_up_kind"])

    candidates = []
    if note_stem and follow_up and not note_stem.endswith(follow_up):
        candidates.append(f"{note_stem}-{follow_up}")
    if note_stem:
        candidates.append(note_stem)
    if follow_up:
        candidates.append(follow_up)
    candidates.append(f"signal-{dedupe_key[:8]}")

    for candidate in candidates:
        if candidate:
            return candidate[:64]
    return f"signal-{dedupe_key[:8]}"


def signal_filename(payload: dict, signal_id: str) -> str:
    prefix = timestamp_filename_prefix(payload["observed_at"])
    source_slug = slugify(payload["source"]) or "source"
    dedupe_key = payload["dedupe_key"]
    slug = short_slug(payload, dedupe_key)
    return f"{prefix}-{source_slug}-{slug}--{signal_id}.json"


def history_partition_path(state_dir: Path, timestamp: str, filename: str) -> Path:
    year, month = year_month(timestamp)
    return history_root(state_dir) / year / month / filename


def archive_partition_path(state_dir: Path, payload: dict, signal_id: str) -> Path:
    year, month = year_month(payload["observed_at"])
    return archive_resolved_dir(state_dir) / year / month / signal_filename(payload, signal_id)


def signal_dirs_v2(state_dir: Path) -> list[Path]:
    return [queue_pending_dir(state_dir), queue_deferred_dir(state_dir), archive_resolved_dir(state_dir)]


def is_v2_state(state_dir: Path) -> bool:
    if not queue_pending_dir(state_dir).exists() or not queue_deferred_dir(state_dir).exists():
        return False
    if not archive_resolved_dir(state_dir).exists():
        return False
    if directory_has_json(queue_root(state_dir)):
        return False
    if directory_has_json(history_root(state_dir)):
        return False

    for directory in signal_dirs_v2(state_dir):
        for path in json_files(directory, recursive=True):
            payload = load_json(path)
            if not isinstance(payload, dict):
                return False
            if payload.get("state_version") != STATE_VERSION:
                return False
    return True


def migrate_queue_payload(payload: dict) -> dict:
    migrated = dict(payload)
    migrated["state_version"] = STATE_VERSION
    migrated["source"] = normalize_source(migrated["source"])
    migrated["signal_id"] = make_signal_id()
    migrated["dedupe_key"] = compute_dedupe_key(migrated)
    return migrated


def has_hex64(value: str) -> bool:
    return bool(HEX_64_RE.fullmatch(value))

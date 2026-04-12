#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

from sleep_state_v2 import (
    CANONICAL_QUEUE_SOURCES,
    QUEUE_SIGNAL_ACTIONS,
    STATE_VERSION,
    archive_resolved_dir,
    clusters_dir,
    compute_dedupe_key,
    has_hex64,
    history_root,
    is_uuid4,
    json_files,
    load_json,
    parse_root_arg,
    queue_deferred_dir,
    queue_pending_dir,
    queue_root,
    relative,
    runs_dir,
    sleep_state_dir,
    targets_dir,
)


RUNTIME_DIRS = ("queue", "runs", "history", "targets", "clusters", "archive")
ALLOWED_HISTORY_ACTIONS = QUEUE_SIGNAL_ACTIONS | {"created_cluster_overview"}


def validate_runtime_examples(state_dir: Path, errors: list[str]) -> None:
    for dirname in RUNTIME_DIRS:
        for path in json_files(state_dir / dirname, recursive=True):
            if path.name.startswith("example-"):
                errors.append(f"{path}: example record must not live in active runtime directories")


def validate_layout(state_dir: Path, errors: list[str]) -> None:
    for required_dir in (queue_pending_dir(state_dir), queue_deferred_dir(state_dir), archive_resolved_dir(state_dir)):
        if not required_dir.exists():
            errors.append(f"{required_dir}: required directory missing")
    if json_files(queue_root(state_dir)):
        errors.append(f"{queue_root(state_dir)}: legacy flat queue files are not allowed in v2")
    if json_files(history_root(state_dir)):
        errors.append(f"{history_root(state_dir)}: legacy flat history files are not allowed in v2")


def validate_signal_file(
    path: Path,
    payload: dict,
    expected_locations: tuple[str, ...],
    root: Path,
    errors: list[str],
) -> tuple[str, str] | None:
    if payload.get("state_version") != STATE_VERSION:
        errors.append(f"{path}: queue/archive signal must declare state_version {STATE_VERSION}")
        return None
    required_fields = {
        "state_version",
        "signal_id",
        "dedupe_key",
        "note_path",
        "interaction_type",
        "observed_at",
        "source",
        "priority_hint",
        "follow_up_kind",
    }
    missing = required_fields - payload.keys()
    if missing:
        errors.append(f"{path}: missing required fields {sorted(missing)}")
        return None

    signal_id = payload["signal_id"]
    dedupe_key = payload["dedupe_key"]
    if not is_uuid4(signal_id):
        errors.append(f"{path}: signal_id must be a lowercase UUID4")
    if not has_hex64(dedupe_key):
        errors.append(f"{path}: dedupe_key must be a 64-character lowercase SHA-256 hex string")
    if payload["source"] not in CANONICAL_QUEUE_SOURCES:
        errors.append(f"{path}: unknown source '{payload['source']}'")
    computed_dedupe = compute_dedupe_key(payload)
    if dedupe_key != computed_dedupe:
        errors.append(f"{path}: dedupe_key does not match canonical signal fields")
    if f"--{signal_id}.json" not in path.name:
        errors.append(f"{path}: filename must include '--{signal_id}.json'")

    location = relative(path, root)
    if not any(expected in location for expected in expected_locations):
        errors.append(f"{path}: unexpected storage location '{location}'")
    return signal_id, dedupe_key


def collect_signals(state_dir: Path, root: Path, errors: list[str]):
    signals_by_id: dict[str, dict] = {}
    pending_dedupe: dict[str, Path] = {}

    for path in json_files(queue_pending_dir(state_dir)):
        payload = load_json(path)
        if not isinstance(payload, dict):
            errors.append(f"{path}: signal record must be a JSON object")
            continue
        result = validate_signal_file(path, payload, ("queue/pending",), root, errors)
        if result is None:
            continue
        signal_id, dedupe_key = result
        if signal_id in signals_by_id:
            errors.append(f"{path}: duplicate signal_id already seen in {signals_by_id[signal_id]['path']}")
        signals_by_id[signal_id] = {"path": relative(path, root), "storage": "pending", "payload": payload}
        if dedupe_key in pending_dedupe:
            errors.append(f"{path}: duplicate dedupe_key already present in {pending_dedupe[dedupe_key]}")
        else:
            pending_dedupe[dedupe_key] = path

    for path in json_files(queue_deferred_dir(state_dir)):
        payload = load_json(path)
        if not isinstance(payload, dict):
            errors.append(f"{path}: signal record must be a JSON object")
            continue
        result = validate_signal_file(path, payload, ("queue/deferred",), root, errors)
        if result is None:
            continue
        signal_id, _ = result
        if signal_id in signals_by_id:
            errors.append(f"{path}: duplicate signal_id already seen in {signals_by_id[signal_id]['path']}")
        signals_by_id[signal_id] = {"path": relative(path, root), "storage": "deferred", "payload": payload}

    for path in json_files(archive_resolved_dir(state_dir), recursive=True):
        payload = load_json(path)
        if not isinstance(payload, dict):
            errors.append(f"{path}: signal record must be a JSON object")
            continue
        result = validate_signal_file(path, payload, ("archive/resolved",), root, errors)
        if result is None:
            continue
        signal_id, _ = result
        if signal_id in signals_by_id:
            errors.append(f"{path}: duplicate signal_id already seen in {signals_by_id[signal_id]['path']}")
        signals_by_id[signal_id] = {"path": relative(path, root), "storage": "archive", "payload": payload}

    return signals_by_id


def validate_history(state_dir: Path, root: Path, signals_by_id: dict[str, dict], errors: list[str]) -> dict[str, dict]:
    receipts_by_signal: dict[str, dict] = {}
    for path in json_files(history_root(state_dir), recursive=True):
        payload = load_json(path)
        if not isinstance(payload, dict):
            errors.append(f"{path}: history record must be a JSON object")
            continue
        action = payload.get("action")
        if action not in ALLOWED_HISTORY_ACTIONS:
            errors.append(f"{path}: unsupported history action '{action}'")
            continue
        for field in ("timestamp", "run_id", "action", "resulting_artifact_path", "outcome"):
            if field not in payload:
                errors.append(f"{path}: missing required history field '{field}'")
        if "signal_path" in payload:
            errors.append(f"{path}: legacy signal_path is not allowed in v2 history")
        if action in QUEUE_SIGNAL_ACTIONS:
            signal_id = payload.get("signal_id")
            archive_path = payload.get("signal_archive_path")
            if not isinstance(signal_id, str) or not is_uuid4(signal_id):
                errors.append(f"{path}: queue history action must include UUID4 signal_id")
                continue
            if not isinstance(archive_path, str):
                errors.append(f"{path}: queue history action must include signal_archive_path")
                continue
            if signal_id not in signals_by_id:
                errors.append(f"{path}: signal_id does not reference a known signal: {signal_id}")
                continue
            signal_record = signals_by_id[signal_id]
            if signal_record["storage"] != "archive":
                errors.append(f"{path}: queue history action must reference an archived signal: {signal_id}")
            if archive_path != signal_record["path"]:
                errors.append(f"{path}: signal_archive_path does not match archived signal path for {signal_id}")
            receipts_by_signal[signal_id] = {"path": relative(path, root), "payload": payload}
    return receipts_by_signal


def validate_runs(state_dir: Path, signals_by_id: dict[str, dict], errors: list[str]) -> None:
    for path in json_files(runs_dir(state_dir)):
        payload = load_json(path)
        if not isinstance(payload, dict):
            errors.append(f"{path}: run record must be a JSON object")
            continue
        for key in ("run_id", "started_at", "selected_targets", "completed_targets", "deferred_targets"):
            if key not in payload:
                errors.append(f"{path}: missing required run field '{key}'")
        if "queue_signals_considered" in payload or "queue_signals_written" in payload:
            errors.append(f"{path}: legacy queue path fields are not allowed in v2 runs")
        for key in ("queue_signal_ids_considered", "queue_signal_ids_written"):
            if key in payload and not isinstance(payload[key], list):
                errors.append(f"{path}: {key} must be a list when present")
                continue
            for signal_id in payload.get(key, []):
                if signal_id not in signals_by_id:
                    errors.append(f"{path}: {key} references unknown signal_id {signal_id}")


def validate_targets(state_dir: Path, errors: list[str]) -> None:
    for path in json_files(targets_dir(state_dir)):
        payload = load_json(path)
        if not isinstance(payload, dict):
            errors.append(f"{path}: target record must be a JSON object")
            continue
        fingerprint = payload.get("source_fingerprint")
        if not isinstance(fingerprint, dict):
            errors.append(f"{path}: missing object source_fingerprint")
            continue
        if "note_content_sha256" not in fingerprint:
            errors.append(f"{path}: source_fingerprint must include note_content_sha256")


def validate_clusters(state_dir: Path, signals_by_id: dict[str, dict], errors: list[str]) -> None:
    for path in json_files(clusters_dir(state_dir)):
        payload = load_json(path)
        if not isinstance(payload, dict):
            errors.append(f"{path}: cluster record must be a JSON object")
            continue
        if "resolved_signal_paths" in payload:
            errors.append(f"{path}: legacy resolved_signal_paths is not allowed in v2 clusters")
        if "resolved_signal_ids" in payload:
            if not isinstance(payload["resolved_signal_ids"], list):
                errors.append(f"{path}: resolved_signal_ids must be a list")
            else:
                for signal_id in payload["resolved_signal_ids"]:
                    if signal_id not in signals_by_id:
                        errors.append(f"{path}: resolved_signal_ids references unknown signal_id {signal_id}")
                    elif signals_by_id[signal_id]["storage"] != "archive":
                        errors.append(f"{path}: resolved_signal_ids must reference archived signals only: {signal_id}")
        snapshot = payload.get("member_snapshot")
        if not isinstance(snapshot, list):
            errors.append(f"{path}: member_snapshot must be a list")
            continue
        for idx, member in enumerate(snapshot):
            if not isinstance(member, dict):
                errors.append(f"{path}: member_snapshot[{idx}] must be an object")
                continue
            if "note_content_sha256" not in member:
                errors.append(f"{path}: member_snapshot[{idx}] must include note_content_sha256")


def main(root: Path) -> int:
    state_dir = sleep_state_dir(root)
    errors: list[str] = []

    validate_runtime_examples(state_dir, errors)
    validate_layout(state_dir, errors)
    signals_by_id = collect_signals(state_dir, root, errors)
    receipts_by_signal = validate_history(state_dir, root, signals_by_id, errors)
    validate_runs(state_dir, signals_by_id, errors)
    validate_targets(state_dir, errors)
    validate_clusters(state_dir, signals_by_id, errors)

    pending_count = sum(1 for record in signals_by_id.values() if record["storage"] == "pending")
    deferred_count = sum(1 for record in signals_by_id.values() if record["storage"] == "deferred")
    archived_count = sum(1 for record in signals_by_id.values() if record["storage"] == "archive")

    if errors:
        print("sleep-state validation failed", file=sys.stderr)
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1

    print("sleep-state validation passed")
    print(f"Pending queue signals: {pending_count}")
    print(f"Deferred queue signals: {deferred_count}")
    print(f"Archived queue signals: {archived_count}")
    print(f"Resolved queue receipts: {len(receipts_by_signal)}")
    return 0


if __name__ == "__main__":
    import sys

    root = parse_root_arg(__file__, "Validate sleep state V2 layout and records.")
    raise SystemExit(main(root))

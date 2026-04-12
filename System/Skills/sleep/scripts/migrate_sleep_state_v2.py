#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

from sleep_state_v2 import (
    STATE_VERSION,
    archive_partition_path,
    archive_resolved_dir,
    clusters_dir,
    dump_json,
    ensure_gitkeep,
    history_partition_path,
    history_root,
    is_v2_state,
    json_files,
    load_json,
    migrate_queue_payload,
    parse_root_arg,
    queue_deferred_dir,
    queue_pending_dir,
    queue_root,
    relative,
    runs_dir,
    sleep_state_dir,
)


def migrate(root: Path) -> int:
    state_dir = sleep_state_dir(root)

    if is_v2_state(state_dir):
        print("Already at sleep state v2")
        return 0

    legacy_queue_files = json_files(queue_root(state_dir))
    legacy_history_files = json_files(history_root(state_dir))
    run_files = json_files(runs_dir(state_dir))
    cluster_files = json_files(clusters_dir(state_dir))

    history_payloads = {path: load_json(path) for path in legacy_history_files}
    resolved_paths = {
        payload["signal_path"]
        for payload in history_payloads.values()
        if isinstance(payload, dict)
        and payload.get("action") == "resolved_queue_signal"
        and isinstance(payload.get("signal_path"), str)
    }

    queue_mapping: dict[str, dict] = {}

    for legacy_path in legacy_queue_files:
        legacy_rel = relative(legacy_path, root)
        payload = load_json(legacy_path)
        migrated = migrate_queue_payload(payload)
        if legacy_rel in resolved_paths:
            destination = archive_partition_path(state_dir, migrated, migrated["signal_id"])
            status = "archived"
        else:
            destination = queue_pending_dir(state_dir) / destination_name(migrated)
            status = "pending"
        queue_mapping[legacy_rel] = {
            "signal_id": migrated["signal_id"],
            "status": status,
            "destination": destination,
            "payload": migrated,
        }

    for entry in queue_mapping.values():
        dump_json(entry["destination"], entry["payload"])

    for legacy_path, payload in history_payloads.items():
        migrated = dict(payload)
        if migrated.get("action") == "resolved_queue_signal":
            signal_path = migrated.pop("signal_path", None)
            if signal_path in queue_mapping:
                mapping = queue_mapping[signal_path]
                migrated["signal_id"] = mapping["signal_id"]
                migrated["signal_archive_path"] = relative(mapping["destination"], root)
        destination = history_partition_path(state_dir, migrated["timestamp"], legacy_path.name)
        dump_json(destination, migrated)

    for run_path in run_files:
        payload = load_json(run_path)
        migrated = dict(payload)
        if "queue_signals_considered" in migrated:
            migrated["queue_signal_ids_considered"] = [
                queue_mapping[path]["signal_id"]
                for path in migrated.pop("queue_signals_considered")
            ]
        if "queue_signals_written" in migrated:
            migrated["queue_signal_ids_written"] = [
                queue_mapping[path]["signal_id"]
                for path in migrated.pop("queue_signals_written")
            ]
        dump_json(run_path, migrated)

    for cluster_path in cluster_files:
        payload = load_json(cluster_path)
        migrated = dict(payload)
        if "resolved_signal_paths" in migrated:
            migrated["resolved_signal_ids"] = [
                queue_mapping[path]["signal_id"]
                for path in migrated.pop("resolved_signal_paths")
            ]
        dump_json(cluster_path, migrated)

    for legacy_path in legacy_queue_files + legacy_history_files:
        if legacy_path.exists():
            legacy_path.unlink()

    ensure_gitkeep(queue_pending_dir(state_dir))
    ensure_gitkeep(queue_deferred_dir(state_dir))
    archive_resolved_dir(state_dir).mkdir(parents=True, exist_ok=True)
    history_root(state_dir).mkdir(parents=True, exist_ok=True)

    archived = sum(1 for entry in queue_mapping.values() if entry["status"] == "archived")
    pending = sum(1 for entry in queue_mapping.values() if entry["status"] == "pending")
    print(f"Migrated sleep state to v{STATE_VERSION}: {archived} archived, {pending} pending")
    return 0


def destination_name(payload: dict) -> str:
    from sleep_state_v2 import signal_filename

    return signal_filename(payload, payload["signal_id"])


if __name__ == "__main__":
    root = parse_root_arg(__file__, "Migrate sleep state to V2 queue layout.")
    raise SystemExit(migrate(root))

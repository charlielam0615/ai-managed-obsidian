import json
import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
MIGRATE_SCRIPT = REPO_ROOT / "System/Skills/sleep/scripts/migrate_sleep_state_v2.py"
VALIDATE_SCRIPT = REPO_ROOT / "System/Skills/sleep/scripts/validate_sleep_state.py"


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dedupe_key_for(payload: dict) -> str:
    canonical = {
        "note_path": payload["note_path"],
        "follow_up_kind": payload["follow_up_kind"],
        "context_note": payload.get("context_note") or "",
        "seed_query": payload.get("seed_query") or "",
    }
    serialized = json.dumps(canonical, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


class SleepStateV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.state_dir = self.root / "System/State/sleep"
        for rel in ("queue", "history", "runs", "targets", "clusters"):
            (self.state_dir / rel).mkdir(parents=True, exist_ok=True)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def run_script(self, script: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), "--root", str(self.root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def seed_legacy_state(self) -> None:
        write_json(
            self.state_dir / "queue/2026-04-07T07-25-34Z-inbox-triage-ai-futures-overview.json",
            {
                "note_path": "Notes/A.md",
                "interaction_type": "create",
                "observed_at": "2026-04-07T07:25:34Z",
                "source": "inbox-triage",
                "priority_hint": "medium",
                "follow_up_kind": "overview",
                "reason": "resolved",
            },
        )
        write_json(
            self.state_dir / "queue/2026-04-12T07-48-15Z-sleep-mamba-3-revisit.json",
            {
                "note_path": "Notes/B.md",
                "interaction_type": "deep_read",
                "observed_at": "2026-04-12T07:48:15Z",
                "source": "sleep",
                "priority_hint": "low",
                "follow_up_kind": "revisit",
                "reason": "still pending",
            },
        )
        write_json(
            self.state_dir / "history/2026-04-07T09-30-43Z-resolved-ai-futures-overview.json",
            {
                "timestamp": "2026-04-07T09:30:43Z",
                "run_id": "sleep-run-2026-04-07T09-27-00Z",
                "target_id": "cluster-a",
                "action": "resolved_queue_signal",
                "signal_path": "System/State/sleep/queue/2026-04-07T07-25-34Z-inbox-triage-ai-futures-overview.json",
                "resulting_artifact_path": "Notes/Overview.md",
                "outcome": "resolved",
            },
        )
        write_json(
            self.state_dir / "runs/sleep-run-2026-04-12T07-46-58Z.json",
            {
                "run_id": "sleep-run-2026-04-12T07-46-58Z",
                "started_at": "2026-04-12T07:46:58Z",
                "completed_at": "2026-04-12T07:48:15Z",
                "scope_hint": "fixture",
                "selected_targets": ["Notes/A.md", "Notes/B.md"],
                "queue_signals_considered": [
                    "System/State/sleep/queue/2026-04-07T07-25-34Z-inbox-triage-ai-futures-overview.json"
                ],
                "queue_signals_written": [
                    "System/State/sleep/queue/2026-04-12T07-48-15Z-sleep-mamba-3-revisit.json"
                ],
                "completed_targets": ["Notes/A.md"],
                "deferred_targets": ["Notes/B.md"],
                "checkpoint_note": "fixture",
            },
        )
        write_json(
            self.state_dir / "clusters/fixture-cluster.json",
            {
                "cluster_id": "fixture-cluster",
                "seed_note": "Notes/A.md",
                "cluster_fingerprint": "cluster-hash",
                "member_note_paths": ["Notes/A.md"],
                "member_snapshot": [{"note_path": "Notes/A.md", "note_content_sha256": "note-a-sha"}],
                "overview_note_path": "Notes/Overview.md",
                "last_digested_at": "2026-04-07T09:30:43Z",
                "freshness_status": "fresh",
                "resolved_signal_paths": [
                    "System/State/sleep/queue/2026-04-07T07-25-34Z-inbox-triage-ai-futures-overview.json"
                ],
                "last_run_id": "sleep-run-2026-04-07T09-27-00Z",
            },
        )
        write_json(
            self.state_dir / "targets/a.json",
            {
                "target_id": "Notes/A.md",
                "target_type": "note",
                "note_path": "Notes/A.md",
                "source_fingerprint": {
                    "fingerprint_schema": "content_sha256",
                    "note_content_sha256": "note-a-sha",
                },
                "last_digested_at": "2026-04-07T09:30:43Z",
                "last_digest_artifact_path": "Notes/Overview.md",
                "freshness_status": "fresh",
                "last_run_id": "sleep-run-2026-04-07T09-27-00Z",
            },
        )

    def test_migration_converts_legacy_state_and_validator_passes(self) -> None:
        self.seed_legacy_state()

        result = self.run_script(MIGRATE_SCRIPT)
        self.assertEqual(result.returncode, 0, msg=result.stderr)

        pending_files = sorted((self.state_dir / "queue/pending").glob("*.json"))
        deferred_files = sorted((self.state_dir / "queue/deferred").glob("*.json"))
        archive_files = sorted((self.state_dir / "archive/resolved/2026/04").glob("*.json"))
        history_files = sorted((self.state_dir / "history/2026/04").glob("*.json"))

        self.assertEqual(len(pending_files), 1)
        self.assertEqual(len(deferred_files), 0)
        self.assertEqual(len(archive_files), 1)
        self.assertEqual(len(history_files), 1)
        self.assertFalse(any((self.state_dir / "queue").glob("2026-*.json")))

        pending_payload = read_json(pending_files[0])
        archive_payload = read_json(archive_files[0])
        history_payload = read_json(history_files[0])
        run_payload = read_json(self.state_dir / "runs/sleep-run-2026-04-12T07-46-58Z.json")
        cluster_payload = read_json(self.state_dir / "clusters/fixture-cluster.json")

        self.assertEqual(pending_payload["state_version"], 2)
        self.assertEqual(archive_payload["state_version"], 2)
        self.assertIn("signal_id", pending_payload)
        self.assertIn("dedupe_key", pending_payload)
        self.assertIn("--", pending_files[0].name)
        self.assertIn("--", archive_files[0].name)

        self.assertEqual(history_payload["signal_id"], archive_payload["signal_id"])
        self.assertEqual(history_payload["signal_archive_path"], archive_files[0].relative_to(self.root).as_posix())
        self.assertNotIn("signal_path", history_payload)

        self.assertIn("queue_signal_ids_considered", run_payload)
        self.assertNotIn("queue_signals_considered", run_payload)
        self.assertNotIn("queue_signals_written", run_payload)
        self.assertEqual(run_payload["queue_signal_ids_considered"], [archive_payload["signal_id"]])
        self.assertEqual(run_payload["queue_signal_ids_written"], [pending_payload["signal_id"]])

        self.assertEqual(cluster_payload["resolved_signal_ids"], [archive_payload["signal_id"]])
        self.assertNotIn("resolved_signal_paths", cluster_payload)

        validate = self.run_script(VALIDATE_SCRIPT)
        self.assertEqual(validate.returncode, 0, msg=validate.stderr)

    def test_validator_rejects_duplicate_pending_dedupe_key(self) -> None:
        pending_dir = self.state_dir / "queue/pending"
        pending_dir.mkdir(parents=True, exist_ok=True)
        (self.state_dir / "queue/deferred").mkdir(parents=True, exist_ok=True)
        (self.state_dir / "archive/resolved").mkdir(parents=True, exist_ok=True)
        payload_base = {
            "state_version": 2,
            "note_path": "Notes/A.md",
            "interaction_type": "create",
            "observed_at": "2026-04-12T07:48:15Z",
            "source": "sleep",
            "priority_hint": "medium",
            "follow_up_kind": "linking",
            "context_note": "",
            "seed_query": "",
            "reason": "fixture",
        }
        shared_dedupe_key = dedupe_key_for(payload_base)
        write_json(
            pending_dir / "2026-04-12T07-48-15Z-sleep-a--11111111-1111-4111-8111-111111111111.json",
            {
                **payload_base,
                "signal_id": "11111111-1111-4111-8111-111111111111",
                "dedupe_key": shared_dedupe_key,
            },
        )
        write_json(
            pending_dir / "2026-04-12T07-48-16Z-sleep-b--22222222-2222-4222-8222-222222222222.json",
            {
                **payload_base,
                "signal_id": "22222222-2222-4222-8222-222222222222",
                "dedupe_key": shared_dedupe_key,
            },
        )

        validate = self.run_script(VALIDATE_SCRIPT)
        self.assertNotEqual(validate.returncode, 0)
        self.assertIn("dedupe", validate.stderr.lower())

    def test_validator_allows_distinct_pending_dedupe_key(self) -> None:
        pending_dir = self.state_dir / "queue/pending"
        pending_dir.mkdir(parents=True, exist_ok=True)
        (self.state_dir / "queue/deferred").mkdir(parents=True, exist_ok=True)
        (self.state_dir / "archive/resolved").mkdir(parents=True, exist_ok=True)
        payload_a = {
            "state_version": 2,
            "note_path": "Notes/A.md",
            "interaction_type": "create",
            "observed_at": "2026-04-12T07:48:15Z",
            "source": "sleep",
            "priority_hint": "medium",
            "follow_up_kind": "linking",
        }
        payload_b = {
            "state_version": 2,
            "note_path": "Notes/A.md",
            "interaction_type": "create",
            "observed_at": "2026-04-12T07:48:16Z",
            "source": "sleep",
            "priority_hint": "medium",
            "follow_up_kind": "overview",
        }
        write_json(
            pending_dir / "2026-04-12T07-48-15Z-sleep-a--11111111-1111-4111-8111-111111111111.json",
            {
                **payload_a,
                "signal_id": "11111111-1111-4111-8111-111111111111",
                "dedupe_key": dedupe_key_for(payload_a),
            },
        )
        write_json(
            pending_dir / "2026-04-12T07-48-16Z-sleep-b--22222222-2222-4222-8222-222222222222.json",
            {
                **payload_b,
                "signal_id": "22222222-2222-4222-8222-222222222222",
                "dedupe_key": dedupe_key_for(payload_b),
            },
        )

        validate = self.run_script(VALIDATE_SCRIPT)
        self.assertEqual(validate.returncode, 0, msg=validate.stderr)

    def test_migration_is_idempotent(self) -> None:
        self.seed_legacy_state()

        first = self.run_script(MIGRATE_SCRIPT)
        self.assertEqual(first.returncode, 0, msg=first.stderr)
        snapshot = sorted(
            (
                path.relative_to(self.root).as_posix(),
                path.read_text(encoding="utf-8"),
            )
            for path in self.state_dir.rglob("*.json")
        )

        second = self.run_script(MIGRATE_SCRIPT)
        self.assertEqual(second.returncode, 0, msg=second.stderr)
        self.assertIn("already at sleep state v2", second.stdout.lower())

        snapshot_after = sorted(
            (
                path.relative_to(self.root).as_posix(),
                path.read_text(encoding="utf-8"),
            )
            for path in self.state_dir.rglob("*.json")
        )
        self.assertEqual(snapshot, snapshot_after)


if __name__ == "__main__":
    unittest.main()

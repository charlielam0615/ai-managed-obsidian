# Sleep Signal Examples

These are reference examples for queue signals written under `System/State/sleep/queue/pending/` or `System/State/sleep/queue/deferred/`.

They are examples only. They are not the queue itself.

## Example Filename Pattern

```text
2026-04-07T12-34-56Z-query-resolution-knowledge-systems--11111111-1111-4111-8111-111111111111.json
```

## Example: Query-Resolution Follow-Up

```json
{
  "state_version": 2,
  "signal_id": "11111111-1111-4111-8111-111111111111",
  "dedupe_key": "7ab66901dbf1f27ad7f5da2f6f21cd4d35fb768f1ee2c6de644fceeb6f5d4b7d",
  "note_path": "Notes/Knowledge Systems.md",
  "interaction_type": "query",
  "observed_at": "2026-04-07T12:34:56Z",
  "source": "query-resolution",
  "priority_hint": "medium",
  "follow_up_kind": "linking",
  "seed_query": "What do I already know about knowledge systems?",
  "reason": "Query surfaced a likely missing link between the knowledge systems note and note-graph structure notes."
}
```

## Example: Inbox Promotion Follow-Up

```json
{
  "state_version": 2,
  "signal_id": "22222222-2222-4222-8222-222222222222",
  "dedupe_key": "c2b3f7b3a8b8c69b373fb3f6788d7fbb962872a81f266ed625c3dfd99ec3b069",
  "note_path": "Notes/Agent Collaboration Patterns.md",
  "interaction_type": "create",
  "observed_at": "2026-04-07T13:10:12Z",
  "source": "inbox-triage",
  "priority_hint": "medium",
  "follow_up_kind": "overview",
  "reason": "The note was processed and promoted from Inbox, but it likely belongs in a broader workflow overview that does not exist yet."
}
```

## Example: Document-Ingestion Follow-Up

```json
{
  "state_version": 2,
  "signal_id": "33333333-3333-4333-8333-333333333333",
  "dedupe_key": "596c7eb005feccb6edafce6106546f0cb9ff4c824f04f93ba0cba7b0e223cc02",
  "note_path": "Notes/Sparse Autoencoders For Feature Discovery.md",
  "interaction_type": "create",
  "observed_at": "2026-04-07T14:02:30Z",
  "source": "document-ingestion",
  "priority_hint": "high",
  "follow_up_kind": "linking",
  "reason": "The source note is in place but still needs links to related interpretability notes and possible inclusion in a topic overview."
}
```

## Example: Sleep Deferral / Future Work

```json
{
  "state_version": 2,
  "signal_id": "44444444-4444-4444-8444-444444444444",
  "dedupe_key": "1a816a4ccbba327b8868d1d03fbb6ff7b0e441457e65d2d2cbf8adf75bdbf620",
  "note_path": "Notes/Knowledge Systems.md",
  "interaction_type": "deep_read",
  "observed_at": "2026-04-07T15:45:05Z",
  "source": "sleep",
  "priority_hint": "low",
  "follow_up_kind": "metadata",
  "context_note": "Notes/Index.md",
  "reason": "Current sleep pass added high-confidence links, but metadata normalization was intentionally deferred to keep the run bounded."
}
```

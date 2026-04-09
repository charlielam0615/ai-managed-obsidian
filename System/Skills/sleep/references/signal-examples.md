# Sleep Signal Examples

These are reference examples for queue signals written under `System/State/sleep/queue/`.

They are examples only. They are not the queue itself.

## Example Filename Pattern

```text
2026-04-07T12-34-56Z-query-resolution-knowledge-systems.json
```

## Example: Query-Resolution Follow-Up

```json
{
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
  "note_path": "Notes/Agent Collaboration Patterns.md",
  "interaction_type": "create",
  "observed_at": "2026-04-07T13:10:12Z",
  "source": "inbox-triage",
  "priority_hint": "medium",
  "follow_up_kind": "overview",
  "reason": "The note was processed and promoted from Inbox, but it likely belongs in a broader workflow overview that does not exist yet."
}
```

## Example: Paper-Ingestion Follow-Up

```json
{
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

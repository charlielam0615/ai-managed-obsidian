# Sleep Signal Writing Protocol

This reference defines how workflows should record future sleep work into `System/State/sleep/queue/`.

The goal is to make future integration work explicit, append-only, and reviewable without turning state into the semantic layer.

See `signal-examples.md` for concrete example records.

## Canonical Location

Write future sleep signals under:

```text
System/State/sleep/queue/
```

Use one JSON file per signal.

Do not maintain a shared mutable queue file in the first version.

## Purpose

A sleep signal records future integration work created by a note-affecting interaction when that work is not being completed immediately.

Signals help later `sleep` passes decide what to revisit.

Signals are operational memory only. They do not replace note-layer knowledge, links, metadata, or summaries.

## When To Write A Signal

Write a signal when:

- a query or deep read surfaces missing links, thin metadata, or needed overview/index follow-up
- a note is promoted from `Inbox/` into `Notes/` but likely needs later linking or broader integration work
- a paper note is created or updated and likely needs later linking, overview integration, or sleep digestion
- a `sleep` pass discovers follow-up work that it intentionally does not complete in the current bounded run

## When Not To Write A Signal

Do not write a signal when:

- the follow-up is trivial
- the relevant integration work was already completed in the current workflow
- the follow-up is speculative or too low-confidence to act on later
- an obviously equivalent pending signal already represents the same work clearly

Prefer one clear actionable signal over repeated noise.

## Record Shape

Each signal file should contain one JSON object with:

- `note_path`
- `interaction_type`
- `observed_at`
- `source`
- `priority_hint`
- `follow_up_kind`

Optional fields:

- `context_note`
- `seed_query`
- `reason`

## Field Guidance

- `note_path`: absolute or vault-relative note path, whichever is used consistently by the current state model
- `interaction_type`: what happened, such as `create`, `edit`, `move`, `metadata_change`, `deep_read`, `query`, or `reorg`
- `observed_at`: timestamp of the interaction in ISO-like form
- `source`: where the interaction came from, such as `user`, `agent`, `query-resolution`, `inbox-triage`, `paper-ingestion`, or `sleep`
- `priority_hint`: lightweight urgency or importance label, such as `low`, `medium`, or `high`
- `follow_up_kind`: the kind of future work, such as `linking`, `metadata`, `index`, `overview`, or `revisit`
- `context_note`: optional anchor note that gives useful surrounding context
- `seed_query`: optional query text that surfaced the follow-up
- `reason`: optional short explanation of why the signal exists

## Filename Convention

Use timestamp-first filenames with a short readable suffix:

```text
YYYY-MM-DDTHH-MM-SSZ-<source>-<short-slug>.json
```

Example:

```text
2026-04-07T12-34-56Z-query-resolution-knowledge-systems.json
```

The filename is an operational identifier only. Meaning belongs inside the JSON body.

## Resolution And Lifecycle

Signals may later be:

- resolved by a `sleep` pass
- deferred into a later run
- superseded by a clearer or more complete signal

Use run records or history entries to note that outcome. Do not overload the queue entry itself with semantic meaning.

## Producer Set For The First Version

The first workflows that should explicitly produce signals are:

- `query-resolution`
- `inbox-triage`
- `paper-ingestion`
- `sleep`

Other note-touching workflows may adopt the same protocol later.

# Sleep State Model

This reference defines the intended role of `System/State/sleep/`.

`sleep` uses state to stay bounded, incremental, and re-runnable. The state layer is operational memory only. It should help later runs decide what to process, what changed, what interactions created future work, and what was deferred. It should not become a second knowledge graph or a shadow note system.

## Design Goals

The state model should support:

- per-target tracking
- cluster tracking
- change detection and staleness
- interaction-driven future-work signaling
- run checkpoints
- audit history

It should stay lean enough that deleting or rebuilding the state would be inconvenient but not catastrophic.

## What Belongs In State

State may contain:

- stable target identifiers
- source paths or note paths
- observed hashes, mtimes, or equivalent change markers
- last-digested timestamps
- digest freshness status
- cluster membership snapshots
- last-run outcomes
- deferral reasons
- queue or priority hints
- interaction signals from note-affecting activity
- audit entries describing what a pass touched

State should describe workflow facts, not vault meaning.

## What Must Not Go In State

Do not store in state:

- the canonical summary of a note
- the canonical digest of a paper
- the only copy of a cluster synthesis
- relationship explanations that should live in notes
- hidden semantic conclusions needed to understand the vault

If a future human or agent should be able to learn something by reading the vault, that knowledge belongs in `Notes/`, not `System/State/sleep/`.

## Conceptual Structure

Suggested structure:

```text
System/State/sleep/
  targets/
  clusters/
  queue/
  runs/
  history/
```

You do not need this exact directory structure if a later implementation finds a cleaner equivalent, but the model should preserve these responsibilities.

Read `signal-writing.md` for the canonical queue write protocol and `signal-examples.md` for concrete example records.

See `System/State/sleep/runs/example-run.json` and `System/State/sleep/history/example-history.json` for concrete examples of how later sleep runs record signal resolution operationally.

## Targets

Purpose:

- track per-target digestion state
- support skip and refresh decisions
- remember what kind of target an object is

Each target record should be able to answer:

- what object does this record refer to
- what kind of target is it
- when was it last digested
- what source version was digested
- does it currently look stale
- was it deferred, and why

Possible fields:

- target id
- target type
- note path or source path
- source fingerprint
- last digested at
- last digest artifact path
- freshness status
- defer reason
- last run id

Targets may also carry lightweight integration status such as whether linking, metadata improvement, or navigation follow-up is still pending.

## Clusters

Purpose:

- track bounded multi-note regions
- detect when cluster-level synthesis may be stale
- avoid rebuilding the same cluster view every run

Each cluster record should be able to answer:

- what seed or rationale created this cluster
- which notes were considered members last time
- what overview artifact represents the cluster
- whether member changes likely made the cluster stale

Possible fields:

- cluster id
- seed note or seed query
- member note paths
- cluster fingerprint derived from members
- overview note path
- last digested at
- freshness status

## Queue

Purpose:

- hold the current or next bounded worklist
- preserve prioritization decisions across interrupted passes
- capture future integration work created by note-affecting interactions

This can be lightweight. It does not need to be a job scheduler.

Queue entries should be written as one JSON file per signal under `System/State/sleep/queue/`.

Useful contents:

- target id
- priority label or score
- selection reason
- queued at
- optional user scope tag
- note path
- interaction type
- observed at
- source such as `user`, `agent`, `query`, `edit`, or `move`
- follow-up kind such as `linking`, `metadata`, `index`, `overview`, or `revisit`
- optional context note or seed query
- optional reason

## Runs

Purpose:

- checkpoint manual `sleep` passes
- preserve resumability for bounded work

Each run record should be able to answer:

- when the pass started
- what scope it intended to cover
- what targets were selected
- what finished
- what was deferred
- whether the pass completed cleanly

Useful fields:

- run id
- started at
- completed at
- scope hint
- selected targets
- completed targets
- deferred targets
- checkpoint note

## Interaction Signals

Purpose:

- record note-affecting activity that should influence later sleep passes
- preserve future integration work even when the current interaction does not perform it immediately

Examples of note-affecting interactions:

- create
- edit
- move
- metadata change
- deep read
- broad query over notes
- reorganization work

Useful fields:

- note path
- interaction type
- observed at
- source
- priority hint
- follow-up kind
- optional context note
- optional seed query
- optional reason

## History

Purpose:

- provide a minimal audit trail
- support review and debugging of repeated `sleep` passes

History should be append-only or easy to inspect.

Useful entries:

- timestamp
- run id
- target id or cluster id
- action taken
- resulting artifact path
- short outcome label

## Change Detection

`sleep` needs a cheap way to tell whether reprocessing is justified.

Practical approaches include:

- file modification times
- content hashes
- lightweight fingerprints derived from relevant source notes
- cluster fingerprints derived from member fingerprints

Do not use a brittle scheme that requires perfect metadata. The goal is to detect meaningful change well enough to avoid obvious redundant work.

## Deferrals

Deferrals should be explicit and lightweight.

Track:

- target id
- defer reason
- deferred at
- optional retry hint

A deferral is an operational fact, not a semantic conclusion.

## Resolution

Signals may be resolved, deferred, or superseded by later runs.

Record that outcome in run records or history entries rather than turning queue files into mutable state logs.

## Rebuildability

The state layer should be rebuildable from the vault at some cost.

That means:

- state can accelerate work, but must not be the only place where meaning lives
- losing state should not destroy the vault's actual understanding
- rebuilding state should recover operational posture, not invent missing semantic artifacts

---
name: sleep
description: Use this skill when a human explicitly requests a bounded maintenance pass over existing vault contents to improve future comprehension by creating or refreshing digests, synthesis notes, links, and integration scaffolding without broad reorganization.
---

# Sleep

## When To Use

Use this skill only when a human explicitly invokes `sleep` or clearly requests a manual consolidation pass over existing vault contents.

This skill is manual-only. Do not trigger it on a timer, on startup, on idle, on file changes, or on agent initiative alone.

## Purpose

`sleep` is the vault's unified consolidation workflow.

Its job is to reduce future reading cost by creating and strengthening semantic scaffolding inside the vault itself. It does this by digesting bounded targets, improving legibility, surfacing relationships, adding high-confidence links, and building progressive-disclosure layers that later humans and agents can read directly.

`sleep` exists because the vault is the source of truth. Future understanding should come from better notes, better digests, and better synthesis in `Notes/`, not from hidden runtime memory.

## Inputs

- an explicit manual invocation
- an optional scope, seed, or priority hint from the user
- the current contents of `Notes/`, relevant papers, and any already-existing digest notes
- operational state from `System/State/sleep/` when available

## Output

One bounded consolidation pass that leaves behind durable, reviewable artifacts in the knowledge layer, such as:

- improved local digests inside notes or paper notes
- refreshed paper-note summaries
- cluster overview notes
- selective high-confidence Obsidian-compatible linking
- new entry points into dense note regions
- refreshed metadata and navigation surfaces

Operational memory about the pass belongs in `System/State/sleep/`. Knowledge and relationships belong in `Notes/`.

## Unified Target Model

A sleep target is any bounded comprehension surface whose digestion would make the vault easier to understand later.

Target shapes include:

- a single note
- a single paper note
- a connected cluster of notes
- a note neighborhood around a seed
- a stale digest that needs refresh

These are all the same kind of work at different scales: read the source material, identify the minimum integration work that would reduce future comprehension cost, write that scaffolding into the knowledge layer, and record operational state for re-runs.

## Progressive Disclosure Model

`sleep` should improve legibility in layers rather than trying to replace raw material.

Preferred layers:

- content index or overview note that helps a reader enter the region
- raw note or raw paper
- local digest that makes one object easier to parse
- cluster digest or overview note that explains how multiple objects fit together

This helps future humans and agents enter a dense region at the highest useful level first, then drill down only as needed.

Use the artifact patterns in `references/artifact-patterns.md` when you need a concrete shape for local or cluster digests.

## Selection And Prioritization

After manual invocation, do not sweep the vault uniformly. Choose high-leverage targets first.

Strong selection signals include:

- no digest exists
- an existing digest is stale
- a note changed materially since its last digestion
- a note or paper has many backlinks or is clearly central
- a dense local cluster has no synthesis note
- an important paper has a weak or missing paper note
- the user explicitly named, pinned, or recently worked in a region

Prefer a small number of high-value targets over many shallow touches.

## Single-Object vs Cluster Digestion

Digest locally when:

- one note or paper is the main bottleneck
- the surrounding region is weakly connected
- a local digest would solve most of the comprehension problem

Digest as a cluster when:

- multiple notes are strongly connected
- the value lies in the relationships, not just one note
- a dense neighborhood lacks an overview
- several local digests exist but no synthesis layer ties them together

Start with the smallest scope that can produce a meaningful integration improvement. Escalate from one note to a cluster only when local digestion would leave the main comprehension gap unresolved.

## Procedure

1. Confirm that `sleep` was explicitly requested and set a bounded scope.
2. Read the current `sleep` state if it exists to avoid blind reprocessing.
3. Read `Notes/Index.md` when it exists and the pass would benefit from the current top-level map of the note layer.
4. Select one or a few high-leverage targets, considering queued future-work signals alongside freshness, centrality, and user scope.
5. Decide whether each target should be handled locally or as a cluster.
6. Read the relevant notes and paper notes first. Read raw PDFs only when the note layer is insufficient.
7. Create or refresh the smallest integration artifact that would make the target materially easier to understand later.
8. Add or improve high-confidence Obsidian-compatible links when they materially strengthen the note graph.
9. Update `Notes/Index.md` only if the pass created or materially improved a processed entry point into the knowledge layer.
10. Update metadata, hubs, or overview notes when they materially improve integration quality.
11. Update `System/State/sleep/` so a later run can tell what changed, what was deferred, what should be revisited next, and which note-affecting interactions created future work.
12. If the pass discovers additional future work that it intentionally does not complete now, write one or more queue signals using `references/signal-writing.md`.

Use the `obsidian-cli` skill for note-aware retrieval or path-sensitive note operations when practical, but `sleep` is not primarily a CLI skill.

## Conservative Write Policy

`sleep` may:

- improve legibility
- add summaries or digests
- add selective high-confidence links
- create overview notes where useful
- refresh the content index when navigation materially improved
- refresh stale digest layers when the underlying material changed
- strengthen metadata and navigation surfaces
- prune or promote bootstrap entries in `Notes/Index.md`

`sleep` must not:

- aggressively rewrite existing thought
- mass-refactor the vault
- force questionable classifications
- perform broad rename or move operations as part of normal consolidation
- turn `System/State/` into a shadow knowledge base

If a meaningful path change seems needed, hand that decision to `path-change-policy` instead of folding it into normal `sleep`.

## Deferral Rules

Skip or defer a target when:

- there is too little information to produce a trustworthy digest
- the input is too noisy or fragmented
- confidence is too low
- a likely duplicate is unresolved
- the right cluster boundary is too unclear
- a new digest would create more confusion than value

When deferring, record the reason in `System/State/sleep/` as operational state, not as hidden semantic content.

## Re-Runnability

Repeated runs should be incremental.

`sleep` should:

- skip unchanged targets
- refresh stale digests when justified
- revisit clusters when member notes changed materially
- avoid rewording stable digests without a real need
- consume queued future-work signals from note-affecting interactions
- promote bootstrap entries into better navigation surfaces when justified
- remove bootstrap entries once stronger navigation exists

The goal is progressive improvement, not churn.

## Cold-Start Behavior

`sleep` must remain useful from day one.

When the vault is immature:

- work with weak metadata
- prefer obvious local digests over ambitious synthesis
- create small overview notes only where a region is already clearly dense
- tolerate partially normalized paper notes
- rely on content, links, and local evidence rather than advanced retrieval systems

Cold-start `sleep` should still leave behind clearer entry points than it found.

## State Use

`sleep` depends on `System/State/sleep/` for bounded operational memory.

State is used to:

- track which targets were already processed
- detect when notes or clusters changed enough to justify re-digestion
- remember deferrals and why they happened
- checkpoint runs and support incremental re-entry
- audit what each pass touched
- record future integration work signaled by note-affecting interactions

State must not contain the actual summaries, synthesis, or relationships that belong in `Notes/`.

Read `references/state-model.md` and `references/signal-writing.md` before implementing or modifying the state layer.

## Relationship To Other Skills

- `inbox-triage`: moves new material into clearer destinations; `sleep` works on existing material after intake.
- `paper-ingestion`: normalizes PDFs and paper notes; `sleep` improves the semantic integration and connected understanding around them later.
- `query-resolution`: answers questions from the current vault; queries and deep reads may also create future sleep signals that help later integration work.
- `path-change-policy`: governs whether path churn is justified; `sleep` should normally avoid path churn and delegate that decision when needed.

## Verification

Before ending a `sleep` pass:

- confirm the pass stayed within scope
- confirm each touched target gained a meaningful comprehension or integration aid
- confirm new artifacts live in the knowledge layer, not hidden state
- confirm unchanged or low-confidence targets were skipped or deferred rather than forced
- confirm the state layer was updated only with operational memory

## Supporting Files

- `references/state-model.md`
- `references/signal-writing.md`
- `references/artifact-patterns.md`

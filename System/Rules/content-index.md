# Content Index

## Purpose

The content index is the vault's curated navigation surface.

Its job is to help humans and agents find the most important entry points in the knowledge layer quickly, without scanning the whole vault or introducing a hidden registry.

## Canonical Location

The primary content index lives at `Notes/Index.md`.

At small scale, prefer a single index note. Only introduce a dedicated `Notes/Indexes/` area if the single-note index becomes noisy enough that a split clearly improves navigation.

`Notes/Index.md` may contain both:

- curated long-term entry sections
- one temporary bootstrap section for newly processed notes that do not yet have a better navigation surface

## What The Index Is

The index is:

- a processed note in the knowledge layer
- a selective list of high-value entry points
- a starting surface for broad queries and exploration
- a progressive-disclosure aid for future humans and agents

The index is not:

- a complete catalog of every note
- a substitute for links, local metadata, or note content
- an operational log
- a hidden database or control plane

The bootstrap section is the only narrow exception to the curated-only posture, and it exists to solve cold-start navigation without turning the whole index into a permanent catalog.

## What Belongs In The Index

Include only notes or pages that materially improve navigation, such as:

- overview notes
- topic hubs
- key source notes
- synthesis notes
- processed question notes that function as entry points
- other stable entry points that help a future reader decide where to go next

Each entry should stay lightweight:

- one link
- one short reason the entry matters

Index descriptions should remain in English by default, even when the linked note is not in English.

## Section Semantics

When `Notes/Index.md` uses the current top-level sections, interpret them narrowly:

- `Core Topics`: durable cluster entrypoints
- `Synthesis And Overviews`: bridge notes, comparisons, subcluster overviews, and other non-top-level synthesis
- `Key Paper Notes`: paper notes that are individually valuable entry points even when they are not cluster anchors

A `Core Topics` note should be:

- the best top-level entry surface into a stable note region
- clearly bounded enough to remain useful over time
- linked outward to multiple nearby notes, sources, or subregions
- more valuable in top-level navigation than leaving it only in generic overview space

Do not promote a note into `Core Topics` merely because it is recent, interesting, or overview-shaped.

Bridge notes, comparison notes, and narrow subcluster overviews should normally remain in `Synthesis And Overviews`.

## Core Topic Promotion Test

Before placing a note in `Core Topics`, confirm all of the following:

1. The note is the main entry surface for a stable cluster rather than one supporting note among many.
2. The cluster boundary is coherent and likely to remain useful.
3. The note links out to multiple related notes, sources, or subregions.
4. Promoting it improves top-level navigation more than leaving it in `Synthesis And Overviews`.
5. The note is not primarily a bridge, comparison, or narrow subcluster note.

If any of these are false, do not promote the note into `Core Topics` yet.

## Bootstrap Section

`Notes/Index.md` may contain one temporary bootstrap section for newly processed notes.

Use it when:

- a note has just left `Inbox/`
- no relevant topic hub, overview, or other navigation surface exists yet
- the note still needs top-level discoverability until better navigation is built

Bootstrap behavior:

- include all newly processed notes that lack a better navigation surface
- keep the section count-limited rather than exhaustive
- treat the section as explicitly prunable during `sleep`
- do not treat inclusion there as proof that the note is a long-term entry point

For the first version, cap the bootstrap section to a small recent set of at most 15 notes.

If adding a newly processed note would exceed the cap:

- remove the oldest bootstrap entry that still lacks a better navigation surface
- do not block promotion out of `Inbox/`
- do not allow silent indefinite overflow
- if the removed entry still needs future integration work, rely on an existing sleep-state signal or write one

Removing an entry from the bootstrap section is an operational pruning step, not a claim that the note is unimportant.

## What Does Not Belong

Do not use the index for:

- raw intake material in `Inbox/`
- routine one-off notes that are not useful entry points
- exhaustive listings of every note in a folder
- operational history that belongs in `System/State/`
- speculative categories created only to make the vault look organized

## Read Protocol

Agents should read `Notes/Index.md` early when the task is broad, exploratory, or requires understanding the shape of the note layer.

Typical cases:

- broad vault questions
- exploratory search
- synthesis work
- bounded maintenance passes such as `sleep`

The index is a starting point, not a complete map. Agents should still expand through note links, backlinks, related summaries, and direct search when needed.

## Update Protocol

Agents should update the index only when navigation materially changes.

Good reasons to update it include:

- a new overview or synthesis note becomes a real entry point
- a new bridge note becomes the clearest entry point into a dense region
- a source note becomes central enough to revisit repeatedly
- a processed query result is filed back into `Notes/`
- a `sleep` pass creates a better top-level entry into a dense note region
- a newly promoted note still lacks any better navigation surface, in which case the bootstrap section should be updated during promotion
- an existing bootstrap entry now has a stronger overview, hub, or local navigation surface and should be replaced or removed
- an existing index description or section placement became stale because the note's role changed materially

Do not update the index for every routine note edit or every new note.

Important non-English notes may still appear when they are real entry points. Prefer English descriptions that help agents and humans retrieve them from the shared English navigation surface.

When no better navigation surface exists yet, newly processed notes may temporarily enter the bootstrap section even if they are not yet true long-term entry points.

## Workflow Decision Requirement

For `inbox-triage` and `sleep`, reconciling touched notes against the index is a required workflow step, not optional cleanup.

Each such run must end with one explicit outcome:

- `updated Notes/Index.md`
- `used existing navigation surface: <path>`
- `deferred with sleep signal: <signal_id>`

When `updated Notes/Index.md` is the outcome, the workflow must also choose the correct section intentionally rather than appending mechanically. In particular:

- durable cluster entrypoints belong in `Core Topics`
- bridge notes, comparisons, and non-top-level overviews belong in `Synthesis And Overviews`
- paper notes that are valuable standalone entry points belong in `Key Paper Notes`

If an agent claims an existing navigation surface instead of updating the index:

- the surface must already link to the relevant note, or be updated in the same run
- the path should be reported explicitly in completion evidence

If neither an index update nor a safe existing-surface update can be completed in the same bounded run:

- write a sleep signal instead of silently treating navigation as complete
- report the signal id explicitly

## Maintenance Rules

Keep the index:

- short enough to read in one pass
- organized by function rather than deep taxonomy
- stable in wording unless an entry's role actually changed
- selective enough that every entry earns its place

Prefer replacing weak or stale entries over endlessly appending.

`sleep` should prune or promote bootstrap entries over time:

- promote them into curated sections when they become real entry points
- remove them once a better topic hub, overview, or local navigation surface exists
- keep the bootstrap section within the fixed count cap

## Scaling Rule

If the index grows beyond a comfortable single-page navigation note, split it conservatively into a small number of functional index notes such as:

- `Notes/Indexes/Topics.md`
- `Notes/Indexes/Papers.md`
- `Notes/Indexes/Questions.md`

Do not treat this as permission to broadly subdivide `Notes/` itself. Prefer navigation notes before folder reorganization.

## Verification

After updating the index:

- confirm each listed entry still exists
- confirm each description still matches the linked page
- confirm the result is still readable in one pass
- confirm the update improved navigation rather than merely adding more text

After a workflow decides not to update the index:

- confirm the cited existing navigation surface exists and still serves as a real entry path
- confirm any deferral has a concrete sleep signal id rather than a vague future intention

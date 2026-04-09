---
name: ai-writing
description: Use this skill when a user wants the agent to help outline, draft, revise, or polish an article, essay, post, newsletter, tutorial, or other substantial piece of writing while keeping the output inside the vault's note-processing and navigation model.
---

# AI Writing

## When To Use

Use this skill when a user wants the agent to:

- outline an article or essay
- draft a post, newsletter, or tutorial
- refine a rough draft
- improve structure, flow, hook, or clarity
- add citations or research support
- turn notes into a more polished written piece

## Purpose

This skill adapts long-form AI-assisted writing to the vault's existing contract.

The goal is not just to generate text. The goal is to create or improve writing in a way that:

- preserves the user's voice and intent
- keeps note-like outputs inside the vault
- respects the `Inbox/` vs `Notes/` processing model
- leaves writing artifacts retrievable and reviewable later

## Placement Model

By default, agent-authored writing should be created directly in its destination folder.

For most writing projects, that means:

- polished or actively worked article drafts belong in `Notes/`
- `Inbox/` should be used only when the user explicitly wants to simulate human capture or rough intake

Do not default to `Inbox/` for agent-written drafts.

If the output is written into `Notes/`, it should satisfy the minimum processed-note metadata contract:

- `lang`
- a short English `summary`

If the note is primarily non-English, also include:

- English `aliases`
- English `search_terms`

## Inputs

- the topic or writing goal
- the user's intended audience
- the desired format, tone, and length when known
- any existing notes, outline fragments, or sources
- any requested citation style or evidence expectations

## Output

One or more of:

- an outline
- a draft article note in `Notes/`
- a revised or polished writing note in `Notes/`
- research-backed supporting material integrated into the writing note
- a queue signal for later sleep integration when follow-up linking, metadata, or overview work remains

## Default Workflow

1. Understand the writing project:
   - topic
   - target audience
   - purpose
   - desired tone
   - expected length or format
   - available sources or existing notes
2. If useful, propose or refine an outline first.
3. Draft or revise the piece section by section.
4. Preserve the user's voice rather than replacing it with generic prose.
5. Add citations or references only when requested or when evidence is needed for substantive claims.
6. Write the resulting note directly into `Notes/` unless the user explicitly asks for inbox-style capture.
7. Add the minimum processed-note metadata.
8. Integrate the note into the appropriate navigation surface using the normal fallback order:
   - existing topic hub or overview note
   - existing curated index section
   - bootstrap section in `Notes/Index.md`
9. If later integration work remains, record one or more queue signals using `System/Skills/sleep/references/signal-writing.md`.

## Writing Principles

- suggest, do not override, the user's voice
- prefer clarity over generic flourish
- keep structure explicit
- improve hooks and transitions when useful
- support claims with sources when appropriate
- avoid pretending unsupported claims are sourced

## Research And Citations

When the user wants research-backed writing:

- gather relevant supporting material conservatively
- prefer credible sources
- distinguish sourced facts from inference
- keep citations in the format the user requests when possible

If reliable sourcing is not available, say so clearly instead of fabricating references.

## Section Feedback

If the user is writing interactively, review sections for:

- clarity
- flow
- evidence gaps
- tone consistency
- transition quality
- whether the section still sounds like the user

## When To Use Inbox Instead

Use `Inbox/` only when the user explicitly wants:

- a rough captured draft for later digestion
- human-capture simulation
- a deliberately incomplete intake artifact

If the user says "write me an article" or "draft this essay," default to `Notes/`, not `Inbox/`.

## Verification

Before finishing:

- confirm the output matches the user's requested form and tone
- confirm the note lives in the correct destination
- confirm the minimum metadata is present if the output is in `Notes/`
- confirm the note is incorporated into the appropriate navigation surface
- confirm any unfinished integration work is represented by queue signals when needed

## Related Skills

- `query-resolution`
- `inbox-triage`
- `obsidian-cli`
- `sleep`

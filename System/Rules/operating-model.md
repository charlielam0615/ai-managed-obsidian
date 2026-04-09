# Operating Model

## Purpose

This vault is a plain-file personal knowledge management system designed to work well with both humans and AI agents.

It is intended to be:

- AI-native from the start
- harness-agnostic across agent and runtime environments
- safe to maintain and reorganize incrementally
- Git-compatible and easy to review
- simple at first glance, with more structure revealed only when needed

## Source Of Truth

The vault's files are the source of truth.

- Markdown notes are the canonical knowledge layer.
- PDFs stored in the library are canonical source objects.
- Folder names, filenames, links, and local metadata should carry meaning directly.
- Do not introduce hidden control planes, required databases, or external registries as the primary source of truth.

## Human And Agent Responsibilities

Humans:

- capture new material into `Inbox/`
- create and edit notes directly when desired
- review, accept, or revert changes through normal file and Git workflows

Agents:

- process material from `Inbox/`
- create processed notes and semantic scaffolding in destination folders
- improve structure incrementally instead of imposing large taxonomies
- preserve link integrity and change history

## Progressive Disclosure

Keep the visible structure simple by default.

- Prefer a small number of stable folders.
- Let semantic structure emerge inside notes, metadata, and links.
- Prefer curated index and overview notes before expanding folder hierarchy.
- Add more explicit organization only when there is enough real content to justify it.

## Incremental Organization

Organization should happen gradually and non-destructively.

- Prefer small, reviewable improvements over sweeping rewrites.
- Avoid forcing early classification when the right structure is not yet clear.
- Defer uncertain organization decisions rather than creating brittle folder systems.

## Where Semantic Structure Should Live

Semantic structure should primarily live in notes, local metadata, and links rather than deep folder trees.

- Notes are the main interface for interpretation and synthesis.
- Curated index notes in `Notes/` may provide top-level navigation into the knowledge layer.
- Links should express relationships between ideas, sources, and source notes.
- Folders provide coarse placement, not the full ontology of the vault.

Notes in `Notes/` remain open to future refinement. The distinction between `Inbox/` and `Notes/` is processing status, not permanence.

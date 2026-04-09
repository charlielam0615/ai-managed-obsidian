# Project Memory

See @README for the repository overview.

For broad orientation in the note layer, start with @Notes/Index.md.

## Core Contract

- The vault's files are the source of truth.
- `Inbox/` is the single human intake point. Do not use it as generic agent staging.
- Processed notes that are ready for integration belong in `Notes/`.
- Canonical source documents belong in `Library/Documents/`.
- Prefer links, local metadata, index notes, and overview notes before adding folder taxonomy.
- Prefer Obsidian-aware operations when note identity or paths matter.
- Keep edits bounded, reviewable, and reversible.

Read these early when structure or navigation is part of the task:

- `System/Rules/operating-model.md`
- `System/Rules/content-index.md`
- `System/Rules/language-and-cross-language-retrieval.md`
- `System/Rules/note-processing-lifecycle.md`
- `System/Rules/processed-note-metadata.md`
- `System/Rules/notes-topic-folders.md`
- `System/Rules/safe-change-policy.md`
- `System/Rules/obsidian-cli-first.md`

## Workflow Routing

Do not improvise a fresh workflow when an existing skill already matches the task.

- Broad vault questions: read `Notes/Index.md` first, then use `System/Skills/query-resolution/SKILL.md`.
- Inbox processing: use `System/Skills/inbox-triage/SKILL.md`.
- Document or PDF ingestion: use `System/Skills/document-ingestion/SKILL.md`.
- AI-authored article or draft writing: use `System/Skills/ai-writing/SKILL.md`.
- Path-sensitive note operations: use `System/Skills/obsidian-cli/SKILL.md` and `System/Skills/path-change-policy/SKILL.md`.
- Bounded maintenance or consolidation: use `System/Skills/sleep/SKILL.md`.

## Content Index

`Notes/Index.md` is the curated entry point into the note layer.

- Read it early for broad, exploratory, or synthesis-oriented work.
- Treat it as a navigation surface, not as proof that nothing else exists.
- Update it only when navigation materially improves.
- For multilingual retrieval, translate broad queries into English and rely on English metadata on non-English processed notes.

## Completion Evidence

For workflow-shaped tasks, include brief evidence in the final response:

- Broad questions: whether `Notes/Index.md` was consulted, whether retrieval was translated into English when relevant, the main note anchors, and whether raw source documents were needed.
- Ingestion tasks: final destinations, duplicate outcome when relevant, whether metadata and navigation integration were completed, and whether the index changed.
- Maintenance passes: scope, links or integration work added or refreshed, whether the index changed, and what future sleep signals were recorded operationally.
- Path-sensitive edits: whether Obsidian-aware operations were used, or why a direct edit was safe.

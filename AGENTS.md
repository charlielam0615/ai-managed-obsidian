# Agent Instructions

This repository is an AI-native Obsidian vault. The vault's files are the source of truth.

Start with:

- [README.md](README.md) for repository overview
- [Notes/Index.md](Notes/Index.md) for broad note-layer orientation
- [System/Rules/operating-model.md](System/Rules/operating-model.md) for the core contract

## Priority Rules

Agents working in this repository must follow the rules under `System/Rules/`.

The most important constraints are:

- `Inbox/` is the single human intake point. Do not use it as a generic agent staging area.
- Processed notes that are ready for integration belong in `Notes/`.
- Canonical paper PDFs belong in `Library/Papers/`.
- System guidance belongs in `System/`.
- Prefer note and link structure over deep folder expansion.
- Prefer curated index and overview notes before expanding folder hierarchy.
- Prefer Obsidian-aware operations when note identity or paths matter.
- Keep changes bounded, reviewable, and reversible.

## Task Routing

Do not improvise a fresh workflow when an existing skill already matches the task.

- Broad vault questions: read `Notes/Index.md` first, then follow `System/Skills/query-resolution/SKILL.md`.
- Inbox processing: follow `System/Skills/inbox-triage/SKILL.md`.
- Paper or PDF ingestion: follow `System/Skills/paper-ingestion/SKILL.md`.
- AI-authored article or draft writing: follow `System/Skills/ai-writing/SKILL.md`.
- Path-sensitive note operations: follow `System/Skills/obsidian-cli/SKILL.md` and `System/Skills/path-change-policy/SKILL.md` when rename or move decisions are involved.
- Bounded maintenance or consolidation: follow `System/Skills/sleep/SKILL.md`.

If a task affects vault structure or navigation, also read:

- `System/Rules/content-index.md`
- `System/Rules/language-and-cross-language-retrieval.md`
- `System/Rules/note-processing-lifecycle.md`
- `System/Rules/processed-note-metadata.md`
- `System/Rules/notes-topic-folders.md`
- `System/Rules/safe-change-policy.md`
- `System/Rules/obsidian-cli-first.md`

## Content Index Protocol

`Notes/Index.md` is the curated entry point into the note layer.

Agents should:

- read it early for broad, exploratory, or synthesis-oriented work
- treat it as a navigation surface, not as proof that nothing else exists
- update it only when navigation materially improves

For multilingual work, agents should keep the shared retrieval surface in English and rely on English metadata on non-English processed notes.

Do not:

- turn it into a complete catalog
- use it as an operational log
- append every new note or paper to it automatically

## Completion Evidence

When a task matches one of the workflows above, the final report should include enough evidence to show the workflow was followed.

- Broad vault questions: say whether `Notes/Index.md` was consulted, whether the query was translated into English for retrieval, which notes were the main anchors, and whether raw PDFs were needed.
- Inbox or paper ingestion: report the final note or PDF destination, duplicate-check outcome when relevant, whether required metadata and navigation integration were completed, and whether the index changed.
- Sleep or maintenance passes: report the scope, links or integration work added or refreshed, whether the index changed, and what future sleep signals were recorded operationally.
- Path-sensitive note edits: say whether Obsidian-aware operations were used and, if not, why a direct edit was safe.

## Change Posture

- Make the smallest change that meaningfully improves the vault.
- Do not force material into a speculative taxonomy.
- Defer when placement, naming, or path changes are too uncertain.
- Keep related edits together and avoid mixing unrelated cleanup with content work.

## If Unsure

If a rule and a convenience conflict, follow the rule.

If a task is broad, start from the index and the matching skill instead of scanning the vault blindly.

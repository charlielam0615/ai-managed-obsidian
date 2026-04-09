# Language And Cross-Language Retrieval

## Purpose

This vault may contain notes in multiple human languages.

The goal of multilingual support here is reliable retrieval, not forced translation or a heavyweight multilingual note-management system.

## English Retrieval Space

Agents should operate in the English retrieval space.

That means:

- system-facing rules and workflow guidance stay in English
- broad note retrieval should be grounded through English search terms and summaries
- when a user asks in a non-English language, the agent should translate the query into English before broad vault search

Agents may still answer in the user's language after retrieval.

## Note Language

Notes may remain in their natural primary language.

- Do not translate note bodies just to normalize the vault.
- Do not treat multilingual support as a requirement to rewrite notes into English.
- Use the smallest retrieval bridge that makes the note discoverable from English-space search.

## Required English Metadata For Non-English Processed Notes

When a non-English note becomes a processed note in `Notes/`, it should include the baseline metadata from `System/Rules/processed-note-metadata.md` plus the extra English discovery metadata below.

Additional required fields:

- `aliases`: English alternate names or phrasings that improve recall
- `search_terms`: English retrieval vocabulary for the note's concepts

This metadata exists for cross-language retrieval. It is not a requirement to duplicate the note's full contents in English.

## English Notes

English notes do not need extra multilingual metadata by default.

Additional aliases or search terms are allowed when helpful, but they are not required just to satisfy symmetry.

## Query Translation Rule

If the incoming query is not in English, the agent should:

1. translate the query into English
2. search the vault in English retrieval space
3. expand through notes, links, source notes, and sources as usual
4. answer in the user's language when appropriate

Failure to match the original query language is not sufficient evidence that the vault lacks the answer.

## Retrieval Order

For multilingual retrieval, prefer this order:

1. `Notes/Index.md` for broad orientation
2. note titles
3. English aliases
4. English `search_terms`
5. English summaries
6. linked notes, backlinks, and source notes
7. raw source documents only when the note layer is insufficient

## Index Guidance

`Notes/Index.md` remains the shared top-level navigation note.

- Keep index descriptions in English by default.
- Important non-English notes may still appear in the index when they are real entry points.
- Do not create parallel per-language index trees by default.

## Redundancy And Personal Scale

This is a personal knowledge vault.

- Some redundant or partially overlapping notes are acceptable.
- Do not overengineer sibling-note management or path disambiguation in the first multilingual version.
- Prefer better English metadata over more structure.

## Intake And Promotion

Rough or not-yet-processed material in `Inbox/` does not need full multilingual metadata.

Apply the English retrieval bridge when:

- a note is promoted into `Notes/`
- a processed non-English note is materially updated
- a note becomes important enough to be a real retrieval target

## Verification

When a non-English processed note is created or normalized:

- confirm `lang` is present
- confirm the required English `summary` is present
- confirm English aliases improve recall
- confirm English `search_terms` describe the note's concepts

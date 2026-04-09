---
name: query-resolution
description: Use this skill when answering questions over the vault by starting from note-layer retrieval, expanding through related notes and source notes, and consulting raw documents only when the note layer is insufficient.
---

# Query Resolution

## When To Use

Use this skill when a user asks a question that should be answered from the contents of the vault rather than from general world knowledge.

## Inputs

- the user question
- English retrieval metadata on non-English processed notes when available
- `Notes/Index.md` when it exists
- access to vault search and note reading
- access to related source notes and, when necessary, canonical source documents

## Output

A grounded answer that:

- is supported by notes or sources actually present in the vault
- distinguishes direct support from inference
- states clearly when the vault is incomplete or ambiguous

## Procedure

1. If the user asks in a non-English language, translate the retrieval query into English before broad search.
2. Read `Notes/Index.md` first when it exists and the query is broad enough to benefit from a top-level map.
3. Search for directly relevant notes, source notes, and summaries in English retrieval space.
4. Read the strongest initial hits.
5. Expand into English aliases, English `search_terms`, English summaries, linked notes, backlinks, and associated source notes when useful.
6. Consult raw source documents only when the note layer is insufficient or the question requires source verification.
7. Answer from the strongest available evidence in the vault.

Use the `obsidian-cli` skill when you need concrete CLI targeting, retrieval, or fallback behavior.

## Preferred Evidence Order

Prefer this order when available:

- integrated summary notes
- source notes in `Notes/`
- closely linked knowledge notes
- raw source files such as documents

Raw source documents are a fallback source, not the default starting point.

## Expansion Rules

Expand conservatively:

- use the index as a navigation surface, not as proof that nothing else exists
- do not stop after failing to match the original query language; continue through English retrieval metadata
- read explicit links mentioned in the anchor note
- use outgoing links and backlinks when they materially improve retrieval
- inspect nearby summary or synthesis notes
- stop when additional notes stop adding evidence

Do not scan the whole vault if a bounded subset is enough.

## When Not To Escalate To Source Documents

Stay in the note layer when:

- an integrated summary already answers the question
- a source note captures the needed claim accurately
- additional source reading would add little value

Escalate to a source document only for missing details, source verification, or quote-level checks.

## Verification

Before finalizing:

- confirm the cited note or source actually supports the answer
- confirm the answer matches the current vault contents
- confirm cross-language misses were handled through English retrieval metadata when relevant
- if the query or deep read surfaced likely future integration work, record one or more queue signals using `System/Skills/sleep/references/signal-writing.md`
- avoid mixing unsupported outside knowledge into a vault-grounded response

## Related Skills

- `obsidian-cli`
- `document-ingestion`

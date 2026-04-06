---
name: obsidian-cli
description: Use this skill when interacting with the vault through Obsidian-aware CLI operations such as search, read, create, append, move, rename, links, backlinks, unresolved-link checks, or property updates, especially when note identity or path semantics matter.
---

# Obsidian CLI

## When To Use

Use this skill when an agent needs reliable Obsidian-aware CLI behavior instead of raw filesystem operations.

## Inputs

- the intended vault operation
- the current shell environment
- access to either `obsidian` on `PATH` or the app-bundled binary

## Output

One of:

- a validated Obsidian CLI plan for the task
- a successful Obsidian-aware operation
- a conservative fallback decision when the runtime environment is not cooperating

## Known Local Reality

In this environment:

- `obsidian` should resolve on `PATH`
- the app-bundled binary is `/Applications/Obsidian.app/Contents/MacOS/obsidian`
- local help has confirmed support for `search`, `search:context`, `read`, `create`, `append`, `prepend`, `move`, `rename`, `links`, `backlinks`, `unresolved`, `files`, `open`, and property operations

The official docs also state that the Obsidian app must be running and that the CLI is intended for automation and agentic workflows.

## Preflight

Before relying on the CLI:

1. Check whether `obsidian` resolves in the current shell.
2. If not, try the app-bundled binary path directly.
3. Verify a narrow help call or simple read-only command in the current environment.

If the command surface is uncertain and browsing is available, re-check the official docs before depending on less common commands.

## Preferred Uses

Use Obsidian CLI first for:

- vault search
- reading notes
- creating notes
- appending or prepending note content
- note-aware rename and move operations
- link-aware inspection through outgoing links, backlinks, and unresolved-link checks
- property reads and writes when metadata should stay Obsidian-aware

Use direct file operations for simple safe reads and isolated non-note-aware files when that is clearly simpler.

## Targeting Rules

Use `file=` when the note name is stable and unambiguous enough to resolve like a wikilink.

Use `path=` when:

- the exact path matters
- there may be name collisions
- a folder target is required
- a move or rename needs deterministic targeting

Prefer exact paths for high-risk operations.

## Retrieval Pattern

1. For broad or exploratory tasks, read `Notes/Index.md` first when it exists.
2. Start with `search` or `search:context`.
3. Use `read` for the most relevant notes.
4. Expand with `links` and `backlinks` when relationship traversal is useful.
5. Use `unresolved` when checking vault integrity or fallout from path changes.

Prefer bounded retrieval over scanning the whole vault.

## Write Pattern

- use `create` for new notes
- use `append` or `prepend` for narrow additive changes
- use property operations for intentional metadata updates

Do not use the CLI just for its own sake. If a direct edit to an isolated system file is safer and clearer, use the file directly.

## Reliability Rules

If the CLI behaves unexpectedly in the current harness:

- retry with a narrow help or read-only command
- prefer the app-bundled binary path if `obsidian` does not resolve
- account for the possibility that sandboxed or GUI-constrained environments may emit macOS or XPC errors or hang
- if needed and allowed, retry outside the sandbox or with the permissions required by the harness

Do not keep escalating complexity around the CLI if a conservative fallback will solve the task more safely.

## Fallback

If Obsidian CLI is unavailable, hanging, or unsuitable:

- fall back to direct file reads for inspection
- fall back to direct writes only for narrow, safe edits that do not depend on note identity or path semantics
- avoid raw rename and move operations for notes unless they are clearly necessary and can be verified deliberately

When falling back, keep changes smaller than you otherwise would.

## Verification

After using Obsidian CLI for a meaningful operation:

- confirm the target note or file reflects the intended result
- confirm path-sensitive changes landed in the expected location
- confirm related note references still behave as expected when that matters

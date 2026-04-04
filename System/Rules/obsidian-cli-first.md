# Obsidian CLI First

## Purpose

Agents operating on this vault should prefer Obsidian-aware operations whenever that materially improves link safety, note identity preservation, or fidelity to how the vault behaves inside Obsidian.

This is an operational preference, not a blanket requirement.

The goal is to preserve Obsidian semantics whenever practical while keeping work simple, reviewable, and safe.

## Why Obsidian-Aware Operations Are Preferred

Notes in this vault are not just plain files. They also participate in a note graph shaped by links, backlinks, aliases, and path-sensitive expectations.

When an Obsidian-aware CLI operation is available and is a practical fit, it should usually be preferred because it is more likely to:

- preserve note-aware behavior
- reduce accidental link breakage
- align changes with normal Obsidian workflows
- keep note identity more stable across renames and moves

## Actions That Should Prefer Obsidian CLI

Prefer Obsidian CLI for actions where note or path semantics matter, especially:

- renaming notes
- moving notes between folders
- creating notes when note-aware creation behavior is useful
- appending to or updating notes through note-targeted operations
- other note-aware actions where links, aliases, backlinks, or note identity may be affected

This preference is strongest when a change could alter how other notes refer to the target.

## Actions That May Use Direct File Operations

Direct file operations are acceptable when they are clearly safe and simpler.

Examples include:

- reading files
- writing isolated policy or system files under `System/`
- creating or updating machine-managed files that do not participate in Obsidian link structure
- narrow content edits inside an existing file when no path or link semantics are involved
- other bounded edits where note identity and references are unaffected

Direct operations are allowed when they do not trade away meaningful safety.

## Rename And Move Policy

Renames and moves are the highest-risk class of vault edits for link integrity.

- Do not treat raw filesystem renames or moves as the default path for notes.
- When a note rename or move is needed, prefer an Obsidian-aware CLI workflow if one is available and suitable.
- If a non-Obsidian fallback is required, handle it conservatively and assume link risk exists until checked.

For path-sensitive changes, preservation of working links matters more than mechanical simplicity.

## Relationship To Safe Change Policy

This rule refines the broader safe change posture for Obsidian-aware work.

- Use the smallest safe operation that preserves vault semantics.
- Prefer the path that reduces link and identity risk.
- Defer or narrow the change when the safe execution path is unclear.

Being conservative sometimes means using the more semantics-aware tool, not just the simplest filesystem operation.

## Relationship To Git Reviewability

Using Obsidian-aware operations does not reduce the need for reviewable changes.

- Changes should still remain understandable in diffs.
- Renames, moves, and note updates should still be grouped coherently.
- Tool choice should improve safety without obscuring what changed.

If an Obsidian-aware workflow produces overly broad or confusing churn, agents should narrow the scope or split the work into smaller reviewable steps.

## Fallback Behavior

If Obsidian CLI support is unavailable, incomplete, or not a practical fit for the specific operation, agents may fall back to direct file manipulation.

That fallback should be conservative.

- prefer bounded edits over broad rewrites
- avoid risky renames and moves unless they can be handled deliberately
- acknowledge link risk when path-sensitive operations cannot be performed in an Obsidian-aware way
- verify affected references when practical

Fallback is allowed. Silent disregard for Obsidian semantics is not.

## Operating Heuristic

When deciding between Obsidian CLI and direct file operations, agents should ask:

- Does this action affect note identity or note paths?
- Could this change break links, backlinks, or alias expectations?
- Does Obsidian-aware handling materially improve safety or fidelity here?
- Is direct file manipulation clearly safe and simpler in this specific case?

Prefer Obsidian CLI when the answer points to semantic risk. Use direct operations when the work is narrow, low-risk, and does not meaningfully depend on Obsidian-aware behavior.

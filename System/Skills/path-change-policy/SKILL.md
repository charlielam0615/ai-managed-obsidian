---
name: path-change-policy
description: Use this skill when considering a note or file rename or move and you need to decide whether the change is justified, whether aliasing is safer, and how to verify the result without causing unnecessary churn.
---

# Path Change Policy

## When To Use

Use this skill before renaming or moving notes or other vault files whose paths may affect readability, link safety, or reviewability.

## Inputs

- the current file or note path
- the proposed new path or name
- the reason for the change
- access to note-aware inspection and link checking when available

## Output

One of:

- a justified, verified path change
- a decision to use aliases instead of renaming
- a decision to defer because the change is not worth the churn

## Decision Rules

A rename or move is justified when it materially improves the vault, for example:

- the current name is misleading or excessively noisy
- an imported filename is unreadable or unstable
- a note or document is clearly in the wrong coarse destination
- a conflict or ambiguity between items needs to be resolved

Cosmetic preference alone is usually not enough.

## Prefer Aliases When

- the current title is already stable and recognizable
- alternate phrasing would improve recall or search
- the problem is discoverability rather than correctness

## Avoid Acting When

- the benefit is minor
- the destination structure is still uncertain
- the change would trigger avoidable churn
- you cannot verify the impact on links or related references

Defer rather than guess.

## Obsidian-Aware Preference

Use the `obsidian-cli` skill for concrete CLI preflight, targeting, and fallback behavior.

When Obsidian-aware rename or move operations are available and suitable, prefer them because they better preserve note identity and align with normal vault behavior.

Important constraint:

- official docs indicate that move and rename can update internal links when automatic internal link updating is enabled in the vault
- do not assume that setting is enabled unless it has been verified

## Verification

After any rename or move:

- confirm the item exists at the new path
- confirm the old path no longer appears as a live target unintentionally
- confirm the renamed or moved note still opens and reads as expected
- inspect for affected references, especially when link updates were not verified

If verification is weak, do not continue with additional path churn.

## Related Skills

- `obsidian-cli`
- `inbox-triage`
- `document-ingestion`

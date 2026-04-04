# Linking And Naming

## Naming Conventions

Use clear, human-readable filenames.

- Note titles should be concise, descriptive, and stable enough to link to.
- PDF filenames should prefer a readable canonical form over opaque importer names.
- Avoid decorative prefixes, deep numbering schemes, or taxonomy encoded into filenames unless a clear need emerges later.

When renaming imported files, prefer names that improve recognition without overfitting to a temporary classification system.

## Obsidian Link Conventions

Prefer Obsidian-native links for note-to-note references.

- Use wiki links when they are the normal local convention.
- Use standard Markdown links where they are clearer or required for non-note files.
- Keep links legible and resilient.

Link choices should favor long-term readability over clever automation tricks.

## Path Stability

Treat paths as part of the operating surface of the vault.

- Avoid churn in filenames and folder placement.
- Do not rename or move files casually.
- Prefer stable locations unless there is a clear organizational benefit.

## Safe Rename And Move Policy

When paths must change:

- prefer Obsidian-aware rename and move workflows that preserve note links
- update affected references rather than leaving silent breakage behind
- keep changes bounded and reviewable

Raw filesystem moves are acceptable only when link safety is not at risk or when all affected references are being handled deliberately.

## Aliases vs Renames

Prefer aliases when the current title is already stable enough but alternate names would improve discovery.

- use an alias to support recall, searchability, or alternate phrasing
- use a rename when the current name is actively misleading, noisy, or unstable

Do not rename files only to satisfy minor style preferences when an alias would achieve the goal with less disruption.

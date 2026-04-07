# Processed Note Metadata Examples

These are reference examples for the minimum processed-note metadata contract.

They are examples only. They are not mandatory templates.

## Example: English Processed Note

```md
---
lang: en
summary: Working note on sparse autoencoder intuition for mechanistic interpretability.
---

# Sparse Autoencoder Intuition

This note collects intuitions, examples, and follow-up questions about sparse autoencoders.
```

Why this is enough:

- `lang` tells agents the note is English-first
- `summary` gives immediate retrieval value in the shared English retrieval space

## Example: Non-English Processed Note

```md
---
lang: zh
summary: Working note on knowledge graph linking patterns inside the vault.
aliases:
  - Knowledge Graph Linking
  - Vault Linking Patterns
search_terms:
  - knowledge graph
  - linking
  - note graph
  - vault structure
---

# 知识图谱连接模式

这是一篇关于知识库内部链接模式的工作笔记。
```

Why the extra fields exist:

- `summary` gives an English retrieval bridge
- `aliases` help title-level recall from English queries
- `search_terms` help concept-level retrieval even when the note title is not in English

## Example: Paper Note

```md
---
lang: en
summary: Paper note on sparse autoencoders and feature decomposition in transformer activations.
---

# Sparse Autoencoders For Feature Discovery

- PDF: [[Library/Papers/sparse-autoencoders.pdf]]
- Authors: Example Author, Another Author
- Year: 2025
```

This example shows that paper notes still follow the same minimum processed-note contract, even when they also carry paper-specific metadata.

---
title: InlineHilite
long_title: InlineHilite Extension
summary: Syntax highlighting for inline code elements
mt_type: extensionEn
---

<span class="badge bg-primary">Supported Versions:>=2.12</span>

## 概要
The InlineHilite extension allows you to add syntax highlighting to Markdown inline code.

<p>In a paragraph, by writing <code>`:::language code`</code>, the code will have inline highlighting corresponding to the <code>language</code>. </p>

This syntax is implemented by `PyMdown Extensions`.
For more information on the syntax, see [InlineHilite - PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/extensions/inlinehilite).

## Example

**Example**

```md
To import a module in Python, use the statement `:::py3 import`.
For example, to import a `sys` module, write `:::py3 import sys`.
```

**Example**

To import a module in Python, use the statement `:::py3 import`.
For example, to import a `sys` module, write `:::py3 import sys`.

## 導入方法
Add the following line to `mkdocs.yml` in the site

```yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
```

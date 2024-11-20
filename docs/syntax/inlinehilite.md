---
title: インラインハイライト
summary: インラインコード要素にシンタックスハイライトをつけます
mt_title: :::lang name
mt_type: syntax
---

<span class="badge bg-primary">対応バージョン:>=2.10</span>

## 概要
インラインハイライト構文を使うと、Markdownのインラインコードに、シンタックスハイライトをつけることができます。

<p>段落中で、<code>`:::language code`</code>と書くことで、コードに<code>language</code>に対応したインラインハイライトがつきます。</p>

この構文は、`PyMdown Extensions`によって実装されます。
構文の詳細については、[InlineHilite - PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/extensions/inlinehilite/)をご覧ください。

## 例

**例**

```md
Pythonでモジュールを読み込むには、`:::py3 import`文を使います。
例えば、`sys`モジュールを読み込むには、`:::py3 import sys`と書きます。
```

**結果**

Pythonでモジュールを読み込むには、`:::py3 import`文を使います。
例えば、`sys`モジュールを読み込むには、`:::py3 import sys`と書きます。

## 導入方法
サイト内の`mkdocs.yml`に、次の行を追加します。

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

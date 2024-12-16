---
title: サイトを作成する
summary: この記事では、新たにサイトを作成する方法を説明します
date : 2022-10-22
order: 2
---

### プロジェクトを作成する
プロジェクトを作成すると、作業ディレクトリにサイトの作成を開始するために必要なファイルやディレクトリが作成されます。

この記事では、`mydocs`というディレクトリにサイトを作成します。ディレクトリのパスは好きなものを使用できます。

ターミナルやコマンドプロンプトなどを開いて、次のコマンドを実行します。

```shell title="Shell"
mkdocs new mydocs
```

これで、`mydocs`にプロジェクトが作成されました。

### mkdocs.yml を編集する
`mydocs`直下に`mkdocs.yml`という名前のファイルが作成されています。このファイルを開きます。

次のテンプレートをコピーして貼り付けます。

```yaml title="mkdocs.yml"
site_name: MyDocs

docs_dir : 'docs'

extra_javascript:
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

theme: lantana
    locale: ja

visible_search : true

plugins:
    - search:
        lang : 'ja'
        min_search_length: 2
    - git-revision-date
    - awesome-pages
    - git-authors:
        show_email_address: true
        count_empty_lines: true
        fallback_to_empty: false
        enabled: true

markdown_extensions:
    - lantana
    - lantana.alerts2
    - lantana.selector
    - lantana.extensions.mdx_embedly
    - lantana.extensions.mdx_wsid
    - attr_list
    - lantana.cards
    - lantana.mtables
    - footnotes
    - pymdownx.highlight:
       anchor_linenums: true
    - lantana.codeblock_copybtn
    - admonition
    - pymdownx.arithmatex:
       generic : true
    - md_in_html
    - pymdownx.details
    - pymdownx.superfences:
        custom_fences:
          - name: mermaid
            class: mermaid
            format: !!python/name:mermaid2.fence_mermaid
    - lantana.mermaid_precompile
    - pymdownx.snippets
    - pymdownx.critic
    - pymdownx.caret
    - pymdownx.keys
    - pymdownx.mark
    - pymdownx.tilde
    - pymdownx.tasklist:
        custom_checkbox: true
    - pymdownx.magiclink
    - pymdownx.striphtml
    - lantana.link_opennewtab
    - lantana.alerts
    - lantana.accordion
    - lantana.tabs
```

設定ファイルには、他にもいくつかの項目があります。どのような設定があるかを知るには、[設定ファイル](/cheatsheet/config)を参照してください。

### プロジェクトをビルドする
設定が完了したら、プロジェクトをビルドします。

ターミナルで、次のコマンドを実行します。

```shell
mkdocs build
```
エラーなくビルドが完了したら、サイトの完成です。
### 完成したサイトを確認する
サイトが完成したら、早速確認してみましょう。
ターミナルで、次のコマンドを実行します。

```shell
mkdocs serve
```

次に、ブラウザで[http://127.0.0.1:8000](http://127.0.0.1:8000)にアクセスします。

これでプロジェクトの作成は完了です。次に、記事を執筆するには、[記事を執筆する](../write)を参照してください。

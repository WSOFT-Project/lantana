---
title: サイトを作成する
summary: この記事では、新たにサイトを作成する方法を説明します
author : Taiseiue
author_url : https://github.com/taiseiueue
date : 2022-10-22
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

language : ja


theme: lantana

visible_search : true

plugins:
    - search:
        lang : 'ja'
        min_search_length: 2
    - macros
    - awesome-pages
    - git-authors

markdown_extensions:
    - attr_list
    - pymdownx.highlight:
       anchor_linenums: true
    - admonition
    - pymdownx.arithmatex:
       generic : true
    - md_in_html
    - pymdownx.details
    - pymdownx.superfences:
        custom_fences:
          - name: mermaid
            class: mermaid
            format: !!python/name:pymdownx.superfences.fence_code_format
    - pymdownx.snippets
    - pymdownx.critic
    - pymdownx.caret
    - pymdownx.keys
    - pymdownx.mark
    - pymdownx.tilde
    - pymdownx.emoji:
        emoji_index: !!python/name:materialx.emoji.twemoji
        emoji_generator: !!python/name:materialx.emoji.to_svg
    - pymdownx.tasklist:
        custom_checkbox: true
    - pymdownx.magiclink
    - pymdownx.striphtml
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
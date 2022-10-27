---
title: サイトを作成する
summary: この記事では、新たにサイトを作成する方法を説明します
author : Taiseiue
author_url : https://github.com/Taiseiueue
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

次のテンプレートにしたがって設定を記述します。

```yaml title="mkdocs.yml"
site_name: 'サイトの名前'
copyright : 'フッターに表示する著作権表示'
language : ja

docs_dir : 'docs'

favicon : favicon.png

theme: lantana

plugins:
    - search:
        lang : 'ja'
        min_search_length: 2

markdown_extensions:
    - codehilite:
    - admonition:
    - pymdownx.superfences:
    - pymdownx.details:
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

次に、ブラウザで[http://127.0.0.1:8000](http://127.0.0.1:8000)にアクセスします。すると、このようにサイトが表示されます。

![実行例](media/site.jpg)

これでプロジェクトの作成は完了です。次に、記事を執筆するには、[記事を執筆する](../3_write)を参照してください。
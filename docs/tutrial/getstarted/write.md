---
title: 記事を執筆する
summary: この記事では、記事を執筆する方法を説明します
date : 2022-10-22
order: 1
---

### ファイルを作成する
ガイド:[サイトを作成する](/guide/2_create)の手順でサイトを作成していれば、記事は`docs`というディレクトリ内にあります。

このディレクトリに`記事の名前.md`という名前でファイルを作成します。ディレクトリを作成して、その中に含めることもできます。

!!! tip
    ディレクトリ内に`index.md`というファイルを作成すると、`index.html`のようにトップページとなります。

### 記事を執筆する
記事の実際の表示を確認しながら記事を執筆できます。
ターミナルで、次のコマンドを実行します。

```shell
mkdocs serve
```

次に、ブラウザで[http://127.0.0.1:8000](http://127.0.0.1:8000)にアクセスし、左のナビバーから記事をクリックして開きます。

さぁ、いよいよ執筆開始です。任意のエディターで先ほど作成したファイルを編集します。次の例のように、記事はマークダウン形式で執筆します。

```markdown
# 記事の例
Lantanaを使って記事を執筆してみました。

記事の執筆はこんなに**簡単**です。
```

どのような構文があるかを知るには、[マークダウン](/cheatsheet/markdown)を参照してください。

記事のタイトルや概要を記述するには、メタタグを使用します。
次の例のように、メタタグはファイルの先頭に記述します。

```markdown
---
title: 記事の例
summary: この記事はサンプルです
author : me
date : 2022-10-22
---
```

どのような情報を指定できるかを知るには、[メタタグ](/cheatsheet/metatag)を参照してください。

これでこのガイドは完了です！必要になったら、いつでもこのガイドに戻ってきてください。

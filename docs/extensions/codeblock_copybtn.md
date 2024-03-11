---
title : CodeBlock CopyBtn
long_title : CodeBlock CopyBtn拡張機能
summary : この記事では、CodeBlock CopyBtn拡張機能の使用方法について説明します
date : 2024-03-11
---

<span class="badge bg-primary">対応バージョン:>=2.9.1</span>

CodeBlock CopyBtn拡張機能は、コードブロックの右上にコピーボタンを追加する拡張機能です。

この拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- コードブロック右上のコピーボタン


### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - lantana.codeblock_copybtn
```

このとき、`alerts`は`codeblock_copybtn`より後に追加してください。
---
title : lantana
long_title : lantana拡張機能
summary : この記事では、lantana拡張機能の使用方法について説明します
date : 2024-03-07
mt_type: extension
---

<span class="badge bg-primary">対応バージョン:>=2.9</span>

Lantana拡張機能は、Lantanaの一部のUIをレンダリングするための拡張機能です。

!!!warning "必須コンポーネント"
    Lantana拡張機能は、Lantanaの必須コンポーネントの一部です。
    Lantanaを使用するときは、この拡張機能を必ず使用するようにしてください。

Lantana拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- 最適化された画像の表示
- リッチなテーブル
- 最適化された引用

この拡張機能は、従来ユーザーサイドでJavaScriptを使用して行っていたレンダリング処理を事前に行うために導入されました。

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - lantana
```

このとき、`lantana`は最後の行に追加してください。
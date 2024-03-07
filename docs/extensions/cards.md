---
title : Cards
long_title : Cards拡張機能
summary : この記事では、Cards拡張機能の使用方法について説明します
date : 2024-03-07
---

<span class="badge bg-primary">対応バージョン:>=2.9</span>

Cards拡張機能は、Lantanaに指定ディレクトリの記事一覧を生成する拡張機能です。
この拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- Cardsコンポーネント

### 使用方法
以下の構文で使用できます。
ディレクトリ名は`docs`ディレクトリからの相対パスを使用します。

!!!note "エスケープ解除"
    以下の例ではすべてエスケープのためのバックスラッシュ(`\`)が入っています。
    これは、この拡張機能がコードブロック中でも作用するためです。
    実際に使用する際はバックスラッシュ文字を削除してください。

```md title="index.md"
=\"ディレクトリ名"|[オプション(カンマ区切り)]\=

**例1**

=\"extensions"\=

**例2**

=\"extensions"|[style-lite]\=
```

**例1**

="extensions"=

**例2**

="extensions"|[style-lite]=

#### オプション
Cards構文中で使用できるオプションは以下の通りです。

オプション|説明
---|---
`include-index`|ディレクトリ内の`index.md`ファイルを一覧に含めます
`include-subdir`|ディレクトリ内のサブディレクトリの`index.md`ファイルを一覧に含めます
`style-lite`|一覧をカード形式ではなく箇条書きとして出力します

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - mdx_cards
      (中略)
```
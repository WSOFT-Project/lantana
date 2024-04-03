---
title : Accordion
long_title : Accordion拡張機能
summary : この記事では、accordion拡張機能の使用方法について説明します
date : 2024-03-11
---

<span class="badge bg-primary">対応バージョン:>=2.9.4</span>

Accordion拡張機能は、Lantanaに折り畳み要素を追加する拡張機能です。

この拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- 折り畳み要素

### 使用方法
折り畳みを使用するには、`??? タイトル`で囲みます。

```md title="Markdown"
??? "ポラーノの広場"
    あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。
    またそのなかでいっしょになったたくさんのひとたち、ファゼーロとロザーロ、羊飼のミーロや、顔の赤いこどもたち、地主のテーモ、山猫博士のボーガント・デストゥパーゴなど、いまこの暗い巨きな石の建物のなかで考えていると、みんなむかし風のなつかしい青い幻燈のように思われます。では、わたくしはいつかの小さなみだしをつけながら、しずかにあの年のイーハトーヴォの五月から十月までを書きつけましょう。
```

**結果**

??? "ポラーノの広場"
    あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。
    またそのなかでいっしょになったたくさんのひとたち、ファゼーロとロザーロ、羊飼のミーロや、顔の赤いこどもたち、地主のテーモ、山猫博士のボーガント・デストゥパーゴなど、いまこの暗い巨きな石の建物のなかで考えていると、みんなむかし風のなつかしい青い幻燈のように思われます。では、わたくしはいつかの小さなみだしをつけながら、しずかにあの年のイーハトーヴォの五月から十月までを書きつけましょう。

また、最初から開いておくには、`???+ タイトル`で囲みます。

```md title="Markdown"
???+ "AliceScriptのツアー"
    AliceScript(「アリススクリプト」と読みます)は、.NET上で動作する軽量なスクリプト言語です。AliceScriptはJavaScriptと同等の書きやすさをもち、かつC#などの読みやすさや安全性も備えています。AliceScriptはC言語やC#、Java、JavaScript、PHPを使用したことのあるプログラマーならすぐに使いこなすことができます。
```

**結果**

???+ "AliceScriptのツアー"
    AliceScript(「アリススクリプト」と読みます)は、.NET上で動作する軽量なスクリプト言語です。AliceScriptはJavaScriptと同等の書きやすさをもち、かつC#などの読みやすさや安全性も備えています。AliceScriptはC言語やC#、Java、JavaScript、PHPを使用したことのあるプログラマーならすぐに使いこなすことができます。

#### 色のカスタマイズ

展開時の色をカスタマイズすることもできます。このとき、指定したタグと実際の色との対応は[Alerts](./alerts.md)と同じです。

```md title="Markdown"
???+ note "メモ"
    `note`で使用できる装飾です。

???+ abstract
    `abstract`で使用できる装飾です。

???+ info
    `info`で使用できる装飾です。

???+ tip
    `tip`で使用できる装飾です。

???+ success
    `success`で使用できる装飾です。

???+ question
    `question`で使用できる装飾です。

???+ warning
    `warning`で使用できる装飾です。

???+ failure
    `failure`で使用できる装飾です。

???+ danger
    `danger`で使用できる装飾です。

???+ bug
    `bug`で使用できる装飾です。

???+ example
    `example`で使用できる装飾です。

???+ quote
    `quote`で使用できる装飾です。
```

**結果**

???+ note "メモ"
    `note`で使用できる装飾です。

???+ abstract
    `abstract`で使用できる装飾です。

???+ info
    `info`で使用できる装飾です。

???+ tip
    `tip`で使用できる装飾です。

???+ success
    `success`で使用できる装飾です。

???+ question
    `question`で使用できる装飾です。

???+ warning
    `warning`で使用できる装飾です。

???+ failure
    `failure`で使用できる装飾です。

???+ danger
    `danger`で使用できる装飾です。

???+ bug
    `bug`で使用できる装飾です。

???+ example
    `example`で使用できる装飾です。

???+ quote
    `quote`で使用できる装飾です。

#### アコーディオンのネスト
アコーディオン内にアコーディオンを含めることもできます。

```md title="Markdown"
???+ note "巻き込み"
    ???+ note "巻き込み"
        これはネストされたアコーディオンです。
```

**結果**

???+ note "巻き込み"
    ???+ note "巻き込み"
        これはネストされたアコーディオンです。

#### アコーディオン回避
`noaccordion`クラスを使用することで、拡張機能によって`details`要素がアコーディオンに変換されるのを回避できます。

```html title="Markdown"
<details class="noaccordion">
  <summary>Details</summary>
  このdetailsはアコーディオンになりません。
</details>
```

**結果**

<details class="noaccordion">
  <summary>Details</summary>
  このdetailsはアコーディオンになりません。
</details>

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - lantana.accordion
```

このとき、`accordion`は`superfences`より後に追加してください。
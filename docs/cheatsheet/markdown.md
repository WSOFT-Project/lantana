---
title: マークダウン記法
summary: この記事では、Lantanaで使用できるマークダウン記法の一覧を示します
author : Taiseiue
author_url : https://github.com/taiseiue
date : 2022-10-22
---
### 普通のテキスト
そのまま記述可能です。
```markdown title="例"
Lantanaは、シンプルで軽量なMKDocsのテーマです。
HTMLの知識がなくても簡単にサイトを作成できます。

改行するには、一行空行を挟みます。
```
結果

Lantanaは、シンプルで軽量なMKDocsのテーマです。
HTMLの知識がなくても簡単にサイトを作成できます。

改行するには、一行空行を挟みます。

### エスケープ
マークダウンで意味のある文字（たとえば、\*や\#など）をテキストとして表示するには、エスケープが必要です。
```markdown title="例"
\*\#\!\`\\
```
!!! quote "結果"
    \*\#\!\`\\

### 明示的な空行
二行以上にわたって改行したい場合など、一部の場合ではHTMLの`<br/>`タグを使用します。
```html title="例"
<br/>
```

### コメント
記事にコメントを記述する方法はHTMLと同じです。ビルド時に削除されます。
```html title="例"
<!-- this is a comment. -->
```

### 見出し
Hタグを生成します。記事にタイトルが指定されていない場合、自動的に記事の一番最初の見出しがタイトルになります。

また、見出しは目次にも表示されます。
```markdown title="例"
# これはH1タグになります
## これはH2タグになります
###### これはH6タグになります
```
結果
<h1>これはH1タグになります</h1>
<h2>これはH2タグになります</h2>
<h6>これはH6タグになります</h6>
<br/>

### テキストの装飾
文章を様々に装飾する方法をまとめて紹介します。
```markdown title="例"
_ か * で囲むとHTMLのemタグになり、 *このように* 表示されます。

__ か ** で囲むとHTMLのstrongタグになり、**このように** 表示されます。

それらを組み合わせることもできます。*** で囲むと、***このように*** 表示されます。

~~ で囲むと打消し線になり、　~~このように~~ 表示されます。

^^ で囲むと下線がつき、^^このように^^ 表示されます。

== で囲むとハイライトがつき、==このように== 表示されます。

~ で囲むと下付き文字になり、使用すると~このように~表示されます。

^ で囲むと上付き文字になり、使用すると^このように^表示されます。

++ で囲むと++ctrl+alt+del++のようにキーボードのキーを表現できます。

また、`print("Hello,World!");`と記述することでコードをインライン表示できます。

```
_ か \* で囲むとHTMLのemタグになり、 *このように* 表示されます。

__ か \*\* で囲むとHTMLのstrongタグになり、**このように** 表示されます。

それらを組み合わせることもできます。\*\*\* で囲むと、***このように*** 表示されます。

\~\~ で囲むと打消し線になり、　~~このように~~ 表示されます。

\^\^ で囲むと下線がつき、^^このように^^ 表示されます。

\=\= で囲むとハイライトがつき、==このように== 表示されます。

\~ で囲むと下付き文字になり、使用すると~このように~表示されます。

\^ で囲むと上付き文字になり、使用すると^このように^表示されます。

\+\+ で囲むと++ctrl+alt+del++のようにキーボードのキーを表現できます。

また、`print("Hello,World!");`と記述することでコードをインライン表示できます。

### コードブロック
```` ``` ```` で囲むことでコードとして認識され、初めを```` ```言語名 ```` とすることでシンタックスハイライトがつきます。`title="タイトル"`とすることでファイル名なども表現できます。また、`linenums="1"`とすると行番号を表示できます。
```markdown title="例"
``` csharp title="Program.cs" linenums="1"
using System;

public class Program
 {
    public static void Main()
     {
            Console.WriteLine("Hello World!");
     }
 }
```

結果
``` csharp title="Program.cs" linenums="1"
using System;

public class Program
 {
    public static void Main()
     {
            Console.WriteLine("Hello World!");
     }
 }
```

!!! warning "注意"
    上記のサンプルでは末尾の```` ``` ````が欠落しています。（マークダウンの制約）コピペで使用する際はご注意ください。

### 数式
`\$\$`で囲むことでTeX記法を用いて数式を記述できます。
```markdown title="例"
$$
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
$$
```
結果

$$
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
$$

`$`または`\(...\)`で囲むことで、数式を文中に埋め込むこともできます。
```markdown title="例"
ディッフィー・ヘルマン鍵共有プロトコルでは、まず大きな素数 ${\displaystyle p}p$ と、
${\displaystyle p-1}p-1$ を割り切る大きな素数 ${\displaystyle q}q$ を用意します。
また、 ${\displaystyle g}g$ を
${\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}{\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}$ の元で、
位数が ${\displaystyle q}q$ である値とします。
この ${\displaystyle p,q,g}{\displaystyle p,q,g}$ の値は公開されているものとします。
```
結果

ディッフィー・ヘルマン鍵共有プロトコルでは、まず大きな素数 ${\displaystyle p}p$ と、 ${\displaystyle p-1}p-1$ を割り切る大きな素数 ${\displaystyle q}q$ を用意します。また、 ${\displaystyle g}g$ を ${\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}{\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}$ の元であり、位数が ${\displaystyle q}q$ である値とします。この ${\displaystyle p,q,g}{\displaystyle p,q,g}$ の値は公開されているものとします。

### 順序なしリスト
リストの上には空行が必要です。
```markdown title="例"
* 文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります
+ 記号のあとには**スペースが必要**です
- 同じリストでは同じ記号を使うことを推奨します。
```
結果

* 文頭に"`*`"、"`+`"、"`-`"のいずれかを入れると順序なしリストになります
+ 記号のあとには**スペースが必要**です
- 同じリストでは同じ記号を使うことを推奨します。

### 番号付きリスト
リストの上には空行が必要です。
```markdown title="例"
1. 文頭に"数字."を入れると番号付きリストになります。
1. "数字."のあとには**スペースが必要**です
1. すべての数字を1にすると、自動的に番号が付きます。
```
結果

1. 文頭に"`数字.`"を入れると番号付きリストになります。
1. "`数字.`"のあとには**スペースが必要**です
1. すべての数字を1にすると、自動的に番号が付きます。

### タスクリスト
順序なしリストの記述の後ろに[ ]を入れるとチェックボックスが生成されます。
また、チェックが入った状態のボックスを生成する場合は[x]を入力します。
```markdown title="例"
- [ ] タスク1
- [x] タスク2
```
結果

- [ ] タスク1
- [x] タスク2

### 水平線
```markdown title="例"
---
```
結果
---

### URL
Urlやメールアドレスを書くだけで、自動的にリンクになります。
```markdown title="例"
https://lantana.wsoft.ws

info@wsoft.ws
```
結果

https://lantana.wsoft.ws

info@wsoft.ws

### リンク
```markdown title="例"
[リンク](about:blank)
```
結果

[リンク](about:blank)

### タイトル付きリンク
タイトルはリンクをホバーした時に表示されます。
```markdown title="例"
[リンク](about:blank "タイトル")
```
結果

[リンク](about:blank "タイトル")

### リンクの使いまわし
```markdown title="例"
[link]: about:blank
[ここ][link]と[ここ][link]は同じになります。
```
結果

[link]: about:blank
[ここ][link]と[ここ][link]は同じになります。

また、[link]という書き方もできます。


### 画像
```markdown title="例"
![代替テキスト](/favicon.png)
```

結果

![代替テキスト](/favicon.png)


### 表
Bootstrapの制約により、ヘッダーでは左右中央揃えが適用されません

```markdown title="例"
| Left align | Right align | Center align |
|:-----------|------------:|:------------:|
| This       | This        | This         |
| column     | column      | column       |
| will       | will        | will         |
| be         | be          | be           |
| left       | right       | center       |
| aligned    | aligned     | aligned      |
```

結果

| Left align | Right align | Center align |
|:-----------|------------:|:------------:|
| This       | This        | This         |
| column     | column      | column       |
| will       | will        | will         |
| be         | be          | be           |
| left       | right       | center       |
| aligned    | aligned     | aligned      |

### 引用
```markdown title="例"
> 文頭に>を置くことで引用になります。
> 複数行にまたがる場合、改行のたびにこの記号を置く必要があります。
> 
> 引用の中に別のMarkdownを使用することも可能です。
> 
> > これはネストされた引用です。
```
結果
> 文頭に>を置くことで引用になります。
> 複数行にまたがる場合、改行のたびにこの記号を置く必要があります。
> 
> 引用の中に別のMarkdownを使用することも可能です。
> 
> > これはネストされた引用です。

### 図形
Lantanaは規定でmermaid.jsをサポートします。mermaid.jsを使うと、複雑な図形を簡単に挿入できます。
```markdown title="例"
<div class="mermaid">
  sequenceDiagram
    本部->>隊長: レンジャー1、状況を報告しろ！
    隊長->>本部:巨大生物と交戦、数匹を撃破しました！
    本部->>隊長:なんだと！？そんな馬鹿な！
    隊員-->>隊員:どうなってんだ……なんで巨大生物が？
    隊員->>隊長:7年ぶりの巨大生物だ。今や絶滅危惧種だぞ！
    隊長->>隊員:危惧は無用だ、絶滅させろ！
    隊員->>隊長:Yes,sir!
    loop 無線
      本部->>隊長:聞こえないぞ、繰り返せ！
    end
</div>
```
結果
<div class="mermaid">
  sequenceDiagram
    本部->>隊長: レンジャー1、状況を報告しろ！
    隊長->>本部:巨大生物と交戦、数匹を撃破しました！
    本部->>隊長:なんだと！？そんな馬鹿な！
    隊員-->>隊員:どうなってんだ……なんで巨大生物が？
    隊員->>隊長:7年ぶりの巨大生物だ。今や絶滅危惧種だぞ！
    隊長->>隊員:危惧は無用だ、絶滅させろ！
    隊員->>隊長:Yes,sir!
    loop 無線
      本部->>隊長:聞こえないぞ、繰り返せ！
    end
</div>

### アラート
目を引く形で説明したい場合、`!!! 種類 "タイトル"`で囲みます。

```markdown title="例"
!!! note "メモ"
    `note`で使用できる装飾です。
```
結果
!!! note "メモ"
    `note`で使用できる装飾です。

!!! abstract
    `abstract`で使用できる装飾です。

!!! info
    `info`で使用できる装飾です。

!!! tip
    `tip`で使用できる装飾です。

!!! success
    `success`で使用できる装飾です。

!!! question
    `question`で使用できる装飾です。

!!! warning
    `warning`で使用できる装飾です。

!!! failure
    `failure`で使用できる装飾です。

!!! danger
    `danger`で使用できる装飾です。

!!! bug
    `bug`で使用できる装飾です。

!!! example
    `example`で使用できる装飾です。

!!! quote
    `quote`で使用できる装飾です。

### スニペットの埋め込み
`--8<--`で囲い、その中にファイル名を書き込むと、そのファイルを埋め込みます。
```markdown title="例"
;--8<--
snippet.md
;--8<--
```
### HTMLの埋め込み
HTMLコードは、そのまま記述することで埋め込むことができます。
```html title="例"
<h4>これはHTMLのH4タグです</h4>
```
結果
<h4>これはHTMLのH4タグです</h4>

### 属性の追加
`{: 属性名}`とするとマークダウンで生成される要素に特定の属性を追加することができます。
```markdown title="例"
### この要素にはqueryというIdがつきます {: #query }
```
結果

以下のようなHTMLが生成されます
```html
<h3 id="query">この要素にはqueryというIdがつきます</h3>
```

### コンテンツの埋め込み
コンテンツを埋め込みカードで表示するには、Urlのhttp部分をembedに置き換えて書きます。httpsではembedsとします。
```markdown title="例"
e mbeds://youtube.com/embed/M7lc1UVf-VE
```
結果

embeds://youtube.com/embed/M7lc1UVf-VE
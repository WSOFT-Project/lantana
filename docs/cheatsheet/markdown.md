---
title: マークダウン記法
summary: この記事では、Lantanaで使用できるマークダウン記法の一覧を示します
date : 2022-10-22
order : 1
---

Lantanaの記事は、すべてMarkdown記法で記述します。
Lantanaの記事は、[Python Markdown(PyMdown)](https://facelessuser.github.io/PyMdown/)を使ってHTMLにレンダリングされます。
Lantanaでは、一般的なMarkdown記法に加えて独自の記法や、[拡張機能](../extensions/index.md)で導入されている記法を使用できます。
この記事では、Lantanaで使用できるMarkdown記法の一覧を示します。

この記事のサンプルは、Markdown記法とビルド結果のHTML、最終的な表示を順番に示します。もしあなたがMarkdownでどのような記事を書けるか調べている場合、「表示」タブを確認することをおすすめします。以下のボタンをクリックして、すべての表示を一斉に切り替えられます。

<div class="btn-group btn-group-sm padding-bottom" role="group">
    <button type="button" id="switch-btn-1" class="btn btn-outline-primary">Markdown</button>
    <button type="button" id="switch-btn-2" class="btn btn-outline-primary">HTML</button>
    <button type="button" id="switch-btn-3" class="btn btn-outline-primary">表示</button>
</div>

<br/>
記事の先頭に書く、記事のタイトルや説明などを設定するメタタグの書き方を知るには、[メタタグ](./metatag.md)をご覧ください。

## 見出し
記事に見出しをつけます。見出しは目次の表示され、見出しへのリンクが生成されます。また、記事にタイトルが指定されていない場合、自動的に記事の一番最初の見出しがタイトルになります。

=== "Markdown"

    ```markdown
    ## これはH2タグになります
    ### これはH3タグになります
    #### これはH4タグになります
    ```
=== "HTML"

    ```html
    <h2>これはH2タグになります</h2>
    <h3>これはH3タグになります</h3>
    <h4>これはH4タグになります</h4>
    ```
=== "表示"

    <h2>これはH2タグになります</h2>
    <h3>これはH3タグになります</h3>
    <h4>これはH4タグになります</h4>
    ---

## テキスト
Markdownでテキストを記述する方法を説明します。
#### 基本的なテキスト
装飾や特殊文字の無いテキストは、そのまま記述します。

=== "Markdown"

    ```markdown
    Lantanaは、シンプルで軽量なMKDocsのテーマです。
    HTMLの知識がなくても簡単にサイトを作成できます。

    段落を変えるには、1行空行を挟みます。
    段落を変えないで改行するには、  
    行末に半角スペースを2つ付けます。
    ```
=== "HTML"

    ```html
    <p>Lantanaは、シンプルで軽量なMKDocsのテーマです。
    HTMLの知識がなくても簡単にサイトを作成できます。</p>
    <p>段落を変えるには、1行空行を挟みます。
    段落を変えないで改行するには、<br>
    行末に半角スペースを2つ付けます。</p>
    ```
=== "表示"

    Lantanaは、シンプルで軽量なMKDocsのテーマです。
    HTMLの知識がなくても簡単にサイトを作成できます。

    段落を変えるには、1行空行を挟みます。
    段落を変えないで改行するには、  
    行末に半角スペースを2つ付けます。
    ---

#### エスケープ
特殊文字（たとえば、\*や\#など）をテキストとして表示するには、`\`を使って文字をエスケープする必要があります。

=== "Markdown"

    ```markdown
    Markdownで特殊文字を表示するには、\\を使って文字をエスケープします。
    例えば、\*や\#、\!、\`などをエスケープできます。

    HTMLタグをエスケープするには、<br/\>のように書きます。
    ```
=== "HTML"

    ```html
    <p>Markdownで特殊文字を表示するには、\を使って文字をエスケープします。
    例えば、*や#、!、`などをエスケープできます。</p>
    <p>HTMLタグをエスケープするには、&lt;br/&gt;のように書きます。</p>
    ```
=== "表示"

    Markdownで特殊文字を表示するには、\\を使って文字をエスケープします。
    例えば、\*や\#、\!、\`などをエスケープできます。

    HTMLタグをエスケープするには、<br/\>のように書きます。

    ---

#### 装飾
文章を様々に装飾する方法をまとめて紹介します。

=== "Markdown"

    ```markdown
    付けたい部分を\*\*(アスタリスク1つ)で囲むと、**太字**に、
    \*(アスタリスク1つ)で囲むと、*斜体*になります。

    \*\*\*(アスタリスク3つ)で囲むことで、太字と斜体を***組み合わせる***こともできます。

    付けたい部分を\~(チルダ1つ)で囲むと~下付き文字~に、
    \^(キャレット1つ)で囲むと^上付き文字^になります。

    \~\~(チルダ2つ)で囲むと~~打ち消し線~~が、
    \^\^(キャレット2つ)で囲むと^^下線^^が、
    \=\=(イコール2つ)で囲むと==ハイライト==がつきます。
    ```
=== "HTML"

    ```html
    <p>付けたい部分を**(アスタリスク1つ)で囲むと、<strong>太字</strong>に、
    *(アスタリスク1つ)で囲むと、<em>斜体</em>になります。</p>
    <p>***(アスタリスク3つ)で囲むことで、太字と斜体を<strong><em>組み合わせる</em></strong>こともできます。</p>
    <p>付けたい部分を~(チルダ1つ)で囲むと<sub>下付き文字</sub>に、
    ^(キャレット1つ)で囲むと<sup>上付き文字</sup>になります。</p>
    <p>~~(チルダ2つ)で囲むと<del>打ち消し線</del>が、
    ^^(キャレット2つ)で囲むと<ins>下線</ins>が、
    ==(イコール2つ)で囲むと<mark>ハイライト</mark>がつきます。</p>
    ```
=== "表示"

    付けたい部分を\*\*(アスタリスク1つ)で囲むと、**太字**に、
    \*(アスタリスク1つ)で囲むと、*斜体*になります。

    \*\*\*(アスタリスク3つ)で囲むことで、太字と斜体を***組み合わせる***こともできます。

    付けたい部分を\~(チルダ1つ)で囲むと~下付き文字~に、
    \^(キャレット1つ)で囲むと^上付き文字^になります。

    \~\~(チルダ2つ)で囲むと~~打ち消し線~~が、
    \^\^(キャレット2つ)で囲むと^^下線^^が、
    \=\=(イコール2つ)で囲むと==ハイライト==がつきます。

    ---

#### 脚注
`[^1]`のように文章の任意の場所に脚注へのリンクを設置すると、ページの末尾の説明へ移動します。
説明は文章中の任意の場所で`[^1]: <説明>`とすることで記述できます。

=== "Markdown"
    ```md
    そのころわたくしは、モリーオ市の博物局に勤めて居りました。
    十八等官 [^1]でしたから役所のなかでも、ずうっと下の方でしたし俸給[^2]もほんのわずかでしたが、受持ちが標本の採集や整理で生れ付き好きなことでしたから、わたくしは毎日ずいぶん愉快にはたらきました。

    [^1]: ロシア帝国では、軍隊、政府、および宮廷における地位と階級を**[官等表](https://en.wikipedia.org/wiki/Table_of_Ranks)**と呼ばれるもので管理していました。
    [^2]: 役所や会社に務める人の給料のことを指す言葉です。
    ```

=== "HTML"
    
    ```html
    <p>そのころわたくしは、モリーオ市の博物局に勤めて居りました。
    十八等官 <sup id="fnref2:1"><a class="footnote-ref" href="#fn:1">1</a></sup>でしたから役所のなかでも、ずうっと下の方でしたし俸給<sup id="fnref2:2"><a class="footnote-ref" href="#fn:2">2</a></sup>もほんのわずかでしたが、受持ちが標本の採集や整理で生れ付き好きなことでしたから、わたくしは毎日ずいぶん愉快にはたらきました。</p>

    <!-- 以下が、ページ末尾に生成されます -->
     <div class="footnote">
        <hr>
        <ol>
            <li id="fn:1">
                <p>ロシア帝国では、軍隊、政府、および宮廷における地位と階級を<strong><a href="https://en.wikipedia.org/wiki/Table_of_Ranks" rel="noopener noreferrer" target="_blank">官等表</a></strong>と呼ばれるもので管理していました。&nbsp;<a class="footnote-backref" href="#fnref:1" title="Jump back to footnote 1 in the text">↩</a></p>
            </li>
            <li id="fn:2">
                <p>役所や会社に務める人の給料のことを指す言葉です。&nbsp;<a class="footnote-backref" href="#fnref:2" title="Jump back to footnote 2 in the text">↩</a></p>
            </li>
        </ol>
    </div>
    ```
=== "表示"

    そのころわたくしは、モリーオ市の博物局に勤めて居りました。
    十八等官 [^1]でしたから役所のなかでも、ずうっと下の方でしたし俸給[^2]もほんのわずかでしたが、受持ちが標本の採集や整理で生れ付き好きなことでしたから、わたくしは毎日ずいぶん愉快にはたらきました。

    [^1]: ロシア帝国では、軍隊、政府、および宮廷における地位と階級を**[官等表](https://en.wikipedia.org/wiki/Table_of_Ranks)**と呼ばれるもので管理していました。
    [^2]: 役所や会社に務める人の給料のことを指す言葉です。

    ---

## リンク
記事にリンクを貼って、サイト内の他のページや他のサイトとリンクできます。

#### 基本的なリンク
リンクには、テキストとUrlを設定します。
[Link OpenNewTab](../extensions/lantana/link_opennewtab.md)拡張機能を使用している場合、自動的に他のサイトへのリンクが新規タブで開きます。

=== "Markdown"

    ```markdown
    サイト内の記事にリンクを貼るには、記事のMarkdownファイルへのパスを書きます。
    例えば、[設定ファイル](./config.md)と書きます。
    
    外部サイトへのリンクは、絶対Urlで書きます。
    例えば、[example.com](https://example.com/)と書きます。
    ```
=== "HTML"

    ```html
    <p>サイト内の記事にリンクを貼るには、記事のMarkdownファイルへのパスを書きます。
    例えば、<a href="../config/">設定ファイル</a>と書きます。</p>
    <p>外部サイトへのリンクは、絶対Urlで書きます。
    例えば、<a href="https://example.com/" rel="noopener,noreferrer" target="_blank">example.com</a>と書きます。</p>
    ```
=== "表示"

    サイト内の記事にリンクを貼るには、記事のMarkdownファイルへのパスを書きます。
    例えば、[設定ファイル](./config.md)と書きます。
    
    外部サイトへのリンクは、絶対Urlで書きます。
    例えば、[example.com](https://example.com/)と書きます。

    ---

#### 自動リンク
Urlやメールアドレスを書くだけで、自動的にリンクになります。

=== "Markdown"

    ```markdown
    https://example.com/

    user@example.com
    ```
=== "HTML"

    ```html
    <p><a href="https://example.com/" rel="noopener noreferrer" target="_blank">https://example.com/</a></p>
    <p><a href="mailto:user@example.com">user@example.com</a></p>
    ```
=== "表示"

    https://example.com/

    user@example.com

    ---

#### タイトル付きリンク
HTMLのtitle属性を指定できます。
一部のブラウザでリンクをホバーした時に表示されます。

=== "Markdown"

    ```markdown
    [WSOFT](https://wsoft.ws/ "WSOFTのサイト")をぜひご覧になってください。
    ```
=== "HTML"

    ```html
    <p><a href="https://wsoft.ws/" rel="noopener noreferrer" target="_blank" title="WSOFTのサイト">WSOFT</a>をぜひご覧になってください。</p>
    ```
=== "表示"

    [WSOFT](https://wsoft.ws/ "WSOFTのサイト")をぜひご覧になってください。

    ---

#### 複数リンク
リンクを定義して、簡単に複数の場所で使いまわせます。

=== "Markdown"

    ```markdown
    [WSOFT]は、Lantanaの開発元です。[WSOFTのサイト][WSOFT]で、他の作品もご覧いただけます。

    [WSOFT]: https://wsoft.ws/
    ```
=== "HTML"

    ```html
    <p><a href="https://example.com/" rel="noopener noreferrer" target="_blank">https://example.com/</a></p>
    <p><a href="mailto:user@example.com">user@example.com</a></p>
    ```
=== "表示"

    [WSOFT]は、Lantanaの開発元です。[WSOFTのサイト][WSOFT]で、他の作品もご覧いただけます。

    [WSOFT]: https://wsoft.ws/

    ---

## 箇条書き
#### 基本の箇条書き
箇条書きで書くには、\*か\*、\+のいずれかを文頭につけます。
箇条書きの上には空行が必要です。

=== "Markdown"

    ```markdown
    - 文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります
    - 記号のあとには**スペースが必要**です
    - 同じリストでは同じ記号を使うことを推奨します。
    ```
=== "HTML"

    ```html
    <ul>
        <li>文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります</li>
        <li>記号のあとには<strong>スペースが必要</strong>です</li>
        <li>同じリストでは同じ記号を使うことを推奨します。</li>
    </ul>
    ```
=== "表示"

    - 文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります
    - 記号のあとには**スペースが必要**です
    - 同じリストでは同じ記号を使うことを推奨します。
  
    ---

#### 数字付きの箇条書き
数字付きの箇条書きを書くには、数字を先頭につけます。
箇条書きの上には空行が必要です。数字はどんな場合でも、ブラウザによって1から始まる数字にレンダリングされます。

=== "Markdown"

    ```markdown
    1. 文頭に"数字."を入れると番号付きリストになります。
    2. "数字."のあとには**スペースが必要**です
    3. ブラウザによって1から始まる数字にレンダリングされます。
    ```
=== "HTML"

    ```html
    <ol>
        <li>文頭に"数字."を入れると番号付きリストになります。</li>
        <li>"数字."のあとには<strong>スペースが必要</strong>です</li>
        <li>ブラウザによって1から始まる数字にレンダリングされます。</li>
    </ol>
    ```
=== "表示"

    1. 文頭に"数字."を入れると番号付きリストになります。
    2. "数字."のあとには**スペースが必要**です
    3. ブラウザによって1から始まる数字にレンダリングされます。

#### タスクリスト
箇条書きに`[ ]`を追加すると、タスクリストになり、チェックボックスが表示されます。`[x]`と書くとチェックが入ります。
順序なしリストの記述の後ろに[ ]を入れるとチェックボックスが生成されます。
また、チェックが入った状態のボックスを生成する場合は[x]を入力します。

=== "Markdown"

    ```markdown
    - [x] バナナを買う
    - [ ] りんごを買う
    - [ ] ぶどうを買う
    ```
=== "HTML"

    ```html
    <ul class="task-list">
        <li class="task-list-item"><label class="task-list-control"><input checked="" disabled="" type="checkbox"><span class="task-list-indicator"></span></label> バナナを買う</li>
        <li class="task-list-item"><label class="task-list-control"><input checked="false" disabled="" type="checkbox"><span class="task-list-indicator"></span></label> りんごを買う</li>
        <li class="task-list-item"><label class="task-list-control"><input checked="false" disabled="" type="checkbox"><span class="task-list-indicator"></span></label> ぶどうを買う</li>
    </ul>
    ```
=== "表示"

    - [x] バナナを買う
    - [ ] りんごを買う
    - [ ] ぶどうを買う

---

## コメント

HTMLと同じようにコメントが書けます。コメントはレンダリング時に削除されます。

=== "Markdown"

    ```markdown
    ここより下にコメントがあります。
    <!-- これはコメントです -->
    ```
=== "HTML"

    ```html
    <p>ここより下にコメントがあります。</p>
    ```
=== "表示"

    ここより下にコメントがあります。
    <!-- これはコメントです -->


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
```` ``` ```` で囲むことでコードとして認識され、初めを```` ```言語名 ```` とすることでシンタックスハイライトがつきます。`title="タイトル"`とすることでファイル名なども表現できます。
```markdown title="例"
``` csharp title="Program.cs"
using System;

public class Program
 {
    public static void Main()
     {
            Console.WriteLine("Hello World!");
     }
 }
 ```
```

表示

```csharp title="Program.cs"
using System;
 
public class Program
 {
    public static void Main()
     {
            Console.WriteLine("Hello World!");
     }
 }
```

`hl_lines`属性を指定すると、特定の行を強調表示できます。

```markdown title="例"
```csharp title="AnimalClasses.cs" hl_lines="6 20"
public class Animal
{
    public string Name { get;set; }
    public string Description { get;set; }

    public virtual void Move()
    {
        throw new NotImplementedException();
    }
}

public class Cat : Animal
{
    public Cat()
    {
        this.Name = "たま";
        this.Description = "吾輩は猫である。名前も決まっている。";
    }

    public override void Move()
    {
        /// ひっかく
    }
}
 ```
```

表示

```csharp title="AnimalClasses.cs" hl_lines="6 20"
public class Animal
{
    public string Name { get;set; }
    public string Description { get;set; }

    public virtual void Move()
    {
        throw new NotImplementedException();
    }
}

public class Cat : Animal
{
    public Cat()
    {
        this.Name = "たま";
        this.Description = "吾輩は猫である。名前も決まっている。";
    }

    public override void Move()
    {
        /// ひっかく
    }
}
```

!!! warning "注意"
    テーブルのデザインや一貫性の問題から、`linenums=1`属性はLantana2.0から非推奨になりました。

### インラインコードのハイライト
<span class="badge bg-primary">対応バージョン:>=2.12</span>

<pre>`:::language code`</pre>と書くことで、インラインコードにもシンタックスハイライトを適用できます。

```markdown title="Markdown"
Pythonでモジュールを読み込むには、`:::py3 import`文を使います。
例えば、`sys`モジュールを読み込むには、`:::py3 import sys`と書きます。
```

**表示**

Pythonでモジュールを読み込むには、`:::py3 import`文を使います。
例えば、`sys`モジュールを読み込むには、`:::py3 import sys`と書きます。

### 数式
`\$\$`で囲むことでTeX記法を用いて数式を記述できます。
```markdown title="例"
$$
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
$$
```
表示

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
表示

ディッフィー・ヘルマン鍵共有プロトコルでは、まず大きな素数 ${\displaystyle p}p$ と、 ${\displaystyle p-1}p-1$ を割り切る大きな素数 ${\displaystyle q}q$ を用意します。また、 ${\displaystyle g}g$ を ${\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}{\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}$ の元であり、位数が ${\displaystyle q}q$ である値とします。この ${\displaystyle p,q,g}{\displaystyle p,q,g}$ の値は公開されているものとします。

### 順序なしリスト
リストの上には空行が必要です。
```markdown title="例"
* 文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります
+ 記号のあとには**スペースが必要**です
- 同じリストでは同じ記号を使うことを推奨します。
```
表示

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
表示

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
表示

- [ ] タスク1
- [x] タスク2

### 水平線
```markdown title="例"
---
```
表示
---

### URL
Urlやメールアドレスを書くだけで、自動的にリンクになります。
```markdown title="例"
https://lantana.wsoft.ws

info@wsoft.ws
```
表示

https://lantana.wsoft.ws

info@wsoft.ws

### リンク
このサイト外へのリンクは新規タブで開かれます。
```markdown title="例"
[リンク](about:blank)

[WSOFT](https://wsoft.ws/)
```
表示

[リンク](about:blank)

[WSOFT](https://wsoft.ws/)

### タイトル付きリンク
タイトルはリンクをホバーした時に表示されます。
```markdown title="例"
[リンク](about:blank "タイトル")
```
表示

[リンク](about:blank "タイトル")

### リンクの使いまわし
```markdown title="例"
[link]: about:blank
[ここ][link]と[ここ][link]は同じになります。
```
表示

[link]: about:blank
[ここ][link]と[ここ][link]は同じになります。

また、[link]という書き方もできます。


### 画像
```markdown title="例"
![代替テキスト](https://wsoft.ws/products/Alice.jpg)
```

表示

![代替テキスト](https://wsoft.ws/products/Alice.jpg)


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

表示

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
表示
> 文頭に>を置くことで引用になります。
> 複数行にまたがる場合、改行のたびにこの記号を置く必要があります。
> 
> 引用の中に別のMarkdownを使用することも可能です。
> 
> > これはネストされた引用です。

### 図形
Lantanaは規定でmermaid.jsをサポートします。mermaid.jsを使うと、複雑な図形を簡単に挿入できます。

<span class="badge bg-primary">対応バージョン:>=2.9</span>

バージョン2.9以降では、[MermaidPrecompile](../extensions/mermaid_precompiler.md)拡張機能の導入するか、[Mermaid.jsのCDN](https://www.jsdelivr.com/package/npm/mermaid)を`mkdocs.yml`内で`extra_javascript`として読み込む必要があります。PreCompileを行うにはビルド時に、CDNを読み込むには使用者に、インターネット接続が必要です。

```markdown title="例"
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

表示
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


### アラート
目を引く形で説明したい場合、`!!! 種類 "タイトル"`で囲みます。

```markdown title="例"
!!! note "メモ"
    `note`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。
```
表示
!!! note "メモ"
    `note`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! abstract
    `abstract`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! info
    `info`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! tip
    `tip`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! success
    `success`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! question
    `question`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! warning
    `warning`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! failure
    `failure`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! danger
    `danger`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! bug
    `bug`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! example
    `example`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

!!! quote
    `quote`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

### 折り畳み要素
折り畳みを使用するには、`??? タイトル`で囲みます。

```markdown title="例"
??? "ポラーノの広場"
    あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。
    またそのなかでいっしょになったたくさんのひとたち、ファゼーロとロザーロ、羊飼のミーロや、顔の赤いこどもたち、地主のテーモ、山猫博士のボーガント・デストゥパーゴなど、いまこの暗い巨きな石の建物のなかで考えていると、みんなむかし風のなつかしい青い幻燈のように思われます。では、わたくしはいつかの小さなみだしをつけながら、しずかにあの年のイーハトーヴォの五月から十月までを書きつけましょう。
```

**表示**

??? "ポラーノの広場"
    あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。
    またそのなかでいっしょになったたくさんのひとたち、ファゼーロとロザーロ、羊飼のミーロや、顔の赤いこどもたち、地主のテーモ、山猫博士のボーガント・デストゥパーゴなど、いまこの暗い巨きな石の建物のなかで考えていると、みんなむかし風のなつかしい青い幻燈のように思われます。では、わたくしはいつかの小さなみだしをつけながら、しずかにあの年のイーハトーヴォの五月から十月までを書きつけましょう。

### 記事一覧
` = "" =`で囲い、その中にディレクトリを指定すると、そのディレクトリの記事一覧を出力します。

```markdown title="例"
= "cheatsheet" =\
```

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
表示
<h4>これはHTMLのH4タグです</h4>

### 属性の追加
`{: 属性名}`とするとマークダウンで生成される要素に特定の属性を追加することができます。
```markdown title="例"
### この要素にはqueryというIdがつきます {: #query }
```
表示

以下のようなHTMLが生成されます
```html
<h3 id="query">この要素にはqueryというIdがつきます</h3>
```

<script>
function switchPreview(type){
    document.querySelectorAll(`button[data-bs-target^="#__tabbed_"][data-bs-target$="_${type}"]`).forEach((element) => (new bootstrap.Tab(element)).show());
}
document.getElementById('switch-btn-1').addEventListener("click", ()=>switchPreview(1));
document.getElementById('switch-btn-2').addEventListener("click", ()=>switchPreview(2));
document.getElementById('switch-btn-3').addEventListener("click", ()=>switchPreview(3));
</script>
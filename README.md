# [Lantana](https://lantana.wsoft.ws/)
![Screenshot](/screenshot.png)
Lantanaは、シンプルで軽量なMKDocsのテーマです。HTMLの知識がなくても簡単にサイトを作成できます。Lantanaは、WSOFT Docsのために開発されています。

Lantanaはシンプルながらも、多言語に対応しており、フリーソフトかつオープンソースプロジェクトで開発されています。

基盤であるMKDocsは、静的サイトジェネレーターで、記事の更新毎にサイトのビルドが必要ですが、一度ビルドしてしまえばに表示できるうえ移植が容易です。

各記事はマークダウン言語で記述するため、マークダウン言語を使用したことがあればすぐに使いこなすことができます。

## 使用法
LantanaはPyPIからダウンロードできます。
```shell
pip install lantana
```
Lantanaの詳しい使用方法については、[チュートリアル:作業開始](https://lantana.wsoft.ws/tutrial/getstarted/)を参照してください。

## 使用しているライブラリなど
* [docs/Credit.md](https://lantana.wsoft.ws/Credit)にまとめてあります。ご確認ください。

## 翻訳の追加および改善方法
Lantanaの翻訳を改善してくださるコントリビューターの方向けの説明です。

もし、あなたがまだ翻訳が実装されていない言語でLantanaを使用したい場合、次のコマンドを使ってテーマがサポートする言語を追加できます。

```sh
./init-locale.sh 言語名
```

また、翻訳可能なテキストがLantanaに増えるたびに、次のコマンドを実行して、翻訳作業を行う必要があります。

```sh
./update-locales.sh
```

これらのスクリプトを実行した後、`lantana/locales`ディレクトリの中に`(言語名)/LC_MESSAGES/messages.po`というファイルができています。
このファイルを使って、翻訳作業を行なってください。
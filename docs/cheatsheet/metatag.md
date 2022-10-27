---
title: メタタグ
summary: この記事では、Lantanaで使用できるメタタグの一覧を示します
author : Taiseiue
author_url : https://github.com/Taiseiueue
date : 2022-10-22
---

Lantanaでは、メタタグを使って記事にメタデータを指定できます。

### タイトル
記事のタイトルを指定します。これは、記事の一番上に表示されるほか、ページのタイトルにもなります。
```yaml
title : 記事のタイトル
```

### 概要
記事の概要です。これは、記事の一番上に表示されるほか、検索エンジンにも認識されます。
```yaml
summary : 記事の概要です
```

### 著者
記事の著者です。これは、記事のツールバーに表示されます。
```yaml
author : me
```

### 画像
記事に指定された画像です。これは、ページのサムネイルとして使用されます。
```yaml
image : thumbnail.png
```

### ナビバーを非表示
ページ左のナビバーを非表示にします。
```yaml
disable_nav : true
```

### 目次を非表示
目次を非表示にします。
```yaml
disable_tol : true
```

### ツールバーを非表示
ツールバーを非表示にします。
```yaml
disable_tools : true
```
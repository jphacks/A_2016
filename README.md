# arcana(アルカナ)

[![demo movie](https://github.com/jphacks/A_2016/blob/master/images/arcana_logo.png?raw=true)](https://youtu.be/DF2gapkrYQQ)

## 製品概要

### 背景(製品開発のきっかけ、課題等）

買い物に行った時、「あれ、家に牛乳どれくらいあったっけ？」といった問題に直面したことはありませんか？また、冷蔵庫に食材を放置しすぎて腐敗したという経験はありませんか？ arcana はそのような課題をテクノロジーで解決します。

[arcana](https://objective-ptolemy-33394b.netlify.app/) は、重さを計測することによって在庫の残量を web から確認できる IoT デバイス・ツールです。牛乳などの消耗品の下に arcana を置いておくと、その残量などをアプリで可視化できます。

### 製品説明（具体的な製品の説明）

### 特長

#### 1. 簡単に設置

<img src="https://github.com/jphacks/A_2016/blob/master/images/device.jpg?raw=true" height="200"/>

量を知りたい物の下に置くだけで、設置完了

<img src="https://github.com/jphacks/A_2016/blob/master/images/use.gif?raw=true" style="height:20em"/>

#### 2. 視覚的に量を確認可能

arcana で管理しているものが簡素なアニメーションで一覧表示されるため、簡単に残量を確認することができます。

<img src="https://github.com/jphacks/A_2016/blob/master/images/screen.png?raw=true" height="460"/>

#### 3. 期限切れ・不足時に通知

期限切れや不足した品物を放置することなく、収納を効率化できます。

<img src="https://github.com/jphacks/A_2016/blob/master/images/milk.jpg?raw=true" height="200"/>

### 解決出来ること

- 期限や在庫状況を常に把握していなくても、アプリで管理・通知することでそれらが放置されてしまう問題を解決します。
- コーンフレークやシャンプーといった日用品の他にも、大規模施設のアルコール消毒液といったこれまで可視化しずらかった物品も「一元的」に管理ができます。

### 今後の展望

- 将来的に全ての食品に RFID が搭載された際、 arcana の RFID リーダが載せられた食品を識別し、自動的に arcana に登録します。
- 残量が減った際に、arcana が自動で注文をします。

### 注力したこと（こだわり等）

- フロントエンドは、一目見た時に直感的にわかりやすい自然なデザインを心掛け、フォントやアニメーションを工夫しました。
- サーバーサイドはドメイン駆動開発を取り入れ、見通しの良い開発ができました。
- ハードウェアはスタンドアロンで動くものを期間中に作ることができました。ホームセンターで買ってきたクッキングスケールを"ハック"してインターネットにつなぎ、IoT デバイスに仕上げました。

## 開発技術

### 活用した技術

#### API・データ

-
-

#### フレームワーク・ライブラリ・モジュール

- Vue
- [FastAPI](https://fastapi.tiangolo.com/ja/)

#### デバイス

- ESP32
- [クッキングスケール](https://www.nitori-net.jp/ec/product/8975062s/)

### 独自技術

#### ハッカソンで開発した独自機能・技術

- 軽量システム: クッキングスケールを分解してセンサーの電圧特性を解析し、arcana の計測システムに組み込みました。
<!-- - 特に力を入れた部分をファイルリンク、または commit_id を記載してください。-->

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）

-
-

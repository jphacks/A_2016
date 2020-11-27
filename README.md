# arcana(アルカナ)

[![demo movie](https://github.com/jphacks/A_2016/blob/master/images/arcana_logo.png?raw=true)](https://youtu.be/DF2gapkrYQQ)

[![project overview](https://user-images.githubusercontent.com/55702777/98469528-81188680-2223-11eb-83e5-432b77cc28eb.png)
](https://youtu.be/DF2gapkrYQQ)

## 製品概要

### 背景(製品開発のきっかけ、課題等）

買い物で「あれ、家に牛乳どれくらいあったっけ？」といった問題に直面したことはありませんか？また、冷蔵庫に食材を放置しすぎて腐敗したという経験はありませんか？ arcana (アルカナ) はそのような課題をテクノロジーで解決します。

[arcana](https://ar-cana.netlify.app/) は、重さを計測することによって在庫の残量を web から確認できる IoT デバイス・ツールです。消耗品の下に arcana を置くだけで、その残量をアプリで可視化できます。

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

- `手組み回路 → プリント基板`、`市販のケース → 専用の筐体` などでの軽量化やコスト削減によって、一つ 1000 円以下での量産体制を整えることができます。
- 自然言語処理を用い、音声や会話等で在庫の確認や管理ができます。
- 将来的に全ての食品に RFID が搭載された際、 arcana の RFID リーダが載せられた食品を識別し、自動的に arcana に登録します。
- 残量が減った際に、arcana が自動で注文をします。

### 注力したこと（こだわり等）

- フロントエンドは、直感的で分かりやすい自然なデザインを心掛け、フォントやアニメーションを工夫しました。
- サーバーサイドはドメイン駆動開発を取り入れ、見通しの良い開発ができました。
- HW はホームセンターで買ってきたクッキングスケールを "ハック" してインターネットにつなぎ、IoT デバイスに仕上げました。

## 開発技術

### 活用した技術

#### API・データ

- [日本語自然言語モデル DistilBERT](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp)

#### フレームワーク・ライブラリ・モジュール

- Vue
- [FastAPI](https://fastapi.tiangolo.com/ja/)

#### デバイス

- ESP32
- [クッキングスケール](https://www.nitori-net.jp/ec/product/8975062s/)

### 独自技術

#### ハッカソンで開発した独自機能・技術

- 計量システム: クッキングスケールを分解して [センサーの電圧特性を解析](https://github.com/jphacks/A_2016/issues/27#issuecomment-722787254) し、arcana の [デバイスに組み込みました。](https://twitter.com/takapitech/status/1325098131713789952?s=20)
- [DistilBERT を日本語版 SQuAD で fine tuning することに挑戦しました。](https://github.com/jphacks/A_2016/commits/chatbot)
<!-- - 特に力を入れた部分をファイルリンク、または commit_id を記載してください。-->

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）

なし

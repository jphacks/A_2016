# A_2016 backend

## 開発

### サーバーを起動

- `docker-compose`

が必要。

```shell script
make start
```

http://localhost:8080 でサーバーが立ち上がる。

- API docs: https://hackmd.io/9vrWlNnbTpCfoyhrPTFjBQ?view
- 実際に生えているエンドポイントのdocs: http://localhost:8080/docs

### DBスキーマの変更

#### ローカル

- `app/domain/entity` 以下のスキーマ定義を編集(新しいテーブルを定義する場合は`__init__.py`にimportする必要がある。)
- DBを起動している状態で `$ make db-revision`
- `app/migrations` 以下のマイグレーションファイルを適宜編集
- `$ make db-upgrade` でDBに適用

### デプロイ

- heroku cli
- `heroku login`
- `heroku container:login`

が必要。

```shell script
make deploy
```

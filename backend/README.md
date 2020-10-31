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

### デプロイ

- heroku cli
- `heroku login`
- `heroku container:login`

が必要。

```shell script
make deploy
```

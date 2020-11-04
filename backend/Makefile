REGISTRY_URL=registry.heroku.com
HEROKU_APP=a-2016-backend
DOCKERFILE=docker/app/Dockerfile
DOCKER_COMPOSE_FILE=docker-compose.local.yml

start:
	docker-compose -f ${DOCKER_COMPOSE_FILE} up --build app postgres

deploy:
	make build && make push && make release

build:
	docker build -f ${DOCKERFILE} -t ${REGISTRY_URL}/${HEROKU_APP}/web .

push:
	docker push ${REGISTRY_URL}/${HEROKU_APP}/web

release:
	heroku container:release web -a ${HEROKU_APP}

db-revision:
	docker-compose -f ${DOCKER_COMPOSE_FILE} run db-revision

db-upgrade:
	docker-compose -f ${DOCKER_COMPOSE_FILE} run db-upgrade

# on production

start-prod:
	alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $$PORT

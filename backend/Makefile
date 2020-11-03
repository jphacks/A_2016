REGISTRY_URL=registry.heroku.com
HEROKU_APP=a-2016-backend
DOCKERFILE=docker/app/Dockerfile
DOCKER_COMPOSE_FILE=docker-compose.local.yml

start:
	docker-compose -f ${DOCKER_COMPOSE_FILE} up --build

deploy:
	make build && make push && make release

build:
	docker build -f ${DOCKERFILE} -t ${REGISTRY_URL}/${HEROKU_APP}/web .

push:
	docker push ${REGISTRY_URL}/${HEROKU_APP}/web

release:
	heroku container:release web -a ${HEROKU_APP}

revision:
	alembic revision --autogenerate

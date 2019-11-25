# makefile -f
DOCKER_COMPOSE_FILE ?= docker/docker-compose.yml
DOCKER_COMPOSE = docker-compose -f ${DOCKER_COMPOSE_FILE}

DOCKER_IMAGE = file_uploader:latest
DOCKER_APP = file_uploader

run-dev:
	${DOCKER_COMPOSE} up --build -d

stop-dev:
	${DOCKER_COMPOSE} down -v --remove-orphans

logs:
	${DOCKER_COMPOSE} logs -f file_uploader

docker-build-image:
	docker build -t ${DOCKER_IMAGE} . -f docker/Dockerfile

docker-run: docker-build-image
	docker run --name ${DOCKER_APP} -d --env-file .env -p 8080:8080 ${DOCKER_IMAGE}

docker-logs:
	docker logs -f ${DOCKER_APP}

start-gunicorn:
	gunicorn app:app -b 0.0.0.0:8080 --reload -w 1

test:
	pytest -v

# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

SHELL := /bin/bash

IMAGE_NAME := $(shell basename "$$(pwd)")-app
BUILDER := extend-builder

PYTHON_VERSION := 3.10

TEST_SAMPLE_CONTAINER_NAME := sample-event-handler-test

SOURCE_DIR := src
VENV_DIR := venv

.PHONY: venv test

venv:
	python$(PYTHON_VERSION) -m venv ${VENV_DIR} \
			&& ${VENV_DIR}/bin/pip install -r requirements-dev.txt

clean:
	cd ${SOURCE_DIR}/app/proto \
		&& rm -fv *_grpc.py *_pb2.py *_pb2.pyi *_pb2_grpc.py

proto: clean
	docker run -t --rm -u $$(id -u):$$(id -g) -v $$(pwd):/data/ -w /data rvolosatovs/protoc:4.0.0 \
			--proto_path=app/proto=${SOURCE_DIR}/app/proto \
			--python_out=${SOURCE_DIR} \
			--grpc-python_out=${SOURCE_DIR} \
			${SOURCE_DIR}/app/proto/*.proto

build: proto

run:
	docker run --rm -it \
			-u $$(id -u):$$(id -g) \
			-v $$(pwd):/data \
			-w /data \
			-e HOME=/data \
			--entrypoint /bin/sh \
			python:$(PYTHON_VERSION)-slim \
			-c 'ln -sf $$(which python) ${VENV_DIR}/bin/python-docker \
					&& PYTHONPATH=${SOURCE_DIR} GRPC_VERBOSITY=debug ${VENV_DIR}/bin/python-docker -m app'

help:
	docker run --rm -t \
			-u $$(id -u):$$(id -g) \
			-v $$(pwd):/data \
			-w /data \
			-e HOME=/data \
			--entrypoint \
			/bin/sh python:$(PYTHON_VERSION)-slim \
			-c 'ln -sf $$(which python) ${VENV_DIR}/bin/python-docker \
					&& PYTHONPATH=${SOURCE_DIR} ${VENV_DIR}/bin/python-docker -m app --help'

image:
	docker buildx build -t ${IMAGE_NAME} --load .

imagex:
	docker buildx inspect $(BUILDER) || docker buildx create --name $(BUILDER) --use 
	docker buildx build -t ${IMAGE_NAME} --platform linux/amd64 .
	docker buildx build -t ${IMAGE_NAME} --load .
	docker buildx rm --keep-state $(BUILDER)

imagex_push:
	@test -n "$(IMAGE_TAG)" || (echo "IMAGE_TAG is not set (e.g. 'v0.1.0', 'latest')"; exit 1)
	@test -n "$(REPO_URL)" || (echo "REPO_URL is not set"; exit 1)
	docker buildx inspect $(BUILDER) || docker buildx create --name $(BUILDER) --use
	docker buildx build -t ${REPO_URL}:${IMAGE_TAG} --platform linux/amd64 --push .
	docker buildx rm --keep-state $(BUILDER)

test_sample_local_hosted:
	@test -n "$(ENV_PATH)" || (echo "ENV_PATH is not set"; exit 1)
	docker build \
			--tag $(TEST_SAMPLE_CONTAINER_NAME) \
			-f test/sample/Dockerfile \
			test/sample
	docker run --rm -t \
			-u $$(id -u):$$(id -g) \
			-e HOME=/data \
			--env-file $(ENV_PATH) \
			-v $$(pwd):/data \
			-w /data \
			--name $(TEST_SAMPLE_CONTAINER_NAME) \
			$(TEST_SAMPLE_CONTAINER_NAME) \
			bash ./test/sample/test-local-hosted.sh

test_sample_accelbyte_hosted:
	@test -n "$(ENV_PATH)" || (echo "ENV_PATH is not set"; exit 1)
ifeq ($(shell uname), Linux)
	$(eval DARGS := -u $$(shell id -u) --group-add $$(shell getent group docker | cut -d ':' -f 3))
endif
	docker build \
			--tag $(TEST_SAMPLE_CONTAINER_NAME) \
			-f test/sample/Dockerfile \
			test/sample
	docker run --rm -t \
			-e HOME=/data \
			-e DOCKER_CONFIG=/tmp/.docker \
			--env-file $(ENV_PATH) \
			-v /var/run/docker.sock:/var/run/docker.sock \
			-v $$(pwd):/data \
			-w /data \
			--name $(TEST_SAMPLE_CONTAINER_NAME) \
			$(DARGS) \
			$(TEST_SAMPLE_CONTAINER_NAME) \
			bash ./test/sample/test-accelbyte-hosted.sh

test_docs_broken_links:
	@test -n "$(SDK_MD_CRAWLER_PATH)" || (echo "SDK_MD_CRAWLER_PATH is not set" ; exit 1)
	bash "$(SDK_MD_CRAWLER_PATH)/md-crawler.sh" \
			-i README.md

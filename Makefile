# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

SHELL := /bin/bash

IMAGE_NAME := $(shell basename "$$(pwd)")-app
BUILDER := extend-builder

PYTHON_VERSION := 3.10

SOURCE_DIR := src
VENV_DIR := venv

.PHONY: venv

venv:
	python$(PYTHON_VERSION) -m venv ${VENV_DIR} \
			&& ${VENV_DIR}/bin/pip install -r requirements-dev.txt

proto:
	docker run -t --rm -u $$(id -u):$$(id -g) \
		-v $$(pwd):/build \
		-w /build \
		--entrypoint /bin/bash \
		rvolosatovs/protoc:4.0.0 \
			proto.sh

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

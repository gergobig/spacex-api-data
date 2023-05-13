.PHONY: venv build check-lint lint
ENV := $(if $(env),$(env),staging)

venv:
	python -m venv .venv

build:
	python -m pip install --upgrade pip
	python -m pip install -r scripts/requirements.txt

build-test:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

build-all: build build-test

check-lint:
	sqlfluff lint .

lint:
	sqlfluff fix . -f

test:
	python -m pytest -vs

build-docker-image:
	docker build -t gergobig/spacex-api-data .

init-docker:
	docker run -p 5432:5432 gergobig/spacex-api-data
#!make
# Default values, can be overridden either on the command line of make
# or in .env
FLASK_DEBUG ?= 0

.PHONY: check-env vars run test dev

vars:
	@echo 'Environment-related vars:'
	@echo '  PYTHONPATH=${PYTHONPATH}'
	@echo '  GUNICORN_APP=${GUNICORN_APP}'
	@echo '  FLASK_APP=${FLASK_APP}'
	@echo '  FLASK_DEBUG=${FLASK_DEBUG}'

run: check-env
	gunicorn ${GUNICORN_APP}

dev: check-env
	flake8 src --max-line-length=120
	pytest --cov=. -x test
	flask run

test: check-env
	flake8 src --max-line-length=120
	pytest --cov=. test
	coverage html
	open htmlcov/index.html

venv:
	cp .env.sample .env
	echo PYTHONPATH=`pwd`/src >> .env
	pipenv --update 
	pipenv update --dev --python 3

check-env:
ifeq ($(wildcard .env),)
	@echo "Please create your .env file first, from .env.sample or by running make venv"
	@exit 1
else
include .env
export
endif

TEST ?=.
COV ?= --cov
BLACK_CONFIG ?= --exclude=venv --skip-string-normalization --line-length 100
CHECK ?= --check

.PHONY: run_tests
run_tests:
	USE_DOTENV=1 TESTING=1 pytest -p no:sugar ${TEST} ${COV}

check: flake8 black

format: CHECK=
format: black

black:
	black ${BLACK_CONFIG} ${CHECK} .

flake8:
	flake8 .
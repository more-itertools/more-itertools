TARGET_DIRS := more_itertools tests

.PHONY: all-checks
all-checks: requirements coverage check docs package

.PHONY: requirements
requirements:
	python3 -m pip install -r requirements/development.txt
	python3 -m pip install --editable .

.PHONY: check
check:
	ruff format --check ${TARGET_DIRS}
	ruff check ${TARGET_DIRS}
	stubtest more_itertools.more more_itertools.recipes

.PHONY: format
format:
	ruff format ${TARGET_DIRS}

.PHONY: coverage
coverage:
	coverage run --include="more_itertools/*.py" -m unittest
	coverage report --show-missing --fail-under=99

.PHONY: lint
lint:
	ruff format ${TARGET_DIRS}
	ruff check --fix ${TARGET_DIRS}

.PHONY: test
test:
	python3 -m unittest -v ${tests}

.PHONY: docs
docs:
	sphinx-build -W -b html docs docs/_build/html

.PHONY: package
package: requirements
	flit build --setup-py
	twine check dist/*

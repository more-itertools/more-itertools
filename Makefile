.PHONY: all-checks
all-checks: requirements coverage check docs package

.PHONY: requirements
requirements:
	python3 -m pip install -r requirements/development.txt
	python3 -m pip install --editable .

.PHONY: check
check:
	ruff check .
	ruff format --check .
	stubtest more_itertools.more more_itertools.recipes

.PHONY: format
format:
	ruff format .

.PHONY: lint
lint:
	ruff check --fix .

.PHONY: coverage
coverage:
	coverage run --include="more_itertools/*.py" -m unittest
	coverage report --show-missing --fail-under=99

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

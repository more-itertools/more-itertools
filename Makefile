.PHONY: all-checks
all-checks: requirements coverage check docs package

.PHONY: requirements
requirements:
	python -m pip install -r requirements/development.txt
	python -m pip install --editable .

.PHONY: check
check:
	ruff format --check .
	ruff check more_itertools tests
	stubtest more_itertools.more more_itertools.recipes

.PHONY: format
format:
	ruff format .

.PHONY: coverage
coverage:
	python -m pip install -r requirements/testing.txt
	coverage run --include="more_itertools/*.py" -m unittest
	coverage report --show-missing --fail-under=99

.PHONY: test
test:
	python -m unittest -v ${tests}

.PHONY: docs
docs:
	python -m pip install -r docs/requirements.txt
	sphinx-build -W -b html docs docs/_build/html

.PHONY: package
package:
	python -m pip install -r requirements/packaging.txt
	flit build --setup-py
	twine check dist/*

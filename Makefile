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
	coverage run --include="more_itertools/*.py" -m unittest
	coverage report --show-missing --fail-under=99

.PHONY: test
test:
	python -m unittest -v ${tests}

.PHONY: docs
docs:
	sphinx-build -W -b html docs docs/_build/html

.PHONY: package
package: requirements
	flit build --setup-py
	twine check dist/*

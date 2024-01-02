.PHONY: requirements
requirements:
	python3 -m pip install -r requirements/development.txt .

.PHONY: check
check:
	black --check .
	flake8 .
	stubtest more_itertools.more more_itertools.recipes

.PHONY: format
format:
	black .

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

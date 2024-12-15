.PHONY: all-checks check coverage docs format package requirements test

all-checks: requirements coverage check docs package

requirements:
	python3 -m pip install -r requirements/development.txt
	python3 -m pip install --editable .

check:
	black --check .
	flake8 more_itertools tests
	stubtest more_itertools.more more_itertools.recipes

format:
	black .

coverage:
	coverage run --include="more_itertools/*.py" -m unittest
	coverage report --show-missing --fail-under=99

test:
	python3 -m unittest -v ${tests}

docs:
	sphinx-build -W -b html docs docs/_build/html

package: requirements
	flit build --setup-py
	twine check dist/*

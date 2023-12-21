#!/bin/bash
# Reminder: Keep in sync with ./.github/workflows/python-app.yml
set -euxo pipefail
cd "$( dirname "${BASH_SOURCE[0]}" )"

test -d .venv || python3 -m venv .venv
set +x
echo "+ . .venv/bin/activate"
. .venv/bin/activate
set -x
pip install -q --upgrade pip wheel
pip install -q coverage flake8 black mypy sphinx sphinx_rtd_theme flit twine

coverage run --include="more_itertools/*.py" -m unittest
coverage report --show-missing --fail-under=99
flake8 --exclude .venv,docs .
black --check .
PYTHONPATH=. stubtest more_itertools.more more_itertools.recipes
sphinx-build -q -W -b html docs docs/_build/html
flit build --setup-py
twine check dist/*

set +x
echo -e "\e[1;32m*** Tests PASSED\e[0m, consider running: git clean -dxf dist docs"

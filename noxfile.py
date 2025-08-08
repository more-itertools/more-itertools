import sys

import nox

# default run all
nox.options.sessions = ["coverage", "check", "docs", "package"]

# select venv backend order, put uv first if available
nox.options.default_venv_backend = "uv|virtualenv"

python_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]


@nox.session
def check(session: nox.Session) -> None:
    session.install("ruff", "mypy")
    session.install("-e", ".")
    session.run("ruff", "format", "--check", ".")
    session.run("ruff", "check", "more_itertools", "tests")
    session.run("stubtest", "more_itertools.more", "more_itertools.recipes")


@nox.session
def format(session: nox.Session) -> None:
    session.install("ruff")
    session.run("ruff", "format", ".")


@nox.session
def coverage(session: nox.Session) -> None:
    session.install("coverage")
    session.install("-e", ".")
    session.run(
        "coverage",
        "run",
        "--include=more_itertools/*.py",
        "-m",
        "unittest",
        *session.posargs,
    )
    session.run("coverage", "report", "--show-missing", "--fail-under=99")


@nox.session(python=python_versions)
def coverages(session: nox.Session) -> None:
    session.notify("coverage")


@nox.session
def test(session: nox.Session) -> None:
    session.install("-e", ".")
    session.run(sys.executable, "-m", "unittest", "-v", *session.posargs)


@nox.session(python=python_versions)
def tests(session: nox.Session) -> None:
    session.notify("test")


@nox.session
def docs(session: nox.Session) -> None:
    session.install("sphinx", "furo>=2024.8")
    session.install("-e", ".")
    session.run("sphinx-build", "-W", "-b", "html", "docs", "docs/_build/html")


@nox.session
def package(session: nox.Session) -> None:
    session.install("flit", "twine")
    session.run("flit", "build", "--setup-py")
    session.run("twine", "check", "dist/*")


@nox.session(python=python_versions)
def packages(session: nox.Session) -> None:
    session.notify("package")

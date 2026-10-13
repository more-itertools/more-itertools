"""Check the source archive produced by the packaging target."""

import tarfile
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory


def check_sdist(filename):
    required = {
        'tests/__init__.py',
        'tests/test_more.py',
        'tests/test_recipes.py',
        'docs/index.rst',
        'docs/api.rst',
        'docs/conf.py',
        'docs/requirements.txt',
        'requirements/testing.txt',
        'Makefile',
        'tox.ini',
    }
    with tarfile.open(filename) as archive:
        files = {
            '/'.join(PurePosixPath(member.name).parts[1:])
            for member in archive.getmembers()
            if member.isfile()
        }
    missing = required - files
    if missing:
        raise AssertionError(f'Missing source files: {sorted(missing)}')
    generated = {
        name
        for name in files
        if name.startswith('docs/_build/')
        or '__pycache__' in PurePosixPath(name).parts
        or name.endswith('.pyc')
    }
    if generated:
        raise AssertionError(f'Generated files in archive: {sorted(generated)}')


if __name__ == '__main__':
    from flit_core.buildapi import build_sdist

    with TemporaryDirectory() as directory:
        filename = build_sdist(directory)
        check_sdist(Path(directory) / filename)

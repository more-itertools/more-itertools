"""Run this using ``fabric``.

I can't remember any of this syntax on my own.

"""
from functools import partial
from os import environ
from os.path import abspath, dirname

from fabric.api import local, cd


local = partial(local, capture=False)

ROOT = abspath(dirname(__file__))

environ['PYTHONPATH'] = (((environ['PYTHONPATH'] + ':') if
    environ.get('PYTHONPATH') else '') + ROOT)


def doc(kind='html'):
    """Build Sphinx docs.

    Requires Sphinx to be installed.

    """
    with cd('docs'):
        local('make clean %s' % kind)


def updoc():
    """Build Sphinx docs and upload them to packages.python.org.

    Requires Sphinx-PyPI-upload to be installed.

    """
    doc('html')
    local('python setup.py upload_sphinx --upload-dir=docs/_build/html')

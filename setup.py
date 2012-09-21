# Hack to prevent stupid error on exit of `python setup.py test`. (See
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html.)
try:
    import multiprocessing
except ImportError:
    pass

import sys

from setuptools import setup, find_packages


extra_setup = {}
if sys.version_info >= (3,):
    extra_setup['use_2to3'] = True


setup(
    name='more-itertools',
    version='2.1',
    description='More routines for operating on iterables, beyond itertools',
    long_description=open('README.rst').read() + '\n\n' +
                     '\n'.join(open('docs/versions.rst').read()
                                                        .splitlines()[1:]),
    author='Erik Rose',
    author_email='erikrose@grinchcentral.com',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    tests_require=['nose'],
    test_suite='nose.collector',
    url='https://github.com/erikrose/more-itertools',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries'],
    keywords=['itertools', 'iterator', 'iteration', 'filter', 'peek',
              'peekable', 'collate', 'chunk', 'chunked'],
    **extra_setup
)

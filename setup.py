# Hack to prevent stupid error on exit of `python setup.py test`. (See
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html.)
try:
    import multiprocessing
except ImportError:
    pass
from re import sub

from setuptools import setup, find_packages


setup(
    name='more-itertools',
    version='3.2.0',
    description='More routines for operating on iterables, beyond itertools',
    long_description=open('README.rst').read() + '\n\n' +
                     sub(r':func:`([a-zA-Z0-9_]+)`', r'\1', '\n'.join(open('docs/versions.rst').read()
                                                                                         .splitlines()[1:])
                                                           .replace('.. automodule:: more_itertools', '')),
    author='Erik Rose',
    author_email='erikrose@grinchcentral.com',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=['six>=1.0.0,<2.0.0'],
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries'],
    keywords=['itertools', 'iterator', 'iteration', 'filter', 'peek',
              'peekable', 'collate', 'chunk', 'chunked'],
)

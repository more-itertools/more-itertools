from re import sub

from setuptools import setup

from more_itertools import __version__


def get_long_description():
    # Fix display issues on PyPI caused by RST markup
    readme = open('README.rst').read()

    version_lines = []
    with open('docs/versions.rst') as infile:
        next(infile)
        for line in infile:
            line = line.rstrip().replace('.. automodule:: more_itertools', '')
            if line == '5.0.0':
                break
            version_lines.append(line)
    version_history = '\n'.join(version_lines)
    version_history = sub(r':func:`([a-zA-Z0-9._]+)`', r'\1', version_history)

    ret = readme + '\n\n' + version_history
    return ret


setup(
    name='more-itertools',
    version=__version__,
    description='More routines for operating on iterables, beyond itertools',
    long_description=get_long_description(),
    long_description_content_type='text/x-rst',
    author='Erik Rose',
    author_email='erikrose@grinchcentral.com',
    license='MIT',
    packages=['more_itertools'],
    package_data={'more_itertools': ['py.typed', '*.pyi']},
    python_requires='>=3.5',
    url='https://github.com/more-itertools/more-itertools',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ],
    keywords=[
        'itertools',
        'iterator',
        'iteration',
        'filter',
        'peek',
        'peekable',
        'collate',
        'chunk',
        'chunked',
    ],
)

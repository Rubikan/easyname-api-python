#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['easynameapi']

requirements = [
    'requests>=2.23.0,<3'
]

test_requirements = [
    'pytest>=3'
]

about = {}
with open(os.path.join(here, 'easynameapi', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_dir={'easynameapi': 'easynameapi'},
    python_requires=">=3.5,",
    install_requires=requirements,
    tests_require=test_requirements,
    project_urls={
        'Documentation': 'https://github.com/Rubikan/easyname-api-python/blob/master/README.md',
        'Source': 'https://github.com/Rubikan/easyname-api-python',
    },
)
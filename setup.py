#coding:utf8
from setuptools import setup, find_packages


version = '0.1.0'

name = 'chinese-slugify'
packages = find_packages(exclude=[
    'ez_setup', '*.tests', '*.tests.*', 'tests.*', 'tests'
])

description = 'chinese slugify'

url = 'https://github.com/oldcai/chinese-slugify'

author = 'oldcai'
author_email = 'oldcai@live.com'
license = 'GNU GPLv3'
install_requires = [i.strip() for i in open("requirements.txt").readlines()]
classifiers = [
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
]

test_suite = 'chinese_slugify.tests.suite'


setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=packages,
    zip_safe = False,
    install_requires=install_requires,
    test_suite=test_suite,
    #tests_require='docutils >= 0.6',
    classifiers=classifiers,
    keywords='slugify, chinese',
)

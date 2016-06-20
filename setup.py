#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
    is_setuptools = True
except ImportError:
    raise
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages           # noqa
    from setuptools.command.test import test              # noqa
    is_setuptools = False

import os
import sys
import codecs

NAME = 'django-premailer'
entrypoints = {}
extra = {}

# -*- Classifiers -*-



classes = """
    Development Status :: 4 - Beta
    Framework :: Django
    Framework :: Django :: 1.6
    Framework :: Django :: 1.7
    Framework :: Django :: 1.8
    Framework :: Django :: 1.9
    License :: OSI Approved :: MIT License
    Topic :: Communications
    Topic :: Internet :: WWW/HTTP
    Topic :: Other/Nonlisted Topic
    Topic :: Software Development :: Libraries :: Python Modules
    Intended Audience :: Developers
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Operating System :: OS Independent
    Operating System :: POSIX
    Operating System :: Microsoft :: Windows
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

# -*- Distribution Meta -*-

import re
re_meta = re.compile(r'__(\w+?)__\s*=\s*(.*)')
re_vers = re.compile(r'VERSION\s*=.*?\((.*?)\)')
re_doc = re.compile(r'^"""(.+?)"""')
rq = lambda s: s.strip("\"'")


def add_default(m):
    attr_name, attr_value = m.groups()
    return ((attr_name, rq(attr_value)), )


def add_version(m):
    v = list(map(rq, m.groups()[0].split(', ')))
    return (('VERSION', '.'.join(v[0:3]) + ''.join(v[3:])), )


def add_doc(m):
    return (('doc', m.groups()[0]), )

pats = {re_meta: add_default,
        re_vers: add_version,
        re_doc: add_doc}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'django_premailer/__init__.py')) as meta_fh:
    meta = {}
    for line in meta_fh:
        if line.strip() == '# -eof meta-':
            break
        for pattern, handler in pats.items():
            m = pattern.match(line.strip())
            if m:
                meta.update(handler(m))

# -*- Installation Requires -*-

py_version = sys.version_info


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            strip_comments(l) for l in open(
                os.path.join(here, 'requirements', *f)).readlines()
        ) if r]


def reqs(*f):
    return [req for subreq in _reqs(*f) for req in subreq]


install_requires = reqs('default.txt')

# -*- Tests Requires -*-

tests_require = reqs('test.txt')

# -*- Long Description -*-

if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', 'r', 'utf-8').read()
else:
    long_description = 'See http://pypi.python.org/pypi/django-premailer'

setup(
    name=NAME,
    version=meta['VERSION'],
    description=meta['doc'],
    author=meta['author'],
    author_email=meta['contact'],
    url=meta['homepage'],
    platforms=['any'],
    license='MIT',
    packages=find_packages(),
    package_data={'django_premailer': ['tests/templates/*.html']},
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose.collector',
    classifiers=classifiers,
    entry_points=entrypoints,
    long_description=long_description,
    keywords=['premailer', 'inline css', 'django', 'templatetag', 'html', 'lxml', 'email', 'mail', 'style'],
)

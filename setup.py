"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
from mantis import __version__
from mantis.builders.tablebuilder import MySQLTableBuilder
import os

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mantis",
    version = __version__,
    author = "Clivern",
    author_email = "hello@clivern.com",
    description="A Minimalist ORM for Python",
    license = "MIT",
    keywords = "orm,database,schema,builder",
    url = "http://clivern.github.io/mantis/",
    packages = ['mantis'],
    long_description = read('README.md'),
    classifiers = [
        'Classifier: Development Status :: 3 - Alpha',
        'Classifier: Framework :: Flask',
        'Classifier: Programming Language :: Python',
        'Classifier: Programming Language :: Python :: 2.7',
        'Classifier: Programming Language :: Python :: 3.0',
        'Classifier: Programming Language :: Python :: 3.1',
        'Classifier: Programming Language :: Python :: 3.2',
        'Classifier: Programming Language :: Python :: 3.3',
        'Classifier: Programming Language :: Python :: 3.4',
        'Classifier: Programming Language :: Python :: 3.5',
        'Classifier: Topic :: Software Development :: Libraries :: Application Frameworks',
        'Classifier: Topic :: Utilities'
    ],
)
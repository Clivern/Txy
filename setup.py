"""
Mantis - A Minimalist Database Toolkit for Python

@author: Clivern U{hello@clivern.com}
"""

from setuptools import setup
from mantis import __version__
from mantis import read_file


setup(
    name = "mantis",
    version = __version__,
    author = "Clivern",
    author_email = "hello@clivern.com",
    description="A Minimalist Database Toolkit for Python",
    license = "MIT",
    keywords = "orm,database,schema,builder",
    url = "http://clivern.github.io/mantis/",
    packages = ['mantis'],
    long_description = read_file('README.md'),
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
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
import os


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="mantis",
    version="1.0.0",
    author="Clivern",
    author_email="hello@clivern.com",
    description="A Minimalist ORM for Python",
    license="MIT",
    keywords="orm,database,schema,builder",
    url="http://clivern.github.io/mantis/",
    packages=['mantis', 'mantis.adapters', 'mantis.builders', 'mantis.exceptions', 'mantis.helpers'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Utilities'
    ],
)

# -*- coding: utf-8 -*-
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function
from .config import Config
from helpers.logger import Logger
from exceptions.exception import MantisError
from builders.querybuilder import SQLiteQueryBuilder, MySQLQueryBuilder, PostgreSQLQueryBuilder
from builders.tablebuilder import SQLiteTableBuilder, MySQLTableBuilder, PostgreSQLTableBuilder
from adapters.mysqladapter import MySQLAdapter
from adapters.postgresqladapter import PostgreSQLAdapter
from adapters.sqliteadapter import SQLiteAdapter


class Mediator(object):
    """Mediator Module"""
    pass

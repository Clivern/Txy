# -*- coding: utf-8 -*-
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""
from __future__ import print_function

class SQLiteQueryBuilder(object):
	"""SQLite Query Builder"""
	pass

class MySQLQueryBuilder(object):
	"""MySQL Query Builder"""

	# Table name
	_table = None

	# A list of commands to build the query
	_commands = []

	# End Query to run
	_query = ""

	# Temp return values used to support chaining
	_temp = []

	# Query logger
	_logger = None

	def set_logger(self, logger):
		"""Set logger"""
		self._logger = logger

	def for_table(self):
		"""Table to build the query for"""
		pass

	def get(self):
		"""Get final query"""
		pass

	def one(self):
		"""Retun only one result"""
		pass

	def many(self):
		"""Return many results"""
		pass

	def select(self):
		"""Build select clause"""
		pass

	def insert_one(self):
		"""Insert one record and return insert id"""
		pass

	def insert_many(self):
		"""Insert many records"""
		pass

	def update(self):
		"""Update existing records"""
		pass

	def where(self):
		"""Build where clause"""
		pass

	def delete(self):
		"""Delete all or some of the table records"""
		pass

	def truncate(self):
		"""Truncate all table records"""
		pass

	def group_by(self):
		"""Build group by clause"""
		pass

	def having(self):
		"""Build having clause"""
		pass

	def join(self):
		"""Join two tables"""
		pass

	def left_join(self):
		"""Left join two tables"""
		pass

	def right_join(self):
		"""Right join two tables"""
		pass

	def union(self):
		"""Union two queries together"""
		pass

	def order_by(self):
		"""Add order by clause"""
		pass

	def offset(self):
		"""Add offset"""
		pass

	def limit(self):
		"""Add Limit"""
		pass

	def _translate(self):
		"""Translate the final query"""
		pass

class PostgreSQLQueryBuilder(object):
	"""PostgreSQL Query Builder"""
	pass
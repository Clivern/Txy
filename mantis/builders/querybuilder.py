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

	def for_table(self, table):
		"""Table to build the query for"""
		self._table = table

	def get(self):
		"""Get final query"""
		# Check if logger is availabe
		if self._logger != None:
			self._logger.log(self._query)

	def one(self):
		"""Retun only one result"""
		_temp['one'] = True
		pass

	def many(self):
		"""Return many results"""
		_temp['many'] = True
		pass

	def select(self, columns = []):
		"""Build select clause"""
		_temp['select'] = columns

	def insert_one(self, record):
		"""Insert one record and return insert id"""
		_temp['insert_one'] = record

	def insert_many(self, records):
		"""Insert many records"""
		_temp['insert_many'] = records

	def update(self):
		"""Update existing records"""
		pass

	def where(self, conditions = {}):
		"""Build where clause"""
		_temp['where'] = conditions

	def delete(self):
		"""Delete all or some of the table records"""
		_temp['delete'] = True

	def truncate(self):
		"""Truncate all table records"""
		_temp['truncate'] = True

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

	def order_by(self, order_by = {}):
		"""Add order by clause"""
		_temp['order_by'] = order_by

	def offset(self, offset):
		"""Add offset"""
		_temp['offset'] = offset

	def limit(self, limit):
		"""Add Limit"""
		_temp['limit'] = limit

	def _translate(self):
		"""Translate the final query"""
		pass

class PostgreSQLQueryBuilder(object):
	"""PostgreSQL Query Builder"""
	pass
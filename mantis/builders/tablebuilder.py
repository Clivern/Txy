# -*- coding: utf-8 -*-
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""
from __future__ import print_function

class SQLiteTableBuilder(object):
	"""SQLite Table Builder"""

	# Table name
	_table = None

	# A list of columns to create
	_columns = []

	# A list of commands to execute
	_commands = []

	# End Query to run
	_query = ""

	# Temp return values used to support chaining
	_temp = None

	# Query logger
	_logger = None

	def set_logger(self, logger):
		"""Set logger"""
		self._logger = logger

	def create_table(self, table_name):
		"""Create a new table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		self._add_command({
			'type' : 'create_table',
			'table_name' : table_name
		})
		return self

	def create_table_if_not_exists(self, table_name):
		"""Create a new table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		self._add_command({
			'type' : 'create_table_if_not_exists',
			'table_name' : table_name
		})
		return self

	def alter_table(self, table_name):
		"""Alter table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		self._add_command({
			'type' : 'alter_table',
			'table_name' : table_name
		})
		return self

	def drop_table(self, table_name):
		"""Drop table from database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'drop_table',
			'table_name' : table_name
		})
		return self

	def drop_table_if_exists(self, table_name):
		"""Drop table if exists from database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'drop_table_if_exists',
			'table_name' : table_name
		})
		return self

	def rename_table(self, from_name, to_name):
		"""Rename table"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'rename_table',
			'from_table_name' : from_name,
			'to_table_name' : to_name
		})
		return self

	def text(self, column_name):
		"""Add text column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'TEXT',
		})]
		return self

	def numeric(self, column_name):
		"""Add numeric column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'NUMERIC',
		})]
		return self

	def integer(self, column_name):
		"""Add integer column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'INTEGER',
		})]
		return self

	def real(self, column_name):
		"""Add real column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'REAL',
		})]
		return self

	def blob(self, column_name):
		"""Add blob column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'BLOB',
		})]
		return self

	def null(self, column_name):
		"""Add null column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'NULL',
		})]
		return self

	def add(self):
		"""Add a new column"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['add'] = True
		return self

	def get(self):
		"""Get Query from columns and commands"""
		self._translate()
		return False if( self._query == '' ) else self._query

	def reset(self, type = ['table', 'columns', 'commands', 'query']):
		""" Reset columns and commands"""
		# Check to reset table
		if 'table' in type:
			self._table = None

		# Check to reset columns
		if 'columns' in type:
			self._columns = []

		# Check to reset commands
		if 'commands' in type:
			self._commands = []

		# Check to reset query
		if 'query' in type:
			self._query = ""

		return self

	def _add_command(self, command):
		"""Add commands storage"""
		self._commands.append(command)
		return len(self._commands) - 1

	def _add_column(self, column_name, parameters):
		"""Add columns storage"""
		self._columns.append({
			'column_name' : column_name,
			'parameters' : parameters
		})
		return len(self._columns) - 1

	def _translate(self):
		""" Translate columns and commands to Query"""
		# Check for current flow
		if (len(self._columns) > 0) and (len(self._commands) > 0):
			# Translate create table command
			self._translate_columns()

		elif (len(self._commands) > 0):
			# Translate other commands
			self._translate_commands()
		# Invalid result reached
		else:
			return False

	def _translate_columns(self):
		"""Translate table creation command"""
		for command in self._commands:

			# Check if command is create table
			if command['type'] == 'create_table':
				return self._translate_create_table(command)

			# Check if command is alter table
			elif command['type'] == 'alter_table':
				return self._translate_alter_table(command)

			# Check if logger is availabe
			if self._logger != None:
				self._logger.log(self._query)

			return True

	def _translate_commands(self):
		"""Translate custom commands"""
		self._query = ""

		# Loop through commands
		for command in self._commands:

			# Check if `drop table if exists` command
			if command['type'] == 'drop_table_if_exists':
				self._query += "DROP TABLE IF EXISTS %s" % (command['table_name'])

			# Check if `drop table` command
			elif command['type'] == 'drop_table':
				self._query += "DROP TABLE %s" % (command['table_name'])

			# Check if `rename table` command
			elif command['type'] == 'rename_table':
				self._query += "ALTER TABLE %s RENAME TO %s" % (command['from_table_name'], command['to_table_name'])

			# Invalid result reached
			else:
				return False

		# Check if logger is availabe
		if self._logger != None:
			self._logger.log(self._query)

		return True

	def _translate_create_table(self, command):
		"""Translate create table command"""

		# Build create table command
		if (command['type'] == 'create_table') and (command['table_name'] != ''):
			self._query = 'CREATE TABLE %s (\n    ' % (command['table_name'])

		# Build create table if not exists command
		elif (command['type'] == 'create_table_if_not_exists') and (command['table_name'] != ''):
			self._query = 'CREATE TABLE IF NOT EXISTS %s (\n    ' % (command['table_name'])

		# Invalid result reached
		else:
			return False

		# Internal data
		nice_column = []

		# Check if no columns set
		if len(self._columns) <= 0:
			return False

		# Loop through columns
		for column in self._columns:

			# Append column end command
			nice_column.append("%s  %s" % (column['column_name'], column['parameters']['type']))

		# check if commands empty
		if len(nice_column) <= 0:
			return False

		# append commands to the final query
		self._query += ",\n    ".join(nice_column)

		# End Query
		self._query += '\n)'

	def _translate_alter_table(self, command):
		"""Translate alter table command"""

		# Loop through columns
		nice_column = []

		for column in self._columns:

			# Append column end command
			nice_column.append('ALTER TABLE %s ADD COLUMN %s %s;' % (command['table_name'], column['column_name'], column['parameters']['type']))

		# append commands to the final query
		self._query += "\n".join(nice_column)


class MySQLTableBuilder(object):
	"""MySQL Table Builder"""

	# Table name
	_table = None

	# A list of columns to create
	_columns = []

	# A list of commands to execute
	_commands = []

	# Default engine
	_engine = "InnoDB"

	# Default charset
	_charset = "utf8"

	# Default collation
	_collation = "utf8_general_ci"

	# End Query to run
	_query = ""

	# Temp return values used to support chaining
	_temp = None

	# Query logger
	_logger = None

	def set_engine(self, engine):
		"""Set engine"""
		self._engine = engine

	def set_charset(self, charset):
		"""Set charset"""
		self._charset = charset

	def set_collation(self, collation):
		"""Set collation"""
		self._collation = collation

	def set_logger(self, logger):
		"""Set logger"""
		self._logger = logger

	def create_table(self, table_name):
		"""Create a new table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		self._add_command({
			'type' : 'create_table',
			'table_name' : table_name
		})
		return self

	def create_table_if_not_exists(self, table_name):
		"""Create a new table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		self._add_command({
			'type' : 'create_table_if_not_exists',
			'table_name' : table_name
		})
		return self

	def alter_table(self, table_name):
		"""Alter table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		self._add_command({
			'type' : 'alter_table',
			'table_name' : table_name
		})
		return self

	def drop_table(self, table_name):
		"""Drop table from database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'drop_table',
			'table_name' : table_name
		})
		return self

	def drop_table_if_exists(self, table_name):
		"""Drop table if exists from database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'drop_table_if_exists',
			'table_name' : table_name
		})
		return self

	def rename_table(self, from_name, to_name):
		"""Rename table"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'rename_table',
			'from_table_name' : from_name,
			'to_table_name' : to_name
		})
		return self

	def has_table(self, table_name):
		"""Check if table exist in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'has_table',
			'table_name' : table_name
		})
		return self

	def has_column(self, table_name, column_name):
		"""Check if column exist in table"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		self._add_command({
			'type' : 'has_column',
			'table_name' : table_name,
			'column_name' : column_name
		})
		return self

	def big_increments(self, column_name, length = 20):
		"""Add big auto increments column"""
		length = length if( length <= 20 ) else 20

		self._temp = [self._add_column(column_name, {
			'type' : 'INT(%s)' % (length),
			'length' : length,
			'null' : False,
			'auto_increment' : True
		})]
		return self

	def increments(self, column_name, length = 11):
		"""Add auto increments column"""
		length = length if( length <= 11 ) else 11

		self._temp = [self._add_column(column_name, {
			'type' : 'INT(%s)' % (length),
			'length' : length,
			'null' : False,
			'auto_increment' : True
		})]
		return self

	def big_integer(self, column_name, length = 20):
		"""Add big integer column"""
		length = length if( length <= 20 ) else 20

		self._temp = [self._add_column(column_name, {
			'type' : 'BIGINT(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def integer(self, column_name, length = 11):
		"""Add integer column"""
		length = length if( length <= 11 ) else 11

		self._temp = [self._add_column(column_name, {
			'type' : 'INT(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def medium_integer(self, column_name, length = 9):
		"""Add medium integer column"""
		length = length if( length <= 9 ) else 9

		self._temp = [self._add_column(column_name, {
			'type' : 'MEDIUMINT(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def small_integer(self, column_name, length = 6):
		"""Add small integer column"""
		length = length if( length <= 6 ) else 6

		self._temp = [self._add_column(column_name, {
			'type' : 'SMALLINT(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def tiny_integer(self, column_name, length = 4):
		"""Add tiny integer column"""
		length = length if( length <= 4 ) else 4

		self._temp = [self._add_column(column_name, {
			'type' : 'TINYINT(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def binary(self, column_name, column_length = 255):
		"""Add binary column"""
		length = length if( length <= 255 ) else 255

		self._temp = [self._add_column(column_name, {
			'type' : 'BINARY(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def boolean(self, column_name):
		"""Add boolean column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'BOOLEAN',
			'null' : False
		})]
		return self

	def string(self, column_name, column_length = 250):
		"""Add varchar column"""
		length = length if( length <= 250 ) else 250

		self._temp = [self._add_column(column_name, {
			'type' : 'VARCHAR(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def varchar(self, column_name, column_length = 250):
		"""Add varchar column"""
		length = length if( length <= 250 ) else 250

		self._temp = [self._add_column(column_name, {
			'type' : 'VARCHAR(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def char(self, column_name, column_length = 255):
		"""Add char column"""
		length = length if( length <= 255 ) else 255

		self._temp = [self._add_column(column_name, {
			'type' : 'CHAR(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def decimal(self, column_name, length, decimals):
		"""Add decimal column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'DECIMAL(%s,%s)' % (length, decimals),
			'length' : length,
			'decimals' : decimals,
			'null' : False
		})]
		return self

	def double(self, column_name, length, decimals):
		"""Add double column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'DOUBLE(%s,%s)' % (length, decimals),
			'length' : length,
			'decimals' : decimals,
			'null' : False
		})]
		return self

	def enum(self, column_name, choices=[]):
		"""Add enum column"""
		self._temp = [self._add_column(column_name, {
			'type' : "ENUM('%s')" %  "','".join(choices),
			'choices' : choices,
			'null' : False
		})]
		return self

	def float(self, column_name, length, decimals):
		"""Add float column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'FLOAT(%s,%s)' % (length, decimals),
			'length' : length,
			'decimals' : decimals,
			'null' : False
		})]
		return self

	def long_blob(self, column_name):
		"""Add long blob column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'LONGBLOB',
			'null' : False
		})]
		return self

	def medium_blob(self, column_name):
		"""Add medium blob column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'MEDIUMBLOB',
			'null' : False
		})]
		return self

	def tiny_blob(self, column_name):
		"""Add tiny blob column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'TINYBLOB',
			'null' : False
		})]
		return self

	def blob(self, column_name):
		"""Add blob column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'BLOB',
			'null' : False
		})]
		return self

	def long_text(self, column_name):
		"""Add long text column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'LONGTEXT',
			'null' : False
		})]
		return self

	def medium_text(self, column_name):
		"""Add medium text column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'MEDIUMTEXT',
			'null' : False
		})]
		return self

	def tiny_text(self, column_name):
		"""Add tiny text column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'TINYTEXT',
			'null' : False
		})]
		return self

	def text(self, column_name):
		"""Add text column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'TEXT',
			'null' : False
		})]
		return self

	def time(self, column_name):
		"""Add time column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'TIME',
			'null' : False
		})]
		return self

	def year(self, column_name, length = 4):
		"""Add year column"""
		length = length if( (length == 4) or (length == 2) ) else 4

		self._temp = [self._add_column(column_name, {
			'type' : 'YEAR(%s)' % (length),
			'length' : length,
			'null' : False
		})]
		return self

	def datetime(self, column_name):
		"""Add datetime column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'DATETIME',
			'null' : False
		})]
		return self

	def date(self, column_name):
		"""Add date column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'DATE',
			'null' : False
		})]
		return self

	def timestamp(self, column_name):
		"""Add timestamp column"""
		self._temp = [self._add_column(column_name, {
			'type' : 'TIMESTAMP',
			'null' : False
		})]
		return self

	def timestamps(self):
		"""Add 'created_at' and 'updated_at' timestamps columns"""
		self._temp = [self._add_column('created_at', {
			'type' : 'TIMESTAMP',
			'null' : False
		}), self._add_column('updated_at', {
			'type' : 'TIMESTAMP',
			'null' : False
		})]
		return self

	def nullable_timestamps(self):
		"""Add nullable 'created_at' and 'updated_at' timestamps columns"""
		self._temp = [self._add_column('created_at', {
			'type' : 'TIMESTAMP',
			'null' : True
		}), self._add_column('updated_at', {
			'type' : 'TIMESTAMP',
			'null' : True
		})]
		return self

	def nullable(self):
		"""Mark column as nullable"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['null'] = True
		return self

	def not_nullable(self):
		"""Mark column as not nullable"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['null'] = False
		return self

	def null(self):
		"""Mark column as nullable"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['null'] = True
		return self

	def not_null(self):
		"""Mark column as not nullable"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['null'] = False
		return self

	def auto_increment(self):
		"""Mark column as auto incremented"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['auto_increment'] = True
		return self

	def primary(self):
		"""Mark column as index"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['primary'] = True
		return self

	def index(self):
		"""Mark column as index"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['index'] = True
		return self

	def key(self):
		"""Mark column as index"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['index'] = True
		return self

	def default(self, default_value):
		"""Add default value to the column"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['default'] = default_value
		return self

	def add(self):
		"""Add a new column"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['add'] = True
		return self

	def modify(self):
		"""Modify column"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['modify'] = True
		return self

	def drop(self):
		"""Drop column"""
		for _temp in self._temp:
			self._columns[_temp]['parameters']['drop'] = True
		return self

	def get(self):
		"""Get Query from columns and commands"""
		self._translate()
		return False if( self._query == '' ) else self._query

	def reset(self, type = ['table', 'columns', 'commands', 'engine', 'charset', 'collation', 'query']):
		""" Reset columns and commands"""
		# Check to reset table
		if 'table' in type:
			self._table = None

		# Check to reset columns
		if 'columns' in type:
			self._columns = []

		# Check to reset commands
		if 'commands' in type:
			self._commands = []

		# Check to reset engine
		if 'engine' in type:
			self._engine = "InnoDB"

		# Check to reset charset
		if 'charset' in type:
			self._charset = "utf8"

		# Check to reset collation
		if 'collation' in type:
			self._collation = "utf8_general_ci"

		# Check to reset query
		if 'query' in type:
			self._query = ""

		return self



	def _add_command(self, command):
		"""Add commands storage"""
		self._commands.append(command)
		return len(self._commands) - 1

	def _add_column(self, column_name, parameters):
		"""Add columns storage"""
		self._columns.append({
			'column_name' : column_name,
			'parameters' : parameters
		})
		return len(self._columns) - 1

	def _translate(self):
		""" Translate columns and commands to Query"""
		# Check for current flow
		if (len(self._columns) > 0) and (len(self._commands) > 0):
			# Translate create table command
			self._translate_columns()

		elif (len(self._commands) > 0):
			# Translate other commands
			self._translate_commands()
		# Invalid result reached
		else:
			return False

	def _translate_columns(self):
		"""Translate table creation command"""
		for command in self._commands:

			# Check if command is create table
			if command['type'] == 'create_table':
				return self._translate_create_table(command)

			# Check if command is alter table
			elif command['type'] == 'alter_table':
				return self._translate_alter_table(command)

			# Check if logger is availabe
			if self._logger != None:
				self._logger.log(self._query)

			return True

	def _translate_commands(self):
		"""Translate custom commands"""
		self._query = ""

		# Loop through commands
		for command in self._commands:

			# Check if `drop table if exists` command
			if command['type'] == 'drop_table_if_exists':
				self._query += "DROP TABLE IF EXISTS `%s`" % (command['table_name'])

			# Check if `drop table` command
			elif command['type'] == 'drop_table':
				self._query += "DROP TABLE `%s`" % (command['table_name'])

			# Check if `rename table` command
			elif command['type'] == 'rename_table':
				self._query += "RENAME TABLE %s TO %s" % (command['from_table_name'], command['to_table_name'])

			# Check if `has column` command
			elif command['type'] == 'has_column':
				self._query += "SHOW COLUMNS FROM `%s` LIKE '%s'" % (command['table_name'], command['column_name'])

			# Check if `has table` command
			elif command['type'] == 'has_table':
				self._query += "SHOW TABLES LIKE '%s'" % (command['table_name'])

			# Invalid result reached
			else:
				return False

		# Check if logger is availabe
		if self._logger != None:
			self._logger.log(self._query)

		return True

	def _translate_create_table(self, command):
		"""Translate create table command"""

		# Build create table command
		if (command['type'] == 'create_table') and (command['table_name'] != ''):
			self._query = 'CREATE TABLE `%s` (\n    ' % (command['table_name'])

		# Build create table if not exists command
		elif (command['type'] == 'create_table_if_not_exists') and (command['table_name'] != ''):
			self._query = 'CREATE TABLE IF NOT EXISTS `%s` (\n    ' % (command['table_name'])

		# Invalid result reached
		else:
			return False

		# Internal data
		nice_column = []
		nice_commands = []
		auto_increment_indicator = ""

		# Check if no columns set
		if len(self._columns) <= 0:
			return False

		# Loop through columns
		for column in self._columns:
			attrs = ""
			auto_increment_indicator = ""

			# Check if column not null or null
			if ('null' in column['parameters']) and (column['parameters']['null'] == False):
				attrs += " NOT NULL"
			else:
				attrs += " NULL"

			# Check for auto increment
			if ('auto_increment' in column['parameters']) and (column['parameters']['auto_increment'] == True):
				attrs += " AUTO_INCREMENT"
				auto_increment_indicator = " AUTO_INCREMENT=1"

			# Check for default value
			if ('default' in column['parameters']) and (column['parameters']['default'] != ""):
				attrs += " DEFAULT '%s'" % (column['parameters']['default'])

			# Append column end command
			nice_column.append("`%s` %s%s" % (column['column_name'], column['parameters']['type'], attrs))

			# Check if column in primary key
			if ('primary' in column['parameters']) and (column['parameters']['primary'] == True):
				nice_commands.append("PRIMARY KEY (`%s`)" % (column['column_name']))

			# Check if column is index
			if ('index' in column['parameters']) and (column['parameters']['index'] == True):
				nice_commands.append("KEY `%s` (`%s`)" % (column['column_name']))


		# Concatenate all commands
		all_commands = nice_column + nice_commands

		# check if commands empty
		if len(all_commands) <= 0:
			return False

		# append commands to the final query
		self._query += ",\n    ".join(all_commands)

		# Set engine and charset
		if ((command['type'] == 'create_table_if_not_exists') or (command['type'] == 'create_table')) and (command['table_name'] != ''):
			self._query += '\n) ENGINE=%s DEFAULT CHARSET=%s%s;";' % (self._engine, self._charset, auto_increment_indicator)

		# Invalid result reached
		else:
			return False

	def _translate_alter_table(self, command):
		"""Translate alter table command"""

		# Build Alter table command
		if (command['type'] == 'alter_table') and (command['table_name'] != ''):
			self._query = 'ALTER TABLE %s\n' % (command['table_name'])

		# Loop through columns
		nice_column = []

		for column in self._columns:
			attrs = ""
			action_type = "ADD"

			# Check if action is add
			if ('add' in column['parameters']) and (column['parameters']['add'] == True):
				action_type = "ADD"

			# Check if action is modify
			elif ('modify' in column['parameters']) and (column['parameters']['modify'] == True):
				action_type = "MODIFY"

			# Check if action is drop
			elif ('drop' in column['parameters']) and (column['parameters']['drop'] == True):
				action_type = "DROP"

			# Set default
			else:
				action_type = "ADD"

			# Check if column not null or null
			if ('null' in column['parameters']) and (column['parameters']['null'] == False) and (action_type != 'DROP'):
				attrs += " NOT NULL"
			elif (action_type != 'DROP'):
				attrs += " NULL"

			# Check for auto increment
			if ('auto_increment' in column['parameters']) and (column['parameters']['auto_increment'] == True) and (action_type != 'DROP'):
				attrs += " AUTO_INCREMENT"

			# Check for default value
			if ('default' in column['parameters']) and (column['parameters']['default'] != "") and (action_type != 'DROP'):
				attrs += " DEFAULT '%s'" % (column['parameters']['default'])

			# Append column end command
			nice_column.append('%s %s %s%s' % (action_type, column['column_name'], column['parameters']['type'], attrs))

		# append commands to the final query
		self._query += "\n".join(nice_column)


class PostgreSQLTableBuilder(object):
	"""PostgreSQL Table Builder"""
	pass

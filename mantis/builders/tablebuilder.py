# -*- coding: utf-8 -*-
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""


class SQLiteTableBuilder(object):
	"""SQLite Table Builder"""
	pass

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
		return self._add_command({
			'type' : 'create_table',
			'table_name' : table_name
		})

	def create_table_if_not_exists(self, table_name):
		"""Create a new table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		return self._add_command({
			'type' : 'create_table_if_not_exists',
			'table_name' : table_name
		})

	def alter_table(self, table_name):
		"""Alter table in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add command
		return self._add_command({
			'type' : 'alter_table',
			'table_name' : table_name
		})

	def drop_table(self, table_name):
		"""Drop table from database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		return self._add_command({
			'type' : 'drop_table',
			'table_name' : table_name
		})

	def drop_table_if_exists(self, table_name):
		"""Drop table if exists from database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		return self._add_command({
			'type' : 'drop_table_if_exists',
			'table_name' : table_name
		})

	def rename_table(self, from_name, to_name):
		"""Rename table"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		return self._add_command({
			'type' : 'rename_table',
			'from_table_name' : from_name,
			'to_table_name' : to_name
		})

	def has_table(self, table_name):
		"""Check if table exist in database"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		return self._add_command({
			'type' : 'has_table',
			'table_name' : table_name
		})

	def has_column(self, table_name, column_name):
		"""Check if column exist in table"""
		# Reset table, columns and commands
		self.reset(['table', 'columns', 'commands', 'query'])
		# Add Command
		return self._add_command({
			'type' : 'has_column',
			'table_name' : table_name,
			'column_name' : column_name
		})

	def big_increments(self, column_name, length = 20):
		"""Add big auto increments column"""
		length = length if( length <= 20 ) else 20

		return self._add_column(column_name, {
			'type' : 'INT(%s)' % (length),
			'length' : length,
			'null' : False,
			'auto_increment' : True
		})

	def increments(self, column_name, length = 11):
		"""Add auto increments column"""
		length = length if( length <= 11 ) else 11

		return self._add_column(column_name, {
			'type' : 'INT(%s)' % (length),
			'length' : length,
			'null' : False,
			'auto_increment' : True
		})

	def big_integer(self, column_name, length = 20):
		"""Add big integer column"""
		length = length if( length <= 20 ) else 20

		return self._add_column(column_name, {
			'type' : 'BIGINT(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def integer(self, column_name, length = 11):
		"""Add integer column"""
		length = length if( length <= 11 ) else 11

		return self._add_column(column_name, {
			'type' : 'INT(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def medium_integer(self, column_name, length = 9):
		"""Add medium integer column"""
		length = length if( length <= 9 ) else 9

		return self._add_column(column_name, {
			'type' : 'MEDIUMINT(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def small_integer(self, column_name, length = 6):
		"""Add small integer column"""
		length = length if( length <= 6 ) else 6

		return self._add_column(column_name, {
			'type' : 'SMALLINT(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def tiny_integer(self, column_name, length = 4):
		"""Add tiny integer column"""
		length = length if( length <= 4 ) else 4

		return self._add_column(column_name, {
			'type' : 'TINYINT(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def binary(self, column_name, column_length = 255):
		"""Add binary column"""
		length = length if( length <= 255 ) else 255

		return self._add_column(column_name, {
			'type' : 'BINARY(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def boolean(self, column_name):
		"""Add boolean column"""
		return self._add_column(column_name, {
			'type' : 'BOOLEAN',
			'null' : False
		})

	def string(self, column_name, column_length = 250):
		"""Add varchar column"""
		length = length if( length <= 250 ) else 250

		return self._add_column(column_name, {
			'type' : 'VARCHAR(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def varchar(self, column_name, column_length = 250):
		"""Add varchar column"""
		length = length if( length <= 250 ) else 250

		return self._add_column(column_name, {
			'type' : 'VARCHAR(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def char(self, column_name, column_length = 255):
		"""Add char column"""
		length = length if( length <= 255 ) else 255

		return self._add_column(column_name, {
			'type' : 'CHAR(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def decimal(self, column_name, length, decimals):
		"""Add decimal column"""
		return self._add_column(column_name, {
			'type' : 'DECIMAL(%s,%s)' % (length, decimals),
			'length' : length,
			'decimals' : decimals,
			'null' : False
		})

	def double(self, column_name, length, decimals):
		"""Add double column"""
		return self._add_column(column_name, {
			'type' : 'DOUBLE(%s,%s)' % (length, decimals),
			'length' : length,
			'decimals' : decimals,
			'null' : False
		})

	def enum(self, column_name, choices=[]):
		"""Add enum column"""
		return self._add_column(column_name, {
			'type' : "ENUM('%s')" %  "','".join(choices),
			'choices' : choices,
			'null' : False
		})

	def float(self, column_name, length, decimals):
		"""Add float column"""
		return self._add_column(column_name, {
			'type' : 'FLOAT(%s,%s)' % (length, decimals),
			'length' : length,
			'decimals' : decimals,
			'null' : False
		})

	def long_blob(self, column_name):
		"""Add long blob column"""
		return self._add_column(column_name, {
			'type' : 'LONGBLOB',
			'null' : False
		})

	def medium_blob(self, column_name):
		"""Add medium blob column"""
		return self._add_column(column_name, {
			'type' : 'MEDIUMBLOB',
			'null' : False
		})

	def tiny_blob(self, column_name):
		"""Add tiny blob column"""
		return self._add_column(column_name, {
			'type' : 'TINYBLOB',
			'null' : False
		})

	def blob(self, column_name):
		"""Add blob column"""
		return self._add_column(column_name, {
			'type' : 'BLOB',
			'null' : False
		})

	def long_text(self, column_name):
		"""Add long text column"""
		return self._add_column(column_name, {
			'type' : 'LONGTEXT',
			'null' : False
		})

	def medium_text(self, column_name):
		"""Add medium text column"""
		return self._add_column(column_name, {
			'type' : 'MEDIUMTEXT',
			'null' : False
		})

	def tiny_text(self, column_name):
		"""Add tiny text column"""
		return self._add_column(column_name, {
			'type' : 'TINYTEXT',
			'null' : False
		})

	def text(self, column_name):
		"""Add text column"""
		return self._add_column(column_name, {
			'type' : 'TEXT',
			'null' : False
		})

	def time(self, column_name):
		"""Add time column"""
		return self._add_column(column_name, {
			'type' : 'TIME',
			'null' : False
		})

	def year(self, column_name, length = 4):
		"""Add year column"""
		length = length if( (length == 4) or (length == 2) ) else 4

		return self._add_column(column_name, {
			'type' : 'YEAR(%s)' % (length),
			'length' : length,
			'null' : False
		})

	def datetime(self, column_name):
		"""Add datetime column"""
		return self._add_column(column_name, {
			'type' : 'DATETIME',
			'null' : False
		})

	def date(self, column_name):
		"""Add date column"""
		return self._add_column(column_name, {
			'type' : 'DATE',
			'null' : False
		})

	def timestamp(self, column_name):
		"""Add timestamp column"""
		return self._add_column(column_name, {
			'type' : 'TIMESTAMP',
			'null' : False
		})

	def timestamps():
		"""Add 'created_at' and 'updated_at' timestamps columns"""
		return (self._add_column('created_at', {
			'type' : 'TIMESTAMP',
			'null' : False
		}), self._add_column('updated_at', {
			'type' : 'TIMESTAMP',
			'null' : False
		}))

	def nullable_timestamps():
		"""Add nullable 'created_at' and 'updated_at' timestamps columns"""
		return (self._add_column('created_at', {
			'type' : 'TIMESTAMP',
			'null' : True
		}), self._add_column('updated_at', {
			'type' : 'TIMESTAMP',
			'null' : True
		}))

	def nullable(self, column_key):
		"""Mark column as nullable"""
		self._columns[column_key]['null'] = True
		return column_key

	def not_nullable(self, column_key):
		"""Mark column as not nullable"""
		self._columns[column_key]['null'] = False
		return column_key

	def auto_increment(self, column_key):
		"""Mark column as auto incremented"""
		self._columns[column_key]['auto_increment'] = True
		return column_key

	def primary(self, column_key):
		"""Mark column as index"""
		self._columns[column_key]['primary'] = True
		return column_key

	def index(self, column_key):
		"""Mark column as index"""
		self._columns[column_key]['index'] = True
		return column_key

	def key(self, column_key):
		"""Mark column as index"""
		self._columns[column_key]['index'] = True
		return column_key

	def default(self, column_key, default_value):
		"""Add default value to the column"""
		self._columns[column_key]['default'] = default_value
		return column_key

	def add(self, column_key):
		"""Add a new column"""
		self._columns[column_key]['add'] = True
		return column_key

	def modify(self, column_key):
		"""Modify column"""
		self._columns[column_key]['modify'] = True
		return column_key

	def drop(self, column_key):
		"""Drop column"""
		self._columns[column_key]['drop'] = True
		return column_key

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
			if command.type == 'create_table':
				return self._translate_create_table(command)

			# Check if command is alter table
			elif command.type == 'alter_table':
				return self._translate_alter_table(command)

			# Check if logger is availabe
			if self._logger !== None:
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
		if self._logger !== None:
			self._logger.log(self._query)

		return True

	def _translate_create_table(self, command):
		"""Translate create table command"""

		# Build create table command
		if (command.type == 'create_table') and (command.table_name !== ''):
			self._query = 'CREATE TABLE `%s` (' % (command.table_name)

		# Build create table if not exists command
		elif (command.type == 'create_table_if_not_exists') and (command.table_name !== ''):
			self._query = 'CREATE TABLE IF NOT EXISTS `%s` (' % (command.table_name)

		# Invalid result reached
		else
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
			if ('null' in column['column_name']) and (column['column_name']['null'] == False):
				attrs += " NOT NULL"
			else:
				attrs += " NULL"

			# Check for auto increment
			if ('auto_increment' in column['column_name']) and (column['column_name']['auto_increment'] == True):
				attrs += " AUTO_INCREMENT"
				auto_increment_indicator = " AUTO_INCREMENT=1"

			# Check for default value
			if ('default' in column['column_name']) and (column['column_name']['default'] !== ""):
				attrs += " DEFAULT '%s'" % (column['column_name']['default'])

			# Append column end command
			nice_column.append("`%s` %s%s" % (column['column_name'], column['column_name']['type'], attrs))

			# Check if column in primary key
			if ('primary' in column['column_name']) and (column['column_name']['primary'] == True):
				nice_commands.append("PRIMARY KEY (`%s`)" % (column['column_name']))

			# Check if column is index
			if ('index' in column['column_name']) and (column['column_name']['index'] == True):
				nice_commands.append("KEY `%s` (`%s`)" % (column['column_name']))

			# Concatenate all commands
			all_commands = nice_column + nice_commands

			# check if commands empty
			if len(all_commands) <= 0:
				return False

			# append commands to the final query
			self._query += ",".join(all_commands)

		# Set engine and charset
		if ((command.type == 'create_table_if_not_exists') or (command.type == 'create_table')) and (command.table_name !== ''):
			self._query += ') ENGINE=%s DEFAULT CHARSET=%s%s;";' % (self._engine, self._charset, auto_increment_indicator)

		# Invalid result reached
		else
			return False

	def _translate_alter_table(self, command):
		"""Translate alter table command"""

		# Build Alter table command
		if (command.type == 'alter_table') and (command.table_name !== ''):
			self._query = 'ALTER TABLE %s' % (command.table_name)

		# Loop through columns
		for column in self._columns:
			attrs = ""
			action_type = "ADD"

			# Check if action is add
			if ('add' in column['column_name']) and (column['column_name']['add'] == True):
				action_type = "ADD"

			# Check if action is modify
			elif ('modify' in column['column_name']) and (column['column_name']['modify'] == True):
				action_type = "MODIFY"

			# Check if action is drop
			elif ('drop' in column['column_name']) and (column['column_name']['drop'] == True):
				action_type = "DROP"

			# Set default
			else:
				action_type = "ADD"

			# Check if column not null or null
			if ('null' in column['column_name']) and (column['column_name']['null'] == False) and (action_type !== 'DROP'):
				attrs += " NOT NULL"
			elif (action_type !== 'DROP'):
				attrs += " NULL"

			# Check for auto increment
			if ('auto_increment' in column['column_name']) and (column['column_name']['auto_increment'] == True) and (action_type !== 'DROP'):
				attrs += " AUTO_INCREMENT"

			# Check for default value
			if ('default' in column['column_name']) and (column['column_name']['default'] !== "") and (action_type !== 'DROP'):
				attrs += " DEFAULT '%s'" % (column['column_name']['default'])

			# Append column end command
			nice_column.append("%s %s %s%s" % (action_type, column['column_name'], column['column_name']['type'], attrs))

			# append commands to the final query
			self._query += "\n".join(nice_column)

class PostgreSQLTableBuilder(object):
	"""PostgreSQL Table Builder"""
	pass

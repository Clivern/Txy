"""
Mantis - A Minimalist ORM for Python

@author: Clivern U{hello@clivern.com}
"""

class SQLiteTableBuilder(object):
	pass

class MySQLTableBuilder(object):

	_table = None
	_columns = []
	_commands = []
	_engine = ""
	_charset = ""
	_collation = ""

	def set_engine(self, engine):
		self._engine = engine

	def set_charset(self, charset):
		self._charset = charset

	def set_collation(self, collation):
		self._collation = collation

	def _add_command(self, command):
		_commands.append(command)

	def _add_column(self, column_name, parameters):
		_columns.append({
			'name' : column_name,
			'parameters' : parameters
		})

	def create(self,table_name):
		self._add_command({

		})

	def drop_table(self, table_name):
		self._add_command({

		})

	def drop_table_if_exists(self, table_name):
		self._add_command({

		})

	def rename_table(self, from, to):
		self._add_command({

		})

	def has_table(self, table_name):
		self._add_command({

		})

	def has_column(self, table_name, column_name):
		self._add_command({

		})

	def big_increments(self, column_name):
		self._add_column(column_name, {
			'Type' : 'Int',
		})

	def increments(self, column_name):
		self._add_column(column_name, {

		})

	def big_integer(self, column_name):
		self._add_column(column_name, {

		})

	def integer(self, column_name):
		self._add_column(column_name, {

		})

	def small_integer(self, column_name):
		self._add_column(column_name, {

		})

	def tiny_integer(self, column_name):
		self._add_column(column_name, {

		})

	def binary(self, column_name):
		self._add_column(column_name, {

		})

	def boolean(self, column_name):
		self._add_column(column_name, {

		})

	def string(self, column_name, column_length = 250):
		self._add_column(column_name, {

		})

	def char(self, column_name, column_length = 5):
		self._add_column(column_name, {

		})

	def date(self, column_name):
		self._add_column(column_name, {

		})

	def date_time(self, column_name):
		self._add_column(column_name, {

		})

	def decimal(self, column_name, precision, scale):
		self._add_column(column_name, {

		})

	def double(self, column_name, precision, scale):
		self._add_column(column_name, {

		})

	def enum(self, column_name, choices=[]):
		self._add_column(column_name, {

		})

	def float(self, column_name):
		self._add_column(column_name, {

		})

	def long_text(self, column_name):
		self._add_column(column_name, {

		})

	def medium_integer(self, column_name):
		self._add_column(column_name, {

		})

	def medium_text(self, column_name):
		self._add_column(column_name, {

		})

	def text(self, column_name):
		self._add_column(column_name, {

		})

	def time(self, column_name):
		self._add_column(column_name, {

		})

	def timestamp(self, column_name):
		self._add_column(column_name, {

		})

	def timestamps():
		self._add_column(column_name, {

		})

	def nullable_timestamps():
		self._add_column(column_name, {

		})

	def get_query(self):
		pass

	def reset(self):
		return self
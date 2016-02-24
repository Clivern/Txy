"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function
from mantis.builders.tablebuilder import SQLiteTableBuilder
import unittest

class TestSQLiteTableBuilderMethods(unittest.TestCase):
	"""SQLite Table Builder Test Cases"""

	def test_drop_table(self):
		"""Test drop table"""
		builder = SQLiteTableBuilder()
		_drop_table = builder.drop_table('test_table').get()
		self.assertEqual(_drop_table, "DROP TABLE test_table")

	def test_drop_table_if_exists(self):
		"""Test drop table if exists"""
		builder = SQLiteTableBuilder()
		_drop_table_if_exists = builder.drop_table_if_exists('test_table').get()
		self.assertEqual(_drop_table_if_exists, "DROP TABLE IF EXISTS test_table")

	def test_rename_table(self):
		"""Test rename table"""
		builder = SQLiteTableBuilder()
		_rename_table = builder.rename_table('test_table', 'new_test_table').get()
		self.assertEqual(_rename_table, "ALTER TABLE test_table RENAME TO new_test_table")

	def test_alter_table(self):
		"""Test alter table"""
		builder = SQLiteTableBuilder()
		_alter_table = builder.alter_table('test_table').text('col1').add().get()
		self.assertEqual(_alter_table, "ALTER TABLE test_table ADD COLUMN col1 TEXT;")

		_alter_table = builder.alter_table('test_table').numeric('col1').add().get()
		self.assertEqual(_alter_table, "ALTER TABLE test_table ADD COLUMN col1 NUMERIC;")

		_alter_table = builder.alter_table('test_table').integer('col1').add().get()
		self.assertEqual(_alter_table, "ALTER TABLE test_table ADD COLUMN col1 INTEGER;")

		_alter_table = builder.alter_table('test_table').real('col1').add().get()
		self.assertEqual(_alter_table, "ALTER TABLE test_table ADD COLUMN col1 REAL;")

		_alter_table = builder.alter_table('test_table').blob('col1').add().get()
		self.assertEqual(_alter_table, "ALTER TABLE test_table ADD COLUMN col1 BLOB;")

		_alter_table = builder.alter_table('test_table').null('col1').add().get()
		self.assertEqual(_alter_table, "ALTER TABLE test_table ADD COLUMN col1 NULL;")

	def test_create_table(self):
		"""Test create table"""
		builder = SQLiteTableBuilder()
		_create_table = builder.create_table('test_table').text('col1').numeric('col2').integer('col3').real('col4').blob('col5').null('col6').get()
		self.assertEqual(_create_table, "CREATE TABLE test_table (\n    col1  TEXT,\n    col2  NUMERIC,\n    col3  INTEGER,\n    col4  REAL,\n    col5  BLOB,\n    col6  NULL\n)")


if __name__ == '__main__':
    unittest.main()
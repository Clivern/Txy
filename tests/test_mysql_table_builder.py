from __future__ import print_function
from mantis.builders.tablebuilder import MySQLTableBuilder, SQLiteTableBuilder, PostgreSQLTableBuilder
import unittest

class TestMySQLTableBuilderMethods(unittest.TestCase):

	def test_drop_table(self):
		"""Test drop table"""
		builder = MySQLTableBuilder()
		_drop_table = builder.drop_table('test_table').get()
		self.assertEqual(_drop_table, "DROP TABLE `test_table`")

	def test_drop_table_if_exists(self):
		"""Test drop table if exists"""
		builder = MySQLTableBuilder()
		_drop_table_if_exists = builder.drop_table_if_exists('test_table').get()
		self.assertEqual(_drop_table_if_exists, "DROP TABLE IF EXISTS `test_table`")

	def test_rename_table(self):
		"""Test rename table"""
		builder = MySQLTableBuilder()
		_rename_table = builder.rename_table('test_table', 'new_test_table').get()
		self.assertEqual(_rename_table, "RENAME TABLE test_table TO new_test_table")

	def test_has_table(self):
		"""Test has table"""
		builder = MySQLTableBuilder()
		_has_table = builder.has_table('test_table').get()
		self.assertEqual(_has_table, "SHOW TABLES LIKE 'test_table'")

	def test_has_column(self):
		"""Test has column"""
		builder = MySQLTableBuilder()
		_has_column = builder.has_column('test_table', 'te_id').get()
		self.assertEqual(_has_column, "SHOW COLUMNS FROM `test_table` LIKE 'te_id'")

	def test_alter_table(self):
		"""Test alter table"""
		builder = MySQLTableBuilder()
		_alter_table = builder.alter_table('test_table').big_integer('col1').nullable().default("test").add().big_integer('col2').modify().big_integer('col3').drop().get()
		self.assertEqual(_alter_table, "ALTER TABLE test_table\nADD col1 BIGINT(20) NULL DEFAULT 'test'\nMODIFY col2 BIGINT(20) NOT NULL\nDROP col3 BIGINT(20)")

	def test_create_table(self):
		"""Test create table"""
		builder = MySQLTableBuilder()
		_create_table = builder.create_table('timber_files').big_increments('fi_id').timestamps().get()
		self.assertEqual(_create_table, "CREATE TABLE `timber_files` (\n    `fi_id` INT(20) NOT NULL AUTO_INCREMENT,\n    `created_at` TIMESTAMP NOT NULL,\n    `updated_at` TIMESTAMP NOT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8;\";")


if __name__ == '__main__':
    unittest.main()
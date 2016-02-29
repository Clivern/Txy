"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function
from mantis.builders.tablebuilder import MySQLTableBuilder
import unittest

class TestMySQLTableBuilderMethods(unittest.TestCase):
	"""MySQL Table Builder Test Cases"""

	def test_drop_table(self):
		"""Test drop table"""
		builder = MySQLTableBuilder()
		_drop_table = builder.drop_table('test_table')
		self.assertEqual(_drop_table.get(), "DROP TABLE `test_table`")

	def test_drop_table_if_exists(self):
		"""Test drop table if exists"""
		builder = MySQLTableBuilder()
		_drop_table_if_exists = builder.drop_table_if_exists('test_table')
		self.assertEqual(_drop_table_if_exists.get(), "DROP TABLE IF EXISTS `test_table`")

	def test_rename_table(self):
		"""Test rename table"""
		builder = MySQLTableBuilder()
		_rename_table = builder.rename_table('test_table', 'new_test_table')
		self.assertEqual(_rename_table.get(), "RENAME TABLE test_table TO new_test_table")

	def test_has_table(self):
		"""Test has table"""
		builder = MySQLTableBuilder()
		_has_table = builder.has_table('test_table')
		self.assertEqual(_has_table.get(), "SHOW TABLES LIKE 'test_table'")

	def test_has_column(self):
		"""Test has column"""
		builder = MySQLTableBuilder()
		_has_column = builder.has_column('test_table', 'te_id')
		self.assertEqual(_has_column.get(), "SHOW COLUMNS FROM `test_table` LIKE 'te_id'")

	def test_alter_table(self):
		"""Test alter table"""
		builder = MySQLTableBuilder()
		_alter_table = builder.alter_table('test_table')
		_alter_table.big_integer('col1').nullable().default("test").add()
		_alter_table.big_integer('col2').modify().big_integer('col3').drop()
		self.assertEqual(_alter_table.get(), "ALTER TABLE test_table\nADD col1 BIGINT(20) NULL DEFAULT 'test'\nMODIFY col2 BIGINT(20) NOT NULL\nDROP col3 BIGINT(20)")

	def test_create_table(self):
		"""Test create table"""
		builder = MySQLTableBuilder()
		_create_table = builder.create_table('test_table')
		_create_table.increments('col_increments')
		_create_table.big_integer('col_big_integer')
		_create_table.integer('col_integer')
		_create_table.medium_integer('col_medium_integer')
		_create_table.small_integer('col_small_integer')
		_create_table.tiny_integer('col_tiny_integer')
		_create_table.binary('col_binary')
		_create_table.boolean('col_boolean')
		_create_table.string('col_string')
		_create_table.varchar('col_varchar').default("defValue")
		_create_table.char('col_char')
		_create_table.decimal('col_decimal', 2, 2)
		_create_table.double('col_double', 2, 2)
		_create_table.enum('col_enum', ['1', '2', '3', '4', '5'])
		_create_table.float('col_float', 2, 2)
		_create_table.long_blob('col_long_blob')
		_create_table.medium_blob('col_medium_blob')
		_create_table.tiny_blob('col_tiny_blob')
		_create_table.blob('col_blob')
		_create_table.long_text('col_long_text')
		_create_table.medium_text('col_medium_text')
		_create_table.tiny_text('col_tiny_text')
		_create_table.text('col_text')
		_create_table.time('col_time').index()
		_create_table.year('col_year').index()
		_create_table.datetime('col_datetime')
		_create_table.date('col_date')
		_create_table.timestamp('col_timestamp')
		_create_table.timestamps()

		# _create_table.nullable_timestamps()
		self.assertEqual(_create_table.get(), "CREATE TABLE `test_table` (\n    `col_increments` INT(11) NOT NULL AUTO_INCREMENT,\n    `col_big_integer` BIGINT(20) NOT NULL,\n    `col_integer` INT(11) NOT NULL,\n    `col_medium_integer` MEDIUMINT(9) NOT NULL,\n    `col_small_integer` SMALLINT(6) NOT NULL,\n    `col_tiny_integer` TINYINT(4) NOT NULL,\n    `col_binary` BINARY(255) NOT NULL,\n    `col_boolean` BOOLEAN NOT NULL,\n    `col_string` VARCHAR(250) NOT NULL,\n    `col_varchar` VARCHAR(250) NOT NULL DEFAULT 'defValue',\n    `col_char` CHAR(255) NOT NULL,\n    `col_decimal` DECIMAL(2,2) NOT NULL,\n    `col_double` DOUBLE(2,2) NOT NULL,\n    `col_enum` ENUM('1','2','3','4','5') NOT NULL,\n    `col_float` FLOAT(2,2) NOT NULL,\n    `col_long_blob` LONGBLOB NOT NULL,\n    `col_medium_blob` MEDIUMBLOB NOT NULL,\n    `col_tiny_blob` TINYBLOB NOT NULL,\n    `col_blob` BLOB NOT NULL,\n    `col_long_text` LONGTEXT NOT NULL,\n    `col_medium_text` MEDIUMTEXT NOT NULL,\n    `col_tiny_text` TINYTEXT NOT NULL,\n    `col_text` TEXT NOT NULL,\n    `col_time` TIME NOT NULL,\n    `col_year` YEAR(4) NOT NULL,\n    `col_datetime` DATETIME NOT NULL,\n    `col_date` DATE NOT NULL,\n    `col_timestamp` TIMESTAMP NOT NULL,\n    `created_at` TIMESTAMP NOT NULL,\n    `updated_at` TIMESTAMP NOT NULL,\n    PRIMARY KEY (`col_increments`),\n    KEY `col_time` (`col_time`),\n    KEY `col_year` (`col_year`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1")


if __name__ == '__main__':
    unittest.main()
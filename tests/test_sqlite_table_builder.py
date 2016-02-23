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

#: CREATE TABLE t1(
#:     t  TEXT,     -- text affinity by rule 2
#:     nu NUMERIC,  -- numeric affinity by rule 5
#:     i  INTEGER,  -- integer affinity by rule 1
#:     r  REAL,     -- real affinity by rule 4
#:     no BLOB      -- no affinity by rule 3
#: );

#: CREATE TABLE IF NOT EXISTS t1(
#:     t  TEXT,     -- text affinity by rule 2
#:     nu NUMERIC,  -- numeric affinity by rule 5
#:     i  INTEGER,  -- integer affinity by rule 1
#:     r  REAL,     -- real affinity by rule 4
#:     no BLOB      -- no affinity by rule 3
#: );

#: DROP TABLE table_name;

#: DROP TABLE IF EXISTS table_name;

#: ALTER TABLE old_table_name RENAME TO new_table_name;

#: ALTER TABLE table_name ADD COLUMN col_name TEXT;

class TestSQLiteTableBuilderMethods(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()
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
        """Get final query and log if logger available"""
        # Check if logger is availabe
        if self._logger is not None:
            self._logger.log(self._query)
        # Return query
        return self._query

    def one(self):
        """Retun only one result"""
        _temp['one'] = True
        return self

    def many(self):
        """Return many results"""
        _temp['many'] = True
        return self

    # .select(['id', 'title', 'content'])
    # .select(['id as test_id', 'title as test_title'])

    # SELECT column_name,column_name
    # FROM table_name;

    # SELECT * FROM table_name;

    # SELECT DISTINCT column_name,column_name
    # FROM table_name;

    def select(self, columns=[], distinct=False):
        """Build select clause"""
        _temp['select'] = columns
        return self

    # .insert_one({'title': 'test title', 'content': 'test content'})

    # INSERT INTO table_name
    # VALUES (value1,value2,value3,...);

    # INSERT INTO table_name (column1,column2,column3,...)
    # VALUES (value1,value2,value3,...);
    def insert_one(self, record={}):
        """Insert one  record and return insert id"""
        _temp['insert_one'] = record
        return self

    # .insert_many([{'title': 'test title', 'content': 'test content'}, {'title': 'test title', 'content': 'test content'}])
    def insert_many(self, records=[]):
        """Insert many records"""
        _temp['insert_many'] = records
        return self

    # .update({'title': 'test title', 'content': 'test content'})

    # UPDATE table_name
    # SET column1=value1,column2=value2,...
    # WHERE some_column=some_value;
    def update(self, new_record):
        """Update existing records"""
        _temp['update'] = new_record
        return self

    # .where({'and':{'id': 9, 'title': 'test'}})
    # .where({'or': {'id': 9, 'title': 'test'}})

    # SELECT * FROM Customers
    # WHERE Country='Mexico';
    # Operators: 
    #   =   Equal
    #   <>  Not equal. Note: In some versions of SQL this operator may be written as !=
    #   >   Greater than
    #   <   Less than
    #   >=  Greater than or equal
    #   <=  Less than or equal
    #   BETWEEN Between an inclusive range
    #   LIKE    Search for a pattern
    #   IN  To specify multiple possible values for a column

    # SELECT * FROM Customers
    # WHERE City='Berlin'
    # OR City='München';

    # SELECT * FROM Customers
    # WHERE City LIKE 's%';

    # SELECT column_name(s)
    # FROM table_name
    # WHERE column_name IN (value1,value2,...);

    # SELECT column_name(s)
    # FROM table_name
    # WHERE column_name BETWEEN value1 AND value2;

    # SELECT * FROM Products
    # WHERE Price BETWEEN 10 AND 20;

    # SELECT * FROM Products
    # WHERE Price NOT BETWEEN 10 AND 20;

    # SELECT * FROM Products
    # WHERE (Price BETWEEN 10 AND 20)
    # AND NOT CategoryID IN (1,2,3);

    # SELECT * FROM Products
    # WHERE ProductName BETWEEN 'C' AND 'M';

    # SELECT * FROM Products
    # WHERE ProductName BETWEEN 'C' AND 'M';
    def where(self, conditions={}):
        """Build where clause"""
        _temp['where'] = conditions
        return self

    # DELETE FROM table_name
    # WHERE some_column=some_value;

    # DELETE FROM table_name;
    # or
    # DELETE * FROM table_name;
    def delete(self):
        """Delete all or some of the table records"""
        _temp['delete'] = True
        return self

    def truncate(self):
        """Truncate all table records"""
        _temp['truncate'] = True
        return self

    def group_by(self):
        """Build group by clause"""
        return self

    def having(self):
        """Build having clause"""
        return self

    def join(self, conditions):
        """Join two tables"""
        _temp['join'] = conditions
        return self

    def left_join(self, conditions):
        """Left join two tables"""
        _temp['left_join'] = conditions
        return self

    def right_join(self, conditions):
        """Right join two tables"""
        _temp['right_join'] = conditions
        return self

    def union(self, query):
        """Union two queries together"""
        _temp['union'] = query
        return self

    # .order_by({'date': 'asc'})
    # .order_by({'date': 'desc'})

    # SELECT column_name, column_name
    # FROM table_name
    # ORDER BY column_name ASC|DESC, column_name ASC|DESC;
    def order_by(self, order_by={}):
        """Add order by clause"""
        _temp['order_by'] = order_by
        return self

    # .offset(0)
    def offset(self, offset = 0):
        """Add offset"""
        _temp['offset'] = offset
        return self

    # .limit(10)
    def limit(self, limit = 10):
        """Add Limit"""
        _temp['limit'] = limit
        return self

    def _translate(self):
        """Translate the final query"""
        pass


class PostgreSQLQueryBuilder(object):
    """PostgreSQL Query Builder"""
    pass

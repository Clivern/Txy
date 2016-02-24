# -*- coding: utf-8 -*-
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

import logging

class Logger(object):
	"""Handle ALl Mantis Logging Tasks"""

	# Holds all logger instances
	_logger = {

		# Default Logger
		'default' : None,

		# SQLite Table Builder Logger
		'sqlite_tab' : None,

		# SQLite Query Logger
		'sqlite_qui' : None,

		# MySQL Table Builder Logger
		'mysql_tab' : None,

		# MySQL Query Logger
		'mysql_qui' : None,

		# PostgreSQL Table Logger
		'postgresql_tab' : None,

		# PostgreSQL Query Logger
		'postgresql_qui' : None
	}

	def config(self, logger_type="default", log_format='@%(asctime)s - %(levelname)s: %(message)s'):
		"""Configure a Logger"""
		self._logger[logger_type] = logging.getLogger('mantis')
		self._logger[logger_type].setLevel(logging.DEBUG)
		fh = logging.FileHandler('test.log')
		fh.setLevel(logging.DEBUG)
		formatter = logging.Formatter(log_format)
		fh.setFormatter(formatter)
		self._logger[logger_type].addHandler(fh)

		return self

	def log(self, log_message, args = {}, logger_type = "default"):
		"""Log messages of info type"""
		if log_message == "":
			return self

		self._logger[logger_type].info(log_message, extra=args)
		return self

	def warning(self, log_message, args = {}, logger_type = "default"):
		"""Log messages of warning type"""
		if log_message == "":
			return self

		self._logger[logger_type].warning(log_message, extra=args)
		return self

	def error(self, log_message, args = {}, logger_type = "default"):
		"""Log messages of error type"""
		if log_message == "":
			return self

		self._logger[logger_type].error(log_message, extra=args)
		return self

	def critical(self, log_message, args = {}, logger_type = "default"):
		"""Log messages of critical type"""
		if log_message == "":
			return self

		self._logger[logger_type].critical(log_message, extra=args)
		return self

	def info(self, log_message, args = {}, logger_type = "default"):
		"""Log messages of info type"""
		if log_message == "":
			return self

		self._logger[logger_type].info(log_message, extra=args)
		return self

# -*- coding: utf-8 -*-
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""


class MantisError(Exception):
    def __init__(self, error_info):
        Exception.__init__(self, "Mantis exception was raised")
        self.error_info = error_info

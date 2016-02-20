"""
Mantis - A Minimalist Database Toolkit for Python

@author: Clivern U{hello@clivern.com}
"""

class MantisError(Exception):
    def __init__(self, error_info):
        Exception.__init__(self ,"Mantis exception was raised")
        self.error_info = error_info
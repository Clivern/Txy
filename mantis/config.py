# -*- coding: utf-8 -*-
"""
    Mantis
    ~~~~~~

    A Minimalist ORM for Python

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function


class Config(dict):
    """Mantis Config Module"""

    def __getattr__(self, name):
    	""" Get Attribute value with name """

        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            # Check for denormalized name
            name = denormalize(name)
            if name in self:
                return self.get(name)
            else:
                raise AttributeError('no attribute named %s' % name)


    def __setattr__(self, name, value):
    	""" Set Attribute name and value """

        if name in self.__dict__:
            self.__dict__[name] = value
        elif name in self:
            self[name] = value
        else:
            # Check for denormalized name
            name2 = denormalize(name)
            if name2 in self:
                self[name2] = value
            else:
                # New attribute
                self[name] = value


	def normalize(val):
	    """ Normalize a string so that it can be used as an attribute
	    to a Python object """

	    if val.find('-') != -1:
	        val = val.replace('-', '_')

	    return val


	def denormalize(val):
	    """ De-normalize a string """

	    if val.find('_') != -1:
	        val = val.replace('_', '-')

	    return val
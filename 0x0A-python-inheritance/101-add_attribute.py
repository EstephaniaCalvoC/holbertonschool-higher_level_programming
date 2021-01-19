#!/usr/bin/python3
"""Define the add_attribute function"""


def add_attribute(obj, attName, value):
    """Add a new attribute to an object if it’s possible"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attName, value)

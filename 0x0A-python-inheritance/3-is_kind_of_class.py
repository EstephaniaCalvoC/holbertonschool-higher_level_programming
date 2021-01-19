#!/usr/bin/python3
"""Define the is_same_class function"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object (obj) is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class (a_class); otherwise False.
    """
    return isinstance(obj, a_class)

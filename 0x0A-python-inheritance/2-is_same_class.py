#!/usr/bin/python3
"""Define the is_same_class function"""


def is_same_class(obj, a_class):
    """
    Return True if the object (obj) is exactly an instance
    of the specified class (a_class); otherwise False.
    """
    return type(obj) == a_class

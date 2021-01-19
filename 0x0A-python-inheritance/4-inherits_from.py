#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """
    Return True if the object (obj) is an instance
    of a class that inherited (directly or indirectly)
    from the specified class (a_class); otherwise False.
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)

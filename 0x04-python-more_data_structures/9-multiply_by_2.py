#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2"""

    nw = dict(zip(a_dictionary.keys(), [n * 2 for n in a_dictionary.values()]))
    return nw

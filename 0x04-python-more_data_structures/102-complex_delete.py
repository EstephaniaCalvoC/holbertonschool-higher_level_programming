#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary"""

    to_del = [i for i in a_dictionary if a_dictionary[i] == value]
    [a_dictionary.pop(d) for d in to_del]

    return (a_dictionary)

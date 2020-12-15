#!/usr/bin/python3
def element_at(my_list, idx):
    """Return an element from a list like in C"""

    if idx not in range(len(my_list)):
        return None

    return my_list[idx]

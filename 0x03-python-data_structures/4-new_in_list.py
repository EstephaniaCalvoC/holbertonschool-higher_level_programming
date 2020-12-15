#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a copy of a list without an element at a specific position."""

    copy = my_list.copy()

    if idx in range(len(my_list)):
        copy[idx] = element

    return (copy)

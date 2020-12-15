#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add 2 tuples"""

    value = [0, 0, 0, 0]
    # index of value list
    i = 0

    for num in tuple_a:
        if i < 2:
            value[i] = num
            i += 1

    i = 2
    for num in tuple_b:
        if i < 4:
            value[i] = num
            i += 1

    return (value[0] + value[2], value[1] + value[3])

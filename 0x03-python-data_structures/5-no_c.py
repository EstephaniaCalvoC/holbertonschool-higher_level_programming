#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string"""

    copy=""

    for i in my_string:
        if i != 'C' and i != 'c':
            copy += i;

    return (copy)

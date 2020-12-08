#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""

    upper_str = ""

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper_str += chr(ord(i) - 32)
        else:
            upper_str += i

    print(upper_str)

#!/usr/bin/python3
"""Define function print_square"""


def print_square(size):
    """
    prints a square with the character #
    Parameters:
        size (int)
    Return: None
    Raises:
        TypeError: When size is not a integer.
        ValueError: When size is less than 0.
    """

    # Validated inputs
    msg1 = "size must be an integer"
    msg2 = "size must be >= 0"

    if type(size) != int:
        raise TypeError(msg1)
    if size < 0:
        raise ValueError(msg2)

    if size == 0:
        print()
    else:
        [print("{}".format("#" * size)) for i in range(size)]

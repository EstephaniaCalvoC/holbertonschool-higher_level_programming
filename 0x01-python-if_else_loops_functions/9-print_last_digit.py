#!/usr/bin/python3


def print_last_digit(number):
    """Print and return the last digit of a number."""

    last_number = abs(number) % 10
    print(last_number, end="")

    return (last_number % 10)

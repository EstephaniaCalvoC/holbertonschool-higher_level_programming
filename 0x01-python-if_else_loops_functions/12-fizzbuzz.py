#!/usr/bin/python3


def fizzbuzz():
    """Prints the numbers from 1 to 100 separated by a space

    For multiples of three print Fizz instead of the number and for multiples\
    of five print Buzz.
    For numbers which are multiples of both three and five print FizzBuzz.
    """

    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(num), end="")

    return (None)

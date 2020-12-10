#!/usr/bin/python3

if __name__ == "__main__":
    """
    Import functions from a file and does some Maths,
    and prints the result
    """

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    operations = [['+', add], ['-', sub], ['*', mul], ['/', div]]

    for i in operations:
        operator = i[0]
        fun = i[1]
        print("{} {} {} = {}".format(a, operator, b, fun(a, b)))

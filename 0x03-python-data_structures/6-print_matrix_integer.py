#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""

    for row in matrix:
        end = ""
        for column in row:
            print("{}{:d}".format(end, column), end="")
            end = " "
        print("")

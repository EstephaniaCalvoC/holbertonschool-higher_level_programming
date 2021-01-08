#!/usr/bin/python3
"""Define function matrix_divided."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    Parameters:
        matrix (list): Contents a list with ints of floats elements.
        div (int or float): The divisor.
    Return: A matrix with the result of the division.
    Raises:
        TypeError: When matrix contains non-numbers.
        TypeError: When matrix contains rows of different sizes.
        TypeError: When div is not an int or float.
        ZeroDivisionError: When div is 0.
    """

    # Validated inputs

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    msg3 = "div must be a number"
    msg4 = "division by zero"

    if (type(matrix) != list or
            matrix == [] or
            not all(type(l) == list for l in matrix)):
        raise TypeError(msg1)

    elements = []
    [elements.extend(l) for l in matrix]
    if not all(type(num) in (int, float) for num in elements):
        raise TypeError(msg1)

    if not all(len(l) == len(matrix[0]) for l in matrix):
        raise TypeError(msg2)

    if type(div) not in (int, float):
        raise TypeError(msg3)

    if div == 0:
        raise ZeroDivisionError(msg4)

    return [[round(num / div, 2) for num in l] for l in matrix]

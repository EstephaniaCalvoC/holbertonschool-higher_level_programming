#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle():
    """
    A class to represent a square.

    Atributes:
    ----------
        __width (int): Width of Rectangle object.
        --height (int): Height of Rectangle object.
    """

    def __init__(self, width=0, height=0):
        """Construct all the necessary attributes for Rectangle object."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter and setter of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width."""

        # Validate value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter and setter of width."""
        return self.__width

    @height.setter
    def height(self, value):
        """Setter of height."""

        # Validate value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

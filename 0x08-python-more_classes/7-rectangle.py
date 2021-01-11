#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle():
    """
    A class to represent a square.

    Atributes:
    ----------
        __width (int): Width of Rectangle object.
        --height (int): Height of Rectangle object.
        number_of_instances (int): Number of instances of Rectangle class.
        print_symbol(any): Symbol for string representation.

    Methods:
        area(): Return the area of a Rectangle object.
        perimeter(): Return the perimeter of a Rectangle object.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Construct all the necessary attributes for Rectangle object."""
        type(self).number_of_instances += 1
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

    def area(self):
        """Return the area of a Rectangle object."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of a Rectangle object."""

        if 0 in (self.__width, self.__height):
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return an informal and nicely printable string
        of a Rectangle object.
        """

        if 0 in (self.__width, self.__height):
            return ("")

        str_rect = ""

        for i in range(self.__height):
            str_rect += str(self.print_symbol) * self.__width + "\n"
        return str_rect[:-1]

    def __repr__(self):
        """
        Return an official string representation of a
        Rectangle object.
        """

        rep_rect = "Rectangle(" + str(self.__width) + ", "
        rep_rect += str(self.__height) + ")"
        return rep_rect

    def __del__(self):
        """Delete a Rectangle object and print 'Bye rectangle...' mesage"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

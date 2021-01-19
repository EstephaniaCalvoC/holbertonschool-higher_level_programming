#!/usr/bin/python3
"""Define Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square object"""

    def __init__(self, size):
        """
        Inicialize a Square object

        Parametters
        -----------
            size (int): The Square's size
       """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

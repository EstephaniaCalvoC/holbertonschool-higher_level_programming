#!/usr/bin/python3
'''
Define a class square.

Classes:
square

'''


class Square():
    '''
    A class to represent a square.

    Atributes
    ---------
        __size: int
            size of the square

    Methods
    -------
        area():
            Calculate the area of a square.
    '''

    def __init__(self, size=0):
        '''
        Construct all the necessary attributes for the square object.

        Parameters
        ----------
            size: int
                size of the square, number positive for default is 0.
        '''

        # Validate size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        '''Getter and setter of size.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter of size."""

        # Validate size
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''
        Calculate the area of a square.

        Returns
        -------
        Area of a square.
        '''
        return self.__size ** 2

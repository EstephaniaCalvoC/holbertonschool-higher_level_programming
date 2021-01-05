#!/usr/bin/python3
'''
Define a class square.

Classes:
square

'''


class Square():
    '''A class to represent a square.'''

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

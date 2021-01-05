#!/usr/bin/python3
'''
Define a class square.

Classes:
square

'''


class Square():
    '''A class to represent a square.'''

    def __init__(self, size):
        '''
        Construct all the necessary attributes for the square object.

        Parameters
        ----------
            size: int or float
                size of the square
        '''

        self.__size = size

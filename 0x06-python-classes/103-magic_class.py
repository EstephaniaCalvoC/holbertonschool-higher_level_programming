#!/usr/bin/python
'''
Define a class MagicClass.
Classes:
MagicClass
'''

import math


class MagicClass():
    '''
    A class to represent a circle.

    Atributes
    ---------
        __radius: int or float
            radius of the circle.
    Methods
    -------
        area():
            Calculate the area of a circle.
        circunference():
            Calculate the perimeter of a circle.
    '''

    def __init__(self, radius=0):
        '''
        Construct all the necessary attributes for the circle object.

        Parameters
        ----------
            radius: int
                radius of the square, number positive for default is 0.
        '''

        if type(radius) is not float and type(radius) is not int:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''Calculate circle's area'''

        return math.pi * 2 ** self.__radius

    def circunference(self):
        '''Calculate circle's perimeter'''

        return math.pi * 2 * self.__radius

c = MagicClass(5)
print(c.area())
print(c.circunference())

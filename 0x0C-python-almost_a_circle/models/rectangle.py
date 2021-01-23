#!usr/bin/python3
"""Define a class Base"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inicialize a rectangle object.

        Parametters:
        ------------
            - width (int): Rectangle's width
            - height (int): Rectangle's height
            - x (int): Rectangle's x position
            - y (int): Rectangle's y position
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter or Setter for Rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter or Setter for Rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter or Setter for Rectangle's x position"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter or Setter for Rectangle's y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return Rectangle's area"""
        return self.__width * self.__height

    def display(self):
        """
        Print an informal and nicely printable string
        of a Rectangle object.
        """
        print((("#" * self.__width) + "\n") * self.__height, end="")

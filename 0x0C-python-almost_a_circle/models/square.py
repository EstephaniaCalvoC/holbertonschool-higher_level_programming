#!usr/bin/python3
"""Define a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Inicialize a square object.

        Parametters:
        ------------
            - size (int): Square's size
            - x (int): Square's x position
            - y (int): Square's y position
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Getter or Setter for Square's size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return an informal printable string of a Square object."""
        return "[Square] ({}) {}/{} - {}". format(
            self.id,
            self.x,
            self.y,
            self.width
        )

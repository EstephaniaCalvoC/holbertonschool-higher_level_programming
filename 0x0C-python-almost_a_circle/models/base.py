#!usr/bin/python3
"""Define a class Base"""


class Base:
    """
    Abstract class to support all other figures classes.

    Attributes:
    -----------
        - __nb_objects (int): The number of instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Inicialize a Base.

        Parametters:
        ------------
            - id (int): Identy of object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

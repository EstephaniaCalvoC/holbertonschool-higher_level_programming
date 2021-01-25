#!usr/bin/python3
"""Define a class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:

            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""

        f_name = cls.__name__ + ".json"

        with open(f_name, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                l_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(l_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

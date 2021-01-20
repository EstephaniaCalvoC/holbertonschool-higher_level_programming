#!/usr/bin/python3
"""Define Student class"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Inicialize a student object"""
        first_name = first_name
        last_name = last_name
        age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance"""
        return self.__dic__

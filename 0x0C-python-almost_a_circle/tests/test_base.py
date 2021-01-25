#!usr/bin/python3
"""
Define unittests for Base class
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase_init(unittest.TestCase):
    """Test cases for init function in Base class"""

    def test_id_None(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(None)
        l_id = [b1.id, b2.id, b3.id]
        self.assertEqual([1, 2, 3], l_id)

    def test_id_number(self):
        self.assertEqual(55, Base(55).id)

    def test_id_mix(self):
        b4 = Base()
        b9 = Base(9)
        b5 = Base()
        l_id = [b4.id, b9.id, b5.id]
        self.assertEqual([4, 9, 5], l_id)


class TestBase_to_json_string(unittest.TestCase):
    """Test cases for to_json_string method in Base class"""

    def test_list_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_list_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_correct_list(self):
        r1 = Rectangle(10, 7, 2, 8)
        dic1 = r1.to_dictionary()
        r2 = Rectangle(20, 14, 4, 16)
        dic2 = r2.to_dictionary()

        json_dictionary = Base.to_json_string([dic1, dic2])
        self.assertEqual(str, type(json_dictionary))

        exp = [
            {"x": 2, "width": 10, "id": r1.id, "height": 7, "y": 8},
            {"x": 4, "width": 20, "id": r2.id, "height": 14, "y": 16}
            ]
        real = eval(json_dictionary)
        self.assertEqual(exp, real) 

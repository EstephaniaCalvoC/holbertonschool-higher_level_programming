#!usr/bin/python3
"""
Define unittests for Rectanagle class
"""
import os
import unittest
from models.rectangle import Rectangle


class TestRectangle_init(unittest.TestCase):
    """Test cases for init function in Rectangle class"""

    def test_correct_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 20, 11)
        r3 = Rectangle(10, 2, 2, 1, 12)
        r4 = Rectangle(10, 2, id=13, y=1, x= 2)

        tr = (r1, r2, r3, r4)
        id1 = r1.id
        l_real = [[ar.width, ar.height, ar.x, ar.y, ar.id] for ar in tr]
        l_exp = [
            [10, 2, 0, 0, id1],
            [1, 20, 11, 0, id1 + 1],
            [10, 2, 2, 1, 12],
            [10, 2, 2, 1, 13]
        ]
        self.assertEqual(l_exp, l_real)

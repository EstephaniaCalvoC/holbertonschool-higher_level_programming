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
        r4 = Rectangle(10, 2, id=13, y=1, x=2)

        tr = (r1, r2, r3, r4)
        id1 = r1.id
        l_real = [[ar.width, ar.height, ar.x, ar.y, ar.id] for ar in tr]
        l_exp = [
            [10, 2, 0, 0, id1],
            [1, 20, 11, 0, id1 + 1],
            [10, 2, 2, 1, 12],
            [10, 2, 2, 1, 13]]
        self.assertEqual(l_exp, l_real)

    def test_Incorrect_widht(self):
        tTypeError = ((1.2, 3), ("1", 2), (True, 2), (None, 2))
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(case[0], case[1])

        tValueError = ((-1, 3), (0, 2))
        for case in tValueError:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(case[0], case[1])

    def test_Incorrect_height(self):
        tTypeError = ((3, 1.2), (2, "1"), (2, True), (2, None))
        msgTypeError = "height must be an integer"
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, msgTypeError):
                Rectangle(case[0], case[1])

        tValueError = ((3, -1), (2, 0))
        for case in tValueError:
            with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(case[0], case[1])

    def test_Incorrect_x(self):
        tTypeError = ((1, 3, 1.2), (1, 2, "1"), (1, 2, True), (1, 2, None))
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(case[0], case[1], case[2])

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_Incorrect_y(self):
        tTypeError = (
            (1, 2, 3, 1.2),
            (1, 2, 3, "1"),
            (1, 2, 3, True),
            (1, 2, 3, None))
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(case[0], case[1], case[2], case[3])

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, y=-3)

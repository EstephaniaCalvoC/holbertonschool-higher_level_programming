#!/usr/bin/python3
"""Define class MyInt"""


class MyInt(int):
    """
    An inherited int class.

    """
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

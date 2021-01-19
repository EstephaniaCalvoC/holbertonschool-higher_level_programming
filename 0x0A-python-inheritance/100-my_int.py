#!/usr/bin/python3
"""Define class MyInt"""


class MyInt(int):
    """
    An inherited int class.

    """
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return super().__eq__(value)

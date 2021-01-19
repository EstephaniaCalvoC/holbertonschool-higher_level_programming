#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):
    """
    An inherited list class.

    Methods
    -------
        print_sorted(): Print a sorted list.
    """

    def print_sorted(self):
        """Print a sorted list."""
        return(sorted(self))

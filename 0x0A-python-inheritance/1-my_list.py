#!/usr/bin/python3
"""This module inherits from the list class"""


class MyList(list):
    """
    MyList class, inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))

#!/usr/bin/python3
"""
A module that defines a class MyList that inherits from list.
"""

class MyList(list):
    """
    A class that inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))


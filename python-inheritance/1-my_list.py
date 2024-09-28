#!/usr/bin/python3
"""
Module for MyList which inherits from list.
This class provides a method to print the list in sorted order.
"""

class MyList(list):
    """
    MyList class that inherits from the built-in list class.
    It allows printing the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        The list is expected to contain integers only.
        """
        print(sorted(self))

    def append(self, item):
        """
        Appends an item to the list.
        The item must be an integer, raises TypeError otherwise.
        """
        if not isinstance(item, int):
            raise TypeError("Item must be an integer")
        super().append(item)


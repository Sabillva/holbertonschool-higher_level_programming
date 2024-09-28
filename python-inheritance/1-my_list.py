#!/usr/bin/python3
"""
Module for MyList which inherits from list.
"""
  class MyList(list):
    """
    elements of the list int type
    return my list and sorted list
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        print(sorted(self))

    def append(self, item):
        """
        Appends an item to the list.
        """
        if not isinstance(item, int):
            raise TypeError("Item must be an integer")
        super().append(item)

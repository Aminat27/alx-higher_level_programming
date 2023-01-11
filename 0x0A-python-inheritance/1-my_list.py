#!/usr/bin/python3
"""My class Mylist"""


class MyList(list):
    """Sort printing for the built-in class"""

    def print_sorted(self):
        """print sorted list in ascending order"""
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)

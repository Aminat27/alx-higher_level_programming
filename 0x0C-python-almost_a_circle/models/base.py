#!/usr/bin/python3
"""Module: base"""


class Base:
    """Class: base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assign the public instance attribute id
        Args:
           id(int): integer value to manage id in this project
        Return:
           Always nothing.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
"""
This module is composed by a function prints a message
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints "My name is <first name> <last name>"
    Args:
        first_name: first name
        last_name: last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

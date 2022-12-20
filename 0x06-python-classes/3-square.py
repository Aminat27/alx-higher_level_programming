#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if type(size) is int:
            if size < 0:
                raise TypeError ('size must be >= 0')
            else:
                self.__size = size
        else:
            	raise ValueError ('size must be an integer')
    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

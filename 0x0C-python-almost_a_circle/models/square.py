#!/usr/bin/python3
"""Defines a square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialized the square
        Args:
           size: side's size of the square
           x: Position on x axis.
           y: Position on y axis.
        Return:
           Always nothing.
        """
        super().__init__(size, size, y, x, id)

    def __str__(self):
        """Method that returns a string"""
        return ("[Square ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height))

    @property
    def size(self):
        """Getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size
        Args:
           value: Size to assign
        Return:
           Always Nothing

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that update arguments for square object
        Args:
           *args: list of arguments.
           **kwargs: Dictionary of the arguments.
        Return:
           Always nothing
        """
        dict_order = ['id', 'size', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for keys in dict_order:
                try:
                    setattr(self, keys, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for keys in dict_order:
                try:
                    setattr(self, keys, kwargs[keys])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method that returns the dictionary
           representation of a Square.
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
        dict_attr = {}
        for key in dict_order:
            dict_attr[key] = getattr(self, key)
        return dict_attr


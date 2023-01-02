#!/usr/bin/python3
""" A rectangle class"""


class Rectangle:
    """ A rectangle.
     Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ prints the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ prints the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return the printable representation of the Rectangle
        using # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for a in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for b in range(self.__width)]
            if a != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return the string represantation of a Rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

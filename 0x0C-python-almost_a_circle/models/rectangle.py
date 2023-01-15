#!/usr/bin/python3
"""Module rectangle"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that init values for a rectangle object
        Args:
           width:size of the width
           height: size of the height
           x: Variable x
           y:  Variable y
        Return:
           Always nothing
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter of width
    @property
    def width(self):
        """Getter the size of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the size of width
        Args:
           value: Size to assign to the width
        Return:
           Always Nothing
        """
        self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter the size of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the size of height
        Args:
           value: Size to assign to the height
        Return:
           Always Nothing
        """
        self.__height = value

    # Getter and setter of x
    @property
    def x(self):
        """Getter the size of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter the size of x
        Args:
           value: Size to assign to the x
        Return:
           Always Nothing
        """
        self.__x = value

    # Getter and setter of y
    @property
    def y(self):
        """Getter of y variable
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter the size of y
        Args:
           value: Size to assign to the y
        Return:
           Always Nothing
        """
        self.__y = value

#!/usr/bin/python3
"""A module for working with rectangles.
"""


class Rectangle:
    """Represents a 2D Polygon with 4 perpendicular sides.
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of this Rectangle.
        Returns:
            int: The width of this rectangle.
        """
        return self.__width

    @property
    def height(self):
        """retrieves the height of this Rectangle.
        Returns:
            int: The height of this Rectangle.
        """
        return slf.__height

    @width.setter
    def width(self, value):
        """Updates the width of this Rectangle.
        Args:
            value (int): The new width of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """updates the height of this rectangle.
        Args:
            value (int): The new height of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must ben an integer')
        elif value < 0:
            raise ValueError('height must >= 0')
        else:
            self.__height = value

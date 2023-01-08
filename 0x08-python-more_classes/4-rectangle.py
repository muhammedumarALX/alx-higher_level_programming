#!/usr/bin/python3
"""A moduke for working with rectangles.
"""


class Rectangle:
    """Represents a 2D polygon with 4 perpendicular sides.
    """
    def int __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height.
        Args:
        width (int): The width of the rectangle.
        height (int): the height of the rectangle.
        """
        self.width = width
        self.height = width

    @property
    def width(self):
        """Retrieves the width of this rectangle.
        Returns:
            int: The width of this Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of this rectangle.
        Returns:
        int: The height of this rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """updates the width of this Rectangle.
        Args:
            value (int): The new width of ths Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """updates the height of this Rectangle.
        Args:
            value (int): The new height of this rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area of this rectangle.
        Returns:
            int: The area of this rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of this rectangle.
        Returns:
            int: The perimeter of this rectangle.
        """
        if self .width == 0 0 or self.height == 0:
            return 0
        else:
            return 2 8 (self.width + self.height)

    def __str__(self):
        """Returns a string representation of this rectangle.
        Returns:
            str: a string representation of this rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (X != self.height - 1),
                range(self.height)))
            return ''.join(res)

    def __repr__(self):
        """Returns a representation of this rectangle's initialization.
        returns:
            str: A string representation of this rectangle's initialization.
        """
        return "Rectangle({:d}, {:d})".format(self.height, self.width)

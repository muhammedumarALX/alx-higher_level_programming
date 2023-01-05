#!/usr/bin/python3
"""A module for working with rectangles
"""


class Rectangle:
    """Represents a 2D polygon with 4 perpendicular sides.
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a gib=ven width and height.
        Args:
            width (int): the width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of this rectangle.
        Returns:
            int: the width of this rectangle.
        """
        return self.__width

    @property
    def height(self):
        """retrieves the height of this rectangle.
        Returns:
            int: the height of this rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Updates the width of this rectangle.
        Args:
            value (int): The new width of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """computes the area of this rectangle.
        Returns:
            int: The area of this rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of this Rectangle.
        Returns:
        int: the primeter of this rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of this rectangle.
        Returns:
        str: A string representation of this Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)

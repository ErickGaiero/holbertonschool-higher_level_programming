#!/usr/bin/python3

"""Define a rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height
        
    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width
    
    @height.setter
    def height(self, height):
        """Set height of rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        
    @width.setter
    def width(self, width):
        """"Set width of rectangle"""""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        

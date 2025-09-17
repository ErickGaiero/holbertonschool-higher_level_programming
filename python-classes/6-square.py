#!/usr/bin/python3

"""Print a square or calulate idkwn"""


class Square:
    """Class to print a square"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)

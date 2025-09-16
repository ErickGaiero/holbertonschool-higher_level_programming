#!/usr/bin/python3

"""Print a square or calulate idkwn"""


class Square:
    """Class to print a square"""
    def __init__(self, size=0):
        """Initialize size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size

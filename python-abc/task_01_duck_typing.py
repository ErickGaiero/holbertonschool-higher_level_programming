#!/usr/bin/env python3
"""A"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape."""

    @abstractmethod
    def area(self):
        """Area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter."""
        pass


class Circle(Shape):
    """Circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area + perimeter."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

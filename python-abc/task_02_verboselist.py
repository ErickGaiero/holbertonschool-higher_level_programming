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
        """Make circle, handle negative radius."""
        self.radius = abs(radius)

    def area(self):
        """pi * r^2"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """2 * pi * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle."""

    def __init__(self, width, height):
        """Make rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """w * h"""
        return self.width * self.height

    def perimeter(self):
        """2*(w+h)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area + perimeter."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


class VerboseList(list):
    """List with notifications."""

    def append(self, item):
        """Add item and notify."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and notify."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item and notify."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and notify."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

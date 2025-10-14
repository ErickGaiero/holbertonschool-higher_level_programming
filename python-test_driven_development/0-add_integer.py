#!/usr/bin/python3

"""Exercise 0"""


def add_integer(a, b=98):
    
    """Adds two numbers after casting floats to integers."""

    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        if a != a or abs(a) == float('inf'):
            raise OverflowError("cannot convert float NaN or infinity to integer")
    if isinstance(b, float):
        if b != b or abs(b) == float('inf'):
            raise OverflowError("cannot convert float NaN or infinity to integer")

    return int(a) + int(b)

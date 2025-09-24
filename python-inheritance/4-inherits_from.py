#!/usr/bin/python3

"""Returns True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Returns true or false"""
    return isinstance(obj, a_class) and type(obj) is not a_class

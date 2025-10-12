#!/usr/bin/python3

"""Exercise 1"""


def safe_print_integer(value):
    """Try to print the value as an integer"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

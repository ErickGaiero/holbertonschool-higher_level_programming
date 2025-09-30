#!/usr/bin/python3

def read_file(filename=""):
    """Read a file in UTF8"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

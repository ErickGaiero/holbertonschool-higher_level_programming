#!/usr/bin/python3

"""Divides all elements of a matrix by a number."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""

    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            result = round(num / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
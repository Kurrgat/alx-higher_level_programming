#!/usr/bin/python3
"""
Module: 2-matrix_divided

This module defines a function that divides all elements of a matrix.

"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: The resulting matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if each row of the matrix does not have the same size, or
                   if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        row = list(map(lambda x: x**2, row))
        square_matrix.append(row)
    return square_matrix

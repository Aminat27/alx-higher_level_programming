#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []

    if len(matrix) == 0:
        return n_matrix

    n_matrix = [[i ** 2 for i in j] for j in matrix]
    return n_matrix

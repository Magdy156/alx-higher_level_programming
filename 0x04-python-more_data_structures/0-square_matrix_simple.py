#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = matrix.copy()

    for i in range(len(copy)):
        copy[i] = list(map(lambda j: j * j, matrix[i]))

    return (copy)

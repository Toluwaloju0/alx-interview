#!/usr/bin/python3
"""A module to rotate a 2-D matrix"""


def rotate_2d_matrix(matrix: list[list]) -> None:
    """A list of list to be rotated"""

    if matrix is None:
        return None
    length = len(matrix)

    # create a new matrix and set
    new_mat = [[0] * length for _ in range(length)]
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            new_mat[b][length - 1] = matrix[a][b]
        length -= 1

    for a in range(len(matrix)):
        for b in range(len(matrix)):
            matrix[a][b] = new_mat[a][b]

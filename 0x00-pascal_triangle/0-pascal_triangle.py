#!/usr/bin/python3
"""A module to get the pascal triangle"""


def pascal_triangle(n):
    """A function for the pascal triangle
    Args:
        n (int): the number of rows in the triangle
    returns:
        list: a list of lists of integers
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

    return triangle

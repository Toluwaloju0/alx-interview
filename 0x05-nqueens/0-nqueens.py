#!/usr/bin/python3
"""A module to place non-attacking queens in a board"""

import sys


def check(list_list, right, left, number):
    """To check the list_list if pos_list can be placed inside"""

    # check the horizontal and vertical lines for any appearance of number
    a = 0
    while a < number:
        if [right, a] in list_list or [a, left] in list_list:
            return False
        a += 1
    # check the diagonal lines going up left for any appearance of number
    a, b = right, left
    while a >= 0 and b >= 0:
        if [a, b] in list_list:
            return False
        a, b = a - 1, b - 1
    # check the diagonal lines going down right for any appearance of number
    a, b = right, left
    while a < number and b < number:
        if [a, b] in list_list:
            return False
        a, b = a + 1, b + 1
    # check the diagonal lines going down left for any appearance of number
    a, b = right, left
    while a >= 0 and b < number:
        if [a, b] in list_list:
            return False
        a, b = a - 1, b + 1
    # check the diagonal lines going down right for any appearance of number
    a, b = right, left
    while a < number and b >= 0:
        if [a, b] in list_list:
            return False
        a, b = a + 1, b - 1
    return True


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
            if number < 4:
                print("N must be at least 4")
                exit(1)
            for soln in range(1, (number - 1)):
                new_list = [[0, soln]]
                # Comment here
                for right in range(number):
                    for left in range(number):
                        if check(new_list, right, left, number):
                            new_list.append([right, left])
                print(new_list)

        except ValueError:
            print('N must be a number')
            exit(1)
    else:
        print('Usage: nqueens N')
        exit(1)

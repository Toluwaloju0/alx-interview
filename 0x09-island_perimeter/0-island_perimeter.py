#!/usr/bin/python3
"""A module to calculate the perimeter of an island"""


def island_perimeter(grid):
    """A function to calculate the perimeter of an island
    land is represented by 1 in the grid"""

    # Iterate through the grid to get lands
    perimeter = 0
    try:
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                # check the sides of the grid
                if (a == 0 or a == len(grid) - 1) and grid[a][b] == 1:
                    print('a == {}'.format(a))
                    perimeter += 1
                if (b == 0 or b == len(grid[a]) - 1) and grid[a][b] == 1:
                    print('b == {}'.format(b))
                    perimeter += 1
                # If land check if it is not surrounded by water
                if grid[a][b] == 1:
                    if grid[a + 1][b] == 0:
                        perimeter += 1
                    if grid[a - 1][b] == 0:
                        perimeter += 1
                    if grid[a][b + 1] == 0:
                        perimeter += 1
                    if grid[a][b - 1] == 0:
                        perimeter += 1
    except IndexError:
        pass
    return perimeter

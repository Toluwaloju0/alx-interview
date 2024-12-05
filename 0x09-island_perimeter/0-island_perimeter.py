#!/usr/bin/python3
"""A module to calculate the perimeter of an island"""


def island_perimeter(grid):
    """A function to calculate the perimeter of an island
    land is represented by 1 in the grid"""

    # if len(grid) == 0:
    #     return 0
    # Iterate through the grid to get lands
    perimeter = 0
    for a in range(1, len(grid) - 1):
        for b in range(1, len(grid) - 1):
            if grid[a][b] == 0:
                continue
            # Check the surrounding fo water
            if grid[a][b - 1] == 0:  # check left
                perimeter += 1
            if grid[a][b + 1] == 0:  # check right
                perimeter += 1
            if grid[a - 1][b] == 0:  # check bottom
                perimeter += 1
            if grid[a + 1][b] == 0:  # check top
                perimeter += 1
    return perimeter

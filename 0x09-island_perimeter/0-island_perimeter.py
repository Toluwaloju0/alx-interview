#!/usr/bin/python3
"""A module to calculate the perimeter of an island"""

def island_perimeter(grid):
    """A function to calculate the perimeter of an island
    land is represented by 1 in the grid"""

    if len(grid) == 0:
        return 0
    # Iterate through the grid to get lands
    try:
        perimeter = 0
        for a in range(len(grid)):
            for b in range(len(grid)):
                if grid[a][b] == 0:
                    continue
                # Check the surrounding fo water
                if grid[a][b - 1] == 0:
                    perimeter += 1
                if grid[a][b + 1] == 0:
                    perimeter += 1
                if grid[a - 1][b] == 0:
                    perimeter += 1
                if grid[a + 1][b] == 0:
                    perimeter += 1
        return perimeter
    except IndexError:
        pass
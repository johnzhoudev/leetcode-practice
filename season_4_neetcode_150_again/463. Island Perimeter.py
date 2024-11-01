

def solve(grid):

    perimeter = 0

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def inRange(x, y):
        return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 1): # land, count sides
                for dx, dy in directions:
                    if (not inRange(i + dx, j + dy) or grid[i + dx][j + dy] == 0):
                        perimeter += 1
    
    return perimeter



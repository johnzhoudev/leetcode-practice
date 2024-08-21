"""

695. Max Area of Island


Idea: just dfs, keep track of size - return size thru dfs
O(mn) time

Try iterative method?

"""

def solve(grid):

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def is_out_of_bounds(i, j):
        return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

    def dfs(i, j):
        if is_out_of_bounds(i, j) or grid[i][j] == 0:
            return 0
        else: # grid[i][j] == 1
            grid[i][j] = 0
            total = 1
            for dx, dy in directions:
                total += dfs(i + dx, j + dy)
            return total
    
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            largest = max(dfs(i, j), largest)
    
    return largest






"""

200. Number of Islands

dfs from each point, maintain visited

O(n) time to visit each point

"""

def solve(grid):

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    num_islands = 0

    def is_out_of_bounds(i, j):
        return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

    def dfs(i, j):
        if is_out_of_bounds(i, j):
            return
        
        if grid[i][j] == '0':
            return # do nothing
        
        if grid[i][j] == '1':
            grid[i][j] = '0'
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(i, j)
    
    return num_islands
        
solve([["1"],["1"]])



"""


2658. Maximum Number of Fish in a Grid

just dfs, O(n)


"""

def solve(grid):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    def isOutOfBounds(x, y):
        return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])

    # returns fish
    def dfs(x, y):
        nonlocal visited
        if grid[x][y] == 0: return 0 # can't go past land
        visited.add((x, y))
        amt = grid[x][y]
        for dx, dy in directions:
            if not isOutOfBounds(x + dx, y + dy) and (x + dx, y + dy) not in visited:
                amt += dfs(x + dx, y + dy)
        
        return amt
    
    best = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                best = max(dfs(r, c), best)
    return best


        

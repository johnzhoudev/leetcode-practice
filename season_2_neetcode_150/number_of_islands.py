# Results:
# Runtime: 352ms 72.88%
# Memory Usage: 16.4MB 82.35%

"""

https://leetcode.com/problems/number-of-islands/

ideas:
- 1's are islands
- 0's are not
- Do a dfs on each 1, and mark to 0.

Tactic: Do dfs to clear, mark 1 as 0
"""

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(grid, startx, starty):
    # do a dfs
    # as you visit nodes, mark as 0
    stack = [(startx, starty)]

    if (len(grid) == 0):
        return

    while stack:
        x, y = stack.pop()

        # break early if 0 or out of bounds
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            continue
        elif (grid[x][y] == "0"):
            continue
        else:
            assert(grid[x][y] == "1")
            # mark as visited, 0
            grid[x][y] = 0

        # add 4 directions
        for deltaX, deltaY in directions:
            stack.push((x + deltaX, y + deltaY))

def solve(grid):
    numIslands = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == "1"):
                numIslands += 1
                dfs(grid, i, j)

    return numIslands
            

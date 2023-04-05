"""

https://leetcode.com/problems/max-area-of-island/

mxn matrix, 01
- return max area of an island


Idea:
- dfs at each island, like number of islands. Record max size
Time: O(mxn)
Space: O(n*m) worst case

Can do iterative

Tactic: Implement DFS iterative / recursive, returns area of island. Do search from each start, marking 0 if seen. 

"""

def solveRecursive(grid):
    maxArea = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        else:
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(grid, r+dr, c+dc)
            return area
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            maxArea = max(dfs(grid, row, col), maxArea)
    return maxArea
            


def solve(grid):
    maxArea = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(grid, row, col):
        nonlocal directions
        state = [(row, col)]
        totalArea = 0
        while state:
            r, c = state.pop()
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue
            if grid[r][c] == 0:
                continue
            else:
                totalArea += 1
                grid[r][c] = 0
                for drow, dcol in directions:
                    state.append((r + drow, c + dcol))
        return totalArea
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            maxArea = max(dfs(grid, row, col), maxArea)
    
    return maxArea
            


x = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
for row in x:
    print(row)

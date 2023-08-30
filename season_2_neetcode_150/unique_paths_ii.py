"""

https://leetcode.com/problems/unique-paths-ii/

- robot in top left, go bottom right, only move down and right
- obstacle = 1, space = 0
- return num unique paths for robot to take

Ideas:
- top down backtracking with memoization?
- seach alg on any direction, but track (i, j) with num unique ways
- then num ways from i, j = num ways from i+1, j + num ways i, j+1 (assuming not out of bounds)
O(nm), since memoize.

Bottom up: dp[i][j] = num paths to get to i, j
dp[i][j] = dp[i-1][j] + dp[i][j-1] provided in range

Tactic: Backtrack with memoization, or bottom up dp. both work.


"""

def solve(grid):
    if grid[-1][-1] == 1: return 0
    # init state
    state = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    state[-1][-1] = 1

    def backtrack(state, r, c):
        # out of bounds, return 0
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        
        # at dest - cached
        # if cached
        if state[r][c] != -1:
            return state[r][c]
        
        # else, explore and backtrack

        # if blocked, return 0
        if grid[r][c] == 1:
            state[r][c] = 0
            return 0

        numpaths = backtrack(state, r+1, c) + backtrack(state, r, c+1)
        state[r][c] = numpaths
        return numpaths
        
    return backtrack(state, 0, 0)


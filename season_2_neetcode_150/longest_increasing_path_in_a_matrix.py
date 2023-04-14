"""

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

- have m x n matrix
- need to find longest increasing path, could start from anywhere

Ideas:
- do dfs from each starting point? get path if increasing, and find longest?

- DP: if reach a square, valid, then store longest increasing path from that square
    - will not have clashing items because it's always strictly increasing

- get to each square only once.
O(nm) time

- dp[i][j] = longest increasing path starting from i, j 

Tactic: DFS + memoization, dp[i][j] = longest inc path from i, j. no overlap since strictly increasing

"""

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def solve(matrix):
    n = len(matrix)
    m = len(matrix[0])

    state = [[-1 for _ in range(m)] for _ in range(n)]

    # returns longest path from i, j 
    def dfs(matrix, state, i, j):
        # cache
        if state[i][j] != -1:
            return state[i][j]

        maxLen = 1
        for di, dj in directions:
            newi = i + di
            newj = j + dj
            if newi < 0 or newi >= n or newj < 0 or newj >= m:
                continue
            if matrix[i][j] < matrix[i+di][j+dj]:
                maxLen = max(maxLen, 1 + dfs(matrix, state, i + di, j + dj))
        
        state[i][j] = maxLen
        return maxLen
    
    maxLen = 1
    for i in range(n):
        for j in range(m):
            maxLen = max(maxLen, dfs(matrix, state, i, j))
    return maxLen



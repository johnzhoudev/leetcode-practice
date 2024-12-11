"""329. Longest Increasing Path in a Matrix

m x n matrix
len of longest increasing path?

Idea:
- dfs from each node
- cache visited nodes

O(n) time
O(n) space for dfs visited 

Tactic:
dfs + memo.
"""

def solve(matrix):

    cache = {}
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isInRange(x, y):
        return 0 <= x and x < len(matrix) and 0 <= y and y < len(matrix[0])

    # cache(i, j) => max number of other nodes inc current that can be visited
    def dfs(i, j):
        nonlocal cache

        if (i, j) in cache:
            return cache[(i, j)]
        
        best = 1 # just yourself
        for dx, dy in directions:
            if not isInRange(i + dx, j + dy) or matrix[i + dx][j + dy] <= matrix[i][j]: continue
            best = max(best, 1 + dfs(i + dx, j + dy)) # visited this square
            # will not be able to visit already visited squares, since we go strictly increasing.
            # otherwise, pass a visited array.
        
        cache[(i, j)] = best # add to cache
        return best
    
    best = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            best = max(best, dfs(i, j))
    
    return best


    


"""

62. Unique Paths

mxn grid
top left
move to bottom right

down or right only

num of unique paths to reach corner?

Brute force:
dfs - have to move m units down and n units right, what's the order?

Isn't this just m + n choose n? ie, choose where the n are supposed to go?

O(1)


alternatively, do backtracking soln with memoization
O(mn) space

Tactic:
Easiest is math, choose combinations. Or, do backtracking with memoization. Can also do bottom up dp[i][j] = num ways to get to point (i, j)

"""
import math

def solve(m, n):
    m = m - 1
    n = n - 1

    def mchoosen(m, n):
        return int(math.factorial(m) / (math.factorial(n) * math.factorial(m-n)))
    
    return mchoosen(m+n, n)
        

def solve(m, n):

    cache = {}

    directions = [(1, 0), (0, 1)]

    def isOutOfBounds(x, y):
        return not (0 <= x and x <=m and 0 <= y and y < n)

    # returns number of ways to get from x, y to m, n
    def dfs(x, y):
        if isOutOfBounds(x, y):
            return 0 # out of bounds

        if (x, y) in cache:
            return cache[(x, y)]
        
        if x == m - 1 and y == n - 1:
            cache[(x, y)] = 1
            return 1
        
        totalways = 0
        for dx, dy in directions:
            totalways += dfs(x + dx, y + dy)
        
        cache[(x, y)] = totalways
        return totalways
    
    return dfs(0, 0)

        
        


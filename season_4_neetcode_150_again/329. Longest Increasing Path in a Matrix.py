"""

329. Longest Increasing Path in a Matrix

given matrix, return longest increasing path

Brute force:
- do a dfs from each point, and find longest path
- O(mn * mn)? or maybe more because cells could be visited multiple times
- O(2^mn)? all combos of the cells
- repeating work 

Better:
- cache the results of each dfs at a node
- O(mn)?
- Optimal because you have to check all paths

- Don't need to be concerned about stepping on same path since strictly increasing

Tactic:
DFS + memo. Don't worry about stepping on same path since strictly inc. O(nm)

"""

def solve(matrix):
    cache = {}
    m = len(matrix)
    n = len(matrix[0])

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isValidMove(x, y, prevX, prevY):
        return (0 <= x and x < m and 0 <= y and y < n) and (matrix[prevX][prevY] < matrix[x][y])

    # returns longest increasing path
    def dfs(x, y):

        if (x, y) in cache: return cache[(x, y)]

        longestPath = 1
        for dx, dy in directions:
            if isValidMove(x + dx, y + dy, x, y):
                longestPath = max(longestPath, 1 + dfs(x + dx, y + dy))
        
        cache[(x, y)] = longestPath
        return longestPath
    
    return max([dfs(x, y) for x in range(m) for y in range(n)])


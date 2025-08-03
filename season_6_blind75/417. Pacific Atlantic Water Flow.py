
"""

DFS from both sides, then sync

O(n) dfs and sync

Tactic: dfs from both sides, then take intersection

"""

def solve(heights):
    
    def is_out_of_bounds(x, y):
        return x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0])

    def dfs(x, y, visited):
        if (x, y) in visited:
            return
        visited.add((x, y))
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for dx, dy in directions:
            newX = x + dx
            newY = y + dy

            if is_out_of_bounds(newX, newY) or heights[newX][newY] < heights[x][y]:
                continue # Skip if out of bounds or can't increase
            dfs(newX, newY, visited)
    
    # search for all pacific
    pacific = []
    for row in range(len(heights)):
        pacific.append((row, 0))
    for col in range(len(heights[0])):
        pacific.append((0, col))
    
    pacific_visited = set()
    for x, y in pacific:
        dfs(x, y, pacific_visited)
    
    # search for all atlantic
    atlantic = []
    for row in range(len(heights)):
        atlantic.append((row, len(heights[0]) - 1))
    for col in range(len(heights[0])):
        atlantic.append((len(heights) - 1, col))
    
    atlantic_visited = set()
    for x, y in atlantic:
        dfs(x, y, atlantic_visited)
    
    return list(pacific_visited.intersection(atlantic_visited))
    


    


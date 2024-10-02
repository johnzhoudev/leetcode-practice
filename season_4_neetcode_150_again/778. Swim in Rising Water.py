"""

grid
- elevation
- at time t, depth of water is t
- can swim if adj squares are <= t

- start at top left, end at bot right, min time?

- Start at 0, 0, and keep adding minimum height nodes until you eventually reach the end.
- Max height node added is cost.

- keep heap of nodes

O(n log n) time (basically to sort in heap)

Tactic:
Search using heap to expand smallest height each time.

"""

import heapq
def solve(grid):
    maxHeight = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def isOutOfBounds(x, y):
        return not (0 <= x and x < len(grid) and 0 <= y and y < len(grid[0]))
    
    visited = set()
    heap = []
    heapq.heappush(heap, (grid[0][0], 0, 0)) # height, x, y
    
    while heap:
        h, x, y = heapq.heappop(heap)
        maxHeight = max(maxHeight, h)
        visited.add((x, y))

        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return maxHeight

        # Add neighbours
        for dx, dy in directions:
            newX = x + dx
            newY = y + dy 
            if isOutOfBounds(newX, newY): continue
            if ((newX, newY) in visited): continue
            heapq.heappush(heap, (grid[newX][newY], newX, newY))
    
    return -1
        


import heapq
def solve(grid):
    maxHeight = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def isOutOfBounds(x, y):
        return not (0 <= x and x < len(grid) and 0 <= y and y < len(grid[0]))
    
    visited = set()
    heap = []
    heapq.heappush(heap, (grid[0][0], 0, 0)) # height, x, y
    
    while heap:
        h, x, y = heapq.heappop(heap)
        maxHeight = max(maxHeight, h)
        visited.add((x, y))

        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return maxHeight

        # Add neighbours
        for dx, dy in directions:
            newX = x + dx
            newY = y + dy 
            if isOutOfBounds(newX, newY): continue
            if ((newX, newY) in visited): continue
            heapq.heappush(heap, (grid[newX][newY], newX, newY))
    
    return -1
        




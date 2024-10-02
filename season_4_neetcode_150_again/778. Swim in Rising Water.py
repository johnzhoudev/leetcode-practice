"""

grid
- elevation
- at time t, depth of water is t
- can swim if adj squares are <= t

- start at top left, end at bot right, min time?

- Start at 0, 0, and keep adding minimum height nodes until you eventually reach the end.
- Max height node added is cost.

O(n) time


"""

import heapq
def solve(grid):
    maxHeight = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def isOutOfBounds(x, y):
        return not (0 <= x and x <= len(grid) and 0 <= y and y <= len(grid[0]))
    
    visited = set()
    heap = []
    heapq.heappush((grid[0][0], 0, 0))
    
    while state:



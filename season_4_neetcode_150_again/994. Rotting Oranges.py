"""

Rotting oranges

0 empty
1 fresh orange
2 rotting

rots every minute 4 dir

return min until no fresh orange, else -1

idea:
- restrictions on grid length?

- just do bfs, increase minute count. O(n)
- if none left, do one more parse to count fresh 

"""

from collections import deque

def solve(grid):
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    state = deque()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                state.appendleft((i, j))
    
    def checkInBounds(x, y):
        return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])
    
    minute = 0
    # Cool loop trick
    while state:
        didRot = False
        for _ in range(len(state)):
            x, y = state.pop()
            for dx, dy in directions:
                newX = x + dx
                newY = y + dy

                if not checkInBounds(newX, newY): continue
                if grid[newX][newY] != 1: continue
                # else is orange
                grid[newX][newY] = 2 # rot
                didRot = True
                state.appendleft((newX, newY))
        if didRot: minute += 1
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return -1
    
    return minute




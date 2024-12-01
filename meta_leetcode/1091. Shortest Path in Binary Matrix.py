"""


1091. Shortest Path in Binary Matrix


shortest clear path

- from top left to bottom right
- all must be 0
- all are 8-directionally connected

A graph alg, shortest path
- bfs with visited

A*
- need to use steps + heuristic
- heuristic <= true value is a must for it to converge...

Tactic:
BFS. Or A*, see impl

"""

import heapq

# A* implementation
def solve(grid):
    goal = (len(grid) - 1, len(grid[0]) - 1)

    # can move diagonally
    def minDist(steps, x, y):
        return steps + max(abs(goal[0]-x), abs(goal[1] - y))

    directions = [(dx, dy) for dx in [1, 0, -1] for dy in [1, 0, -1] if dx != 0 or dy != 0]
    def isOutOfBounds(x, y):
        return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])
    
    # For A*, maintain a heap of the next distances 
    heap = []
    heapq.heappush(heap, (minDist(1, 0, 0), 1, 0, 0)) # mindist, steps, x, y

    while heap:
        _, steps, x, y = heapq.heappop(heap) # pop smallest

        if grid[x][y] != 0:
            continue
        
        # valid, so explore
        if (x, y) == goal:
            return steps
        grid[x][y] = 1

        for dx, dy in directions:
            # out of bounds could throw off minDist calculation
            if not isOutOfBounds(x + dx, y + dy):
                heapq.heappush(heap, (minDist(steps, x + dx, y + dy), steps + 1, x + dx, y + dy))
    
    return -1





def solve(grid):

    # trick, use grid = 1 as visited
    goal = (len(grid)-1, len(grid[0])-1)

    state = [(0, 0)]
    directions = [(dx, dy) for dx in [1, 0, -1] for dy in [1, 0, -1] if dx != 0 or dy != 0]
    # print(directions)

    def isOutOfBounds(x, y):
        return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])
    
    length = 0
    while state:
        length += 1
        newState = []

        for x, y in state:

            if isOutOfBounds(x, y):
                continue
            if grid[x][y] != 0: # already visited or invalid, pass
                continue
            
            # grid is 0

            if (x, y) == goal:
                return length

            grid[x][y] = 1 # mark as visited
            for dx, dy in directions:
                newState.append((x + dx, y + dy))
        
        state = newState
    
    return -1




solve([])


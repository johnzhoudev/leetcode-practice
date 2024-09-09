"""

2d, treasure chests and walls / water

wall = -1
treasure = 0
inf = empty space

fill each with distance to nearest treasure chest

ideas:

brute force, bfs from each point to get to treasure chest
O(n^2)

or search from each treasure chest, add points as you go?
- or do bfs from all treasure chests?

- traverse first to find all chests
- then put in queue, and explore one by one - only explore next if distance less than curr distance

O(n) time?

"""

from collections import deque
def solve(grid):
    state = deque()

    inf = 2147483647

    # Load all treasures
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                state.appendleft((i, j, 0)) # x, y, dist from thing

    # Now do bfs
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def checkInBounds(x, y):
        return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])


    while state:
        (x, y, dist) = state.pop() # already added

        for dx, dy in directions:
            if not checkInBounds(x + dx, y + dy): continue
            elif grid[x + dx][y + dy] == -1 or grid[x + dx][y+dy] <= dist + 1: continue
            # can replace
            grid[x + dx][y+dy] = dist + 1
            state.appendleft((x + dx, y + dy, dist + 1))
        
    # return grid







    


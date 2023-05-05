"""

https://leetcode.com/problems/swim-in-rising-water/

- grid, elevation
- at time t, depth of water everywhere is t
    - can swim from one to another if elevation in both squares is at most t. 
- can swim any distance in 0 time.

- Basically find the path with the smallest edge weight from top left to bottom right.

- search algorithm
- top down dp, path minimum from x to end

- or maybe do a dfs but adding the minimum edge each time, to a new thing.
O(n log n), log n each time to add an edge or new square (get min), plus n items
- where n is number of cubes.

DP Idea: dp[i][j] = least resistance path to get from i, j to end.
    - but thing is can go backwards, so this isn't really a subproblem.
    - either way runtime is O(n log n)

Idea: Do a search, but add the minimum edge each time reachable. Kind of like prim's alg.
- dfs works, try and add each direction

Tactic: Do search, but add squares reachable + minimum weight at a time. Use heap. Works because if you add many, will always add smaller ones first. And watch max weight needed.
"""

import heapq

def solve(grid):
    # init dfs
    # state = [(grid[0][0], (0, 0))] # (weight, (x, y))
    state = [(grid[0][0], (0, 0))] # (weight, (x, y))
    minWeight = grid[0][0]
    visited = set()
    heapq.heapify(state)

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while state:
        weight, (x, y) = heapq.heappop(state)
        # out of bounds check
        if (x, y) in visited:
            continue
        visited.add((x, y))
        weight = grid[x][y]
        minWeight = max(weight, minWeight)

        if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
            return minWeight

        # now add adjacents to heap. if something larger, will only be added when nothing smaller can be added
        for dx, dy in dir:
            newx = x + dx
            newy = y + dy
            if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]) or (newx, newy) in visited:
                continue
            heapq.heappush(state, (grid[newx][newy], (newx, newy)))
    return -1

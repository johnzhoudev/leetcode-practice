"""

827. Making A Large Island


change at most one 0 to a 1
- return largest size
- largest 4 directionally connected group?

Ideas:

- Do dfs, make map of each coordinate to a size counter 
    - mutable reference
- Then on subsequent pass, all empties, check neighbours and see if you can connect
    - check references to make sure not equal

O(n) time
O(n) space for storing the coordinate map
    - O(n) space anyway for visited

Better than using references: Just use index - set!

Tactic:
1st pass dfs, use index to store size of each zone. Then 2nd pass, look up different zone sizes.

"""

from collections import defaultdict

def solve(grid):
    groupSizes = defaultdict(lambda : 0) # map of index => [count]
    nodes = {} # map of node to group idx

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isOutOfBounds(row, col):
        return not (0 <= row and row < len(grid) and 0 <= col and col < len(grid[0]))

    def dfs(i, j, groupIndex):
        nonlocal nodes
        nonlocal groupSizes
        nonlocal directions

        # already visited
        if (i, j) in nodes:
            return
        
        # Don't continue exploring if 0 or out of bounds
        if isOutOfBounds(i, j) or grid[i][j] == 0:
            return

        assert(grid[i][j] == 1)
        nodes[(i, j)] = groupIndex
        groupSizes[groupIndex] += 1
        
        # explore rest
        for dx, dy in directions:
            dfs(i + dx, j + dy, groupIndex)
    
    idx = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in nodes:
                dfs(i, j, idx) # only adds if not visited or out of bounds
                idx += 1
    
    # Best individual island size
    bestSize = max(groupSizes.values(), default=0)
    # in case none are 0

    def getBestNeighSize(i, j):
        nonlocal directions
        neighs = set()
        for dx, dy in directions:
            if not isOutOfBounds(i + dx, j + dy) and grid[i + dx][j + dy] == 1:
                # only add new areas
                neighs.add(nodes[(i + dx, j + dy)]) # adds idx
        
        # actually just add them all together
        return 1 + sum([groupSizes[x] for x in neighs])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if can be 0, calc best island
            if grid[i][j] == 0:
                bestSize = max(bestSize, getBestNeighSize(i, j))
    
    return bestSize
                

def solve(grid):
    nodes = {} # map of (i, j) => [count]
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isOutOfBounds(row, col):
        return not (0 <= row and row < len(grid) and 0 <= col and col < len(grid[0]))

    def dfs(i, j, sizeRef):
        nonlocal nodes
        nonlocal directions

        # already visited
        if (i, j) in nodes:
            return
        
        # Don't continue exploring if 0 or out of bounds
        if isOutOfBounds(i, j) or grid[i][j] == 0:
            return

        assert(grid[i][j] == 1)
        sizeRef[0] += 1
        nodes[(i, j)] = sizeRef
        
        # explore rest
        for dx, dy in directions:
            dfs(i + dx, j + dy, sizeRef)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            sizeRef = [0, i, j] # ticketing system
            dfs(i, j, sizeRef) # only adds if not visited or out of bounds
    
    # print(nodes)
    # Now combine regions

    # Best individual island size
    bestSize = max([x[0] for x in nodes.values()], default=0)
    # in case none are 0

    def getBestNeighSize(i, j):
        nonlocal directions
        neighs = []
        for dx, dy in directions:
            if not isOutOfBounds(i + dx, j + dy) and grid[i + dx][j + dy] == 1:
                # only add new areas
                if nodes[(i + dx, j + dy)] not in neighs:
                    neighs.append(nodes[(i + dx, j + dy)])
        
        # actually just add them all together
        return 1 + sum([x[0] for x in neighs])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if can be 0, calc best island
            if grid[i][j] == 0:
                # print(i, j)
                # print(getBestNeighSize(i, j))
                bestSize = max(bestSize, getBestNeighSize(i, j))
    
    # print(nodes)
    # nodes[(0, 0)][0] += 1
    # print(nodes)
    # assert(nodes[(0, 0)] != nodes[(1, 1)])
    return bestSize
                



print(solve([[1,0],[0,1]]))
print(solve([[0,0,0,0,0,0,0],
             [0,1,1,1,1,0,0],
             [0,1,0,0,1,0,0],
             [1,0,1,0,1,0,0],
             [0,1,0,0,1,0,0],
             [0,1,0,0,1,0,0],
             [0,1,1,1,1,0,0]]))




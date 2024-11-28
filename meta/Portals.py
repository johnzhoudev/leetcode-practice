"""

Portals

- . is empty
- S, E start end
- # wall
- a..z is portal, on entering, will appear at any of them

Shortest path to end.

BFS? do bfs. visited. keep min. O(n)

Teleporting takes time!

"""

from collections import deque, defaultdict

def solve(R, C, grid):
    state = deque()

    portals = defaultdict(list)

    def findStartAndBuildMap():
        start = None
        ignore = set(['S', 'E', '.', '#'])
        
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 'S':
                    start = (row, col)
                elif grid[row][col] in ignore:
                    continue
                else:
                    portals[grid[row][col]].append((row, col))
                
        assert(start != None)
        return start


    state.append(findStartAndBuildMap())

    print(portals)

    # now do bfs

    def isInBounds(x, y):
        return 0 <= x and x < R and 0 <= y and y < C

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    numSteps = 0

    while len(state) != 0:
        n = len(state)

        for _ in range(n):
            r, c = state.popleft()

            if (r, c) in visited: continue # already seen, continue

            if (not isInBounds(r, c)): continue

            val = grid[r][c]

            if (val == 'E'):
                return numSteps
            elif (val == '#'):
                pass
            elif (val == 'S' or val == '.'):
                for dr, dc in directions:
                    state.append((r + dr, c + dc)) # just add normally
            else: # portal, can either walk left and right, or portal
                for dr, dc in directions:
                    state.append((r + dr, c + dc)) # just add normally
                for nr, nc in portals[val]:
                    # if (nr, nc) in visited: continue
                    state.append((nr, nc))

            visited.add((r, c))

        numSteps += 1
    
    return -1




R = 3
C = 4
G = [['a', 'S', '.', 'b'],
    ['#', '#', '#', '#'],
    ['E', 'b', '.', 'a' ]]

print(solve(R, C, G))



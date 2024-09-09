"""

417. Pacific Atlantic Water Flow

pacific - left and top
atlantic - bot and righ
- can flow if leq
- return list of coords that can flow to ocean - unsorted?

Idea:
- do dfs, if reach ocean or another node that reached ocean, keep stack trace and mark as reached?
- or, if blocked, mark as blocked and terminate?

OR, do dfs from all edge blocks

O(n) time, only ever visit each block once and results in blocked or good


Ohh, must be able to flow to both! not just one or the other
- soln, do 2 dfs's from the corners

"""

def solve(heights):

    state = []
    for r in range(len(heights)):
        state.append((r, 0)) # left edge
        # state.append((r, len(heights[0]) - 1)) # right edge
    for c in range(len(heights[0])):
        state.append((0, c)) # top edge
        # state.append((len(heights) - 1, c)) # bot edge

    reachableFromPacific = dfs(heights, state)

    # atlantic
    state = []
    for r in range(len(heights)):
        state.append((r, 0)) # left edge
        # state.append((r, len(heights[0]) - 1)) # right edge
    for c in range(len(heights[0])):
        state.append((0, c)) # top edge
        # state.append((len(heights) - 1, c)) # bot edge
    
    reachableFromAtlantic = dfs(heights, state)

    def dfs(heights, state):
        added = set()
        def isInBounds(x, y):
            return 0 <= x and x < len(heights) and 0 <= y and y < len(heights[0])
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while state:
            x, y = state.pop()
            if (x, y) in added: continue

            added.add((x, y)) # can reach
            for dx, dy in directions:
                if not isInBounds(x + dx, y + dy): continue
                if heights[x][y] > heights[x + dx][y + dy]: continue # can't go down
                state.append((x + dx, y + dy))
            
        return added
    
    output = []
    for p in reachableFromAtlantic:
        if p in reachableFromPacific:
            output.append(p)

    return output



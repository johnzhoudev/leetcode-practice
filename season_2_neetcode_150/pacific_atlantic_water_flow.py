"""

https://leetcode.com/problems/pacific-atlantic-water-flow/


- Return 2d array of coordinates that can flow to both the atlantic and pacific ocean

Idea:
- do a dfs starting from each side, going up. 
- will only process each cell once.
- O(n*n)
- if dfs reaches cells reachable from both sides, all good.

- can do iterative dfs since only have to store current height. just maintain set of visited

Tactic: DFS from the ocean, maintain sets of what has been reached. Also if reached, don't need to reach again in dfs.

"""

def solve(heights):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # dfs using state as starting point, and add to visited
    def dfs(state, visited):
        while state:
            row, col = state.pop()
            # process
            visited.add((row, col))

            # add children
            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc
                if newRow < 0 or newRow >= len(heights) or newCol < 0 or newCol >= len(heights[0]) or (newRow, newCol) in visited:
                    continue
                if heights[row][col] <= heights[newRow][newCol]:
                    state.append((newRow, newCol))
        
    # search from first side
    state = [(0, col) for col in range(len(heights[0]))] + [(row, 0) for row in range(len(heights))] # top and left edges
    pacific = set()
    dfs(state, pacific)
    state = [(len(heights)-1, col) for col in range(len(heights[0]))] + [(row, len(heights[0])-1) for row in range(len(heights))]
    atlantic = set()
    dfs(state, atlantic)

    output = []
    for x in pacific:
        if x in atlantic:
            output.append(x)
    return output








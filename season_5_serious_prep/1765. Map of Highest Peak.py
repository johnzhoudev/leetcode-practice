"""

1765. Map of Highest Peak

- water map
- need to make map of highest peaks
- adj cells can diff at most 1

- can only re-raise if touching others that were raised.
    - if any stopped, done.

Naive way: multiple passes to see if you can raise
- must do other passes => surrounding depends on those?
- Or, maybe do dfs and have dfs return the height
    - but what about mutual recursive?

- Or maybe dfs from water to get 1's, then from 1's to get 2's, etc.
O(n)


Salad Ingredients
- lemon
- quinoa
- salt
- pepper
- sugar
- olive oil
- cucumbers tomatoes onions
- parsely / cilantro
- mung bean? steam with quinoa
- cheese
- roasted nuts or pumpkin seeds

"""

from collections import deque

def solve(isWater):

    toVisit = deque()
    output = [[-1 for _ in range(len(isWater[0]))] for _ in range(len(isWater))] # make output arr and init to all -1
    for i in range(len(isWater)):
        for j in range(len(isWater[0])):
            if isWater[i][j] == 1:
                toVisit.append((i, j))
                output[i][j] = 0
    
    # Water added, now bfs

    def isOutOfBounds(i, j):
        return i < 0 or i >= len(isWater) or j < 0 or j >= len(isWater[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    level = 0
    while toVisit:
        n = len(toVisit)
        for _ in range(n):
            x, y = toVisit.popleft()
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if isOutOfBounds(newX, newY): continue
                elif output[newX][newY] != -1: continue
                else:
                    # can increase height of this one since reached by other
                    output[newX][newY] = level + 1
                    toVisit.append((newX, newY))
        level += 1
    
    return output

print(solve([[0,1],[0,0]]))








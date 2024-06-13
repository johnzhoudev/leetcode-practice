"""

https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

stone removed if it shares same row and col with another non removed stone

max stones that can be removed 

O(n) to build graph
- adjacency, x row and y row defaultdict?

Tactic: Count number of islands. Use DFS. Could also use union find??? since union between rows and cols


"""

from collections import defaultdict

def solve(stones): # array [xi, yi]
    # build graph

    xList = defaultdict(list)
    yList = defaultdict(list)

    seen = set()

    for [x, y] in stones:
        # TODO: only use other ordinate
        xList[x].append((x, y))
        yList[y].append((x, y))
        seen.add((x, y))
    
    # Do search for each component
    numComponents = 0
    while seen:
        (x, y) = seen.pop()
        seen.add((x, y)) # add back

        numComponents += 1
        # Remove all others
        stack = [(x, y)]

        while stack:
            (currX, currY) = stack.pop()
            if (currX, currY) in seen:
                seen.remove((currX, currY))
            else:
                continue # already removed
            # add all others

            for (nextX, nextY) in xList[currX]:
                stack.append((nextX, nextY))
            for (nextX, nextY) in yList[currY]:
                stack.append((nextX, nextY))

            # Empty list since visited
            xList[currX] = []
            yList[currY] = []
    
    return len(stones) - numComponents







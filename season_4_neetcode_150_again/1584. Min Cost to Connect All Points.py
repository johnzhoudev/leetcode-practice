"""

manhattan distance

- min cost connections between all

Idea:
- generate all pairs and costs
- sort by cost
- add lowest cost edge union find, until all connected

MST algorithm!

O(n^2) time to generate all pairs
O(n log n) sorting
O(n) union find with rank compression
    - or greedily add smallest edge?
- Go until you've added n-1 edges

Kruskal's Algorithm: Generate all edges, Add min weighted edges and do union find untill all connected. O(E log E)
Prim's Algorithm: From each point, just add min weighted edge to the pool and continue, using heap. O(E + V log V)??

Prim's algorithm faster.

"""

# Prim's alg
import heapq

def solve(points):
    def dist(i, j):
        x1, y1 = points[i]
        x2, y2 = points[j]
        return abs(y2-y1) + abs(x2-x1)
    heap = []
    addedPoints = set()
    
    # add first point
    addedPoints.add(0) # use idx
    for i in range(len(points)):
        d = dist(0, i)
        heapq.heappush(heap, (d, i))
    
    # Now loop
    total = 0
    while len(addedPoints) < len(points):
        d, dest = heapq.heappop(heap)
        while dest in addedPoints:
            d, dest = heapq.heappop(heap)

        total += d
        addedPoints.add(dest)

        # add new destinations
        for newDest in range(len(points)):
            if newDest in addedPoints: continue
            heapq.heappush(heap, (dist(dest, newDest), newDest))
    
    return total









# Kruskal's alg
from collections import defaultdict
def solve(points):

    def dist(x1, y1, x2, y2):
        return abs(y2-y1) + abs(x2-x1)
    # generate all pairs and costs
    # literally a fully connected graph
    edges = []
    for i, (x, y) in enumerate(points):
        for j, (x2, y2) in enumerate(points):
            edges.append((i, j, dist(x, y, x2, y2))) # point idx, point b idx, distance
    
    # sort edges
    edges.sort(key=lambda x : x[2])

    # Now go and run union find, only add edge if connecting two different.
    ranks = defaultdict(lambda : 0)
    parents = {}
    for i in range(len(points)):
        parents[i] = i
    
    def parent(i):
        stack = []
        while parents[i] != i:
            stack.append(i)
            i = parents[i]
        # now compress paths
        for j in stack:
            parents[j] = i
        
        return i
    
    def union(x, y): # false if already in same 
        xPar = parent(x)
        yPar = parent(y)

        if xPar == yPar:
            return False
        
        # Always add to parent with larger rank => more children, so children traverse less
        if ranks[xPar] > ranks[yPar]:
            parents[yPar] = xPar 
            ranks[xPar] += 1
        else:
            parents[xPar] = yPar 
            ranks[yPar] += 1
        return True
    
    numAdded = 0
    totalCost = 0
    for (i, j, d) in edges:
        if union(i, j): # if able to add
            numAdded += 1
            totalCost += d
        
        if numAdded == len(points) - 1:
            break
    
    return totalCost

        

        



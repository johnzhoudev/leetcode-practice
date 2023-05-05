"""

https://leetcode.com/problems/min-cost-to-connect-all-points/

- given points in plane, x y
- cost to connect 2 points is manhattan distance
- return min distance to connect all points - make a tree

Ideas:
- dijkstras?
- compute distances between each points
- start at an arbitrary point, and add min distance point to set and update
- not correct. x

- problem is compute the minimum weight spanning tree of this set
    - greedy? order all edges by weight and add minimum weight edges
    - true.

- either prim's alg (arb vertex, add smallest edge reaching outside set)
- or kruskall's alg (sort edges, start adding unless makes loop. disjoint set union stuff. might be worthwhile to impl)


Tips:
- graph creation is O(n^2), but can do a bit better by dynamically adding edges during the main loop only if (u, v) v is not visited yet
- tip also, break from while loop as soon as n found


Tactic: Prim's alg with heap and visited. Break early when n reached. Can build adj list before, or generate on the fly (state = dist, new point, only add if visited).


"""
from collections import defaultdict
import heapq

def solve(points):
    def dist(x, y, x2, y2):
        return abs(y2-y) + abs(x2-x)
    
    # Don't build adj, just go straight into the loop
    n = len(points)
    totalSum = 0
    state = [(0, (points[0][0], points[0][1]))] # stores distance, (new point)
    heapq.heapify(state)
    visited = set()

    while state and len(visited) != n:
        d, (x, y) = heapq.heappop(state)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        totalSum += d
        # add adjacent
        for (x2, y2) in points:
            if (x2, y2) not in visited:
                heapq.heappush(state, (dist(x, y, x2, y2), (x2, y2)))
    
    return totalSum

# Use prim's alg, basic

test = [[0,0],[2,2],[3,10],[5,2],[7,0]]

def solve(points):

    def dist(x, y, x2, y2):
        return abs(y2-y) + abs(x2-x)
    # create graph / adjacency list
    adj = defaultdict(list)

    for x, y in points:
        for x2, y2 in points:
            if x == x2 and y == y2:
                continue
            adj[(x, y)].append((dist(x, y, x2, y2), x2, y2))
    
    # do prim's alg. Maintain heap of edges, and remove. 
    first = (points[0][0], points[0][1])
    visited = set()
    visited.add(first)
    # need heap of smallest weights
    next = [val for val in adj[first]]
    heapq.heapify(next)
    totalCost = 0

    while next and len(visited) < len(points): # Adding the break here is actually quite important for time.
        d, x, y = heapq.heappop(next)
        # if point in tree, continue
        if (x, y) in visited:
            continue
        visited.add((x, y))
        # else add the point, update total cost, and add new edges
        totalCost += d
        for val in adj[(x, y)]:
            heapq.heappush(next, val)
    
    return totalCost







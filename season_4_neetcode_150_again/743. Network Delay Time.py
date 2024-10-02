"""

directed edges with travel times
- send node from k
- min time it takes for all nodes to receive signal

- Basically find shortest paths to all nodes, and take max
- Dijkstra? just add edges to pool and continue until all nodes reached

O(v log v) runtime

"""

import heapq
from collections import defaultdict
def solve(times, n, k):
    # create adjacency list
    adjList = defaultdict(list)
    for u, v, d in times:
        adjList[u].append((v, d))

    longestPath = 0
    heap = []
    visitedNodes = set()

    # setup minheap and start from starting node
    visitedNodes.add(k)
    for dest, d in adjList[k]:
        heapq.heappush(heap, (d, dest))

    while len(visitedNodes) != n and heap:
        totalD, dest = heapq.heappop(heap)
        visitedNodes.add(dest)
        longestPath = totalD
        for nextDest, d2 in adjList[dest]:
            if nextDest in visitedNodes: continue
            heapq.heappush(heap, (d2 + totalD, nextDest))

    return longestPath if len(visitedNodes) == n else -1







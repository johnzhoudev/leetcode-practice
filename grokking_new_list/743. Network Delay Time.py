"""

743. Network Delay Time
https://leetcode.com/problems/network-delay-time/description/

nodes 1 to n
(u, v, w) time to travel
send signal from k
min time for all n nodes to receive signal

Idea:

djikstra's, maintain heap of least weights travelled and explore
- keep track of largest
- keep track of explored count


Tactic: Djikstra's BFS, can use a queue! 

"""

import heapq
from collections import defaultdict

def solve(times, n, k):
    # build adjacency list
    adj = defaultdict(list)

    for (u, v, w) in times:
        adj[u] += [(v, w)]
    
    # create heap for weights
    heap = [(0, k)]
    maxTime = 0
    numVisited = 0
    visited = set()

    while heap:
        expWeight, node = heapq.heappop(heap)
        if node in visited: continue
        visited.add(node)
        numVisited += 1
        maxTime = max(maxTime, expWeight)
        # add others
        for (v, w) in adj[node]:
            heapq.heappush(heap, (expWeight + w, v))
    
    return maxTime if numVisited == n else -1
        




print(solve([[2,1,1],[2,3,1],[3,4,1]], 4, 2))




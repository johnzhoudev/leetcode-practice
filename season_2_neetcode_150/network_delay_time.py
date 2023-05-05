"""

https://leetcode.com/problems/network-delay-time/

- n nodes
- travel times (source, target, weight)
- send signal from k

- so simultaneously emits from source, and then goes to target

Ideas:
- BFS, but the time thing comes into play
- maintain a min heap of the time, and pop the min time and add that to the search
- also add neighbours
- once hit n things, done.

O(n log n) time, accounting for getting the min
O(times) size to create the adjacency list, maximum O(n^2)

Tactic: Basically do BFS, but use minheap for time and add in order of timestamp. state = (timeToActivate, vert). Use visited.

"""

from collections import defaultdict
import heapq

def solve(times, n, k):
    # create adj list
    adj = defaultdict(list)

    for u, v, t in times:
        adj[u].append((t, v))
    
    state = [(0, k)] # (time, (point))
    visited = set()
    heapq.heapify(state)
    time = 0

    while state and len(visited) != n:
        d, v = heapq.heappop(state)
        if v in visited:
            continue
        visited.add(v)
        time = d
        # now add adjacent things
        for (deltat, v2) in adj[v]:
            if v2 in visited: continue
            heapq.heappush(state, (d + deltat, v2))
    
    return time if len(visited) == n else -1




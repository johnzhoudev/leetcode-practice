"""

https://leetcode.com/problems/cheapest-flights-within-k-stops/

- n cities
- flights array from, to, price
- src, dest, k
- cheapest flight from src to dest with at most k stops. else ret -1

Ideas:
- can't use dijkstras, have to break early if k stops. how to know which stop to skip?
- dfs, add edges in order of lowest cost and maintain seen. if edge visited already

- BFS? k iterations, record best times
- O(n * k)


Tactic: Easiest way, level BFS and remove states if reach node with higher cost. Keep bestPrice defaultdict. But maybe can use dijkstra or DFS? Many ways to skin this cat.
- actually this is bellamn ford

"""

from collections import defaultdict

def solve(n, flights, src, dst, k):
    # make adj list
    adj = defaultdict(list)
    for f, t, prx in flights:
        adj[f].append((prx, t))

    # just do bfs
    level = 0
    bestPrice = defaultdict(lambda: float('inf')) # use to store best price
    state = [(src, 0)] # node, currprice. if on while loop you reach with more or equal to bestprice, break

    while level <= k + 1:
        dummy = []

        for node, prx in state:
            # early break if we've already reached node with a lower price
            if prx >= bestPrice[node]:
                continue
            bestPrice[node] = prx
            # now add adjacents
            for dp, dest in adj[node]:
                dummy.append((dest, prx + dp))

        state = dummy
        level += 1

    return bestPrice[dst] if bestPrice[dst] != float('inf') else -1

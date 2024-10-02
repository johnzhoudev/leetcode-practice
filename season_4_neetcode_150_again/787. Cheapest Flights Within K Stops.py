"""

n cities
flights from, to, price
src, dst, k
cheapest price from src todest with at most k stops, or -1

Maybe do a BFS with k steps, keep map of each node with lowest price to reach there.
See what happens after k steps
only continue searching if reached a point with new low amount

No multiple flights between 2 cities

O(k n )
Tactic:
Do breadth first search iteratively, maintain cheapestCost dict and update. Make sure to update copy of cheapestCost and set equal to copy at end!
Or, just do normal BFS with pruning (if cost is higher than current best)?

"""

from collections import defaultdict
def solve(n, flights, src, dst, k):
    # Adjacency list
    adjList = defaultdict(list)
    for fr, to, pr in flights:
        adjList[fr].append((to, pr))
    
    # cheapest arr
    cheapestCost = defaultdict(lambda : float('inf'))

    # now do bfs
    state = [src]
    cheapestCost[src] = 0
    level = 1
    while state and level <= k + 1:
        newState = set()
        cheapestCostNew = cheapestCost.copy()
        for currState in state:
            for nextState, price in adjList[currState]:
                if cheapestCost[currState] + price < cheapestCost[nextState]:
                    cheapestCostNew[nextState] = min(cheapestCost[currState] + price, cheapestCostNew[nextState])
                    newState.add(nextState)
        
        state = list(newState)
        cheapestCost = cheapestCostNew
        level += 1
    
    return cheapestCost[dst] if cheapestCost[dst] != float('inf') else -1



            






    


"""

Graph valid tree

- list of edges
- check if it's a valid tree (no cycles)
- edges are undirected! so only one instance

Idea:
- do dfs from any node and see if you hit a loop (revisit visited)
- also, check if connected!

- when exploring, keep track of previous node so you don't mistake undirected edge as backwards
- or, if you use an edge forwards, remove the backwards edge

Tactic: Cycle detection in undirected graph - remove backwards edge, watch for self edges

"""

def solve(n, edges):
    adjList = [set() for _ in range(n)]

    for a, b in edges:
        if a == b: return False
        adjList[a].add(b)
        adjList[b].add(a)
    
    state = [0]

    visited = set()

    # edge case: self edges
    while state:
        curr = state.pop()
        if curr in visited:
            return False
        visited.add(curr)

        for next in adjList[curr]:
            # remove backwards edge
            state.append(next)
            adjList[next].remove(curr) # don't go backwards
    
    return len(visited) == n
    







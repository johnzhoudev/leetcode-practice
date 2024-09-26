
"""

undirected graph n nodes
edges [a, b]
- num connected components?

DFS from each num?
mark as visited?

"""

def solve(n, edges):

    adjList = [[] for _ in range(n)]
    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    
    visited = set()

    def dfs(i):
        if i in visited: return
        visited.add(i)
        for next in adjList[i]:
            dfs(next)
        
    numIslands = 0
    for start in range(n):
        if start not in visited:
            numIslands += 1
            dfs(start)
    
    return numIslands


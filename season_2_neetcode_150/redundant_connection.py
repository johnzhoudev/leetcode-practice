"""

https://leetcode.com/problems/redundant-connection/

- tree is connected undirected graph with no cycles
- an edge has been added to the tree between 2 different nodes
- return edge occurring last in the input

Ideas:
- pretty much need cycle detection here

- DFS until you find a node already in seen, then you have a cycle in the state
- pop edges as part of the cycle until you get to start, and keep index of last edge

- Wow that was so bad

Idea 2: Add edges to the graph as you go, and if the two ends are connected before you add, then that's the one.
- set union / disjoint sets to maintain

Idea: Union Find problem
- add edges, and until you try and add an edge connecting two elts in same set, return. that's the cycle.
- process in order of edges

Union Find Algorithm
- Represent sets as graphs / trees (not binary)
- find(x) gives topmost element. impl with parent array
- union(x) adds smaller rank set as child of larger. just set parent, since we only search upwards. use parent array
    - increment rank of parent
- can compress path during a search, the searched elements just attach to parent

Time: O(log n) for each find and join, with rank. So O(n log n), since we potentially join all

Tactic: Add edges one by one, union find. Union find using rank, compression, parent arr.

"""

def solve(edges):
    # from, to
    # setup state / union find
    n = len(edges)
    parent = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]

    def find(x):
        backtrace = []
        while parent[x] != x:
            backtrace.append(x)
            x = parent[x]
        for y in backtrace: # compress path
            parent[y] = x
        return x
    
    def union(x, y):
        s1 = find(x)
        s2 = find(y)
        if rank[s1] > rank[s2]:
            parent[s2] = s1
            rank[s1] += 1
        else:
            parent[s1] = s2
            rank[s2] += 1

    for f, t in edges:
        s1 = find(f)
        s2 = find(t)
        if s1 == s2:
            return [f, t]
        union(s1, s2)
    
    raise RuntimeError()
        






# slow dfs
def solve(edges):
    # develop adj lists
    n = len(edges) # from 1 to n
    adj = [[] for _ in range(n + 1)]
    for f, t in edges:
        adj[f].append(t)
        adj[t].append(f)
    # edges is list of edges, [start, end]
    # keep visited and path 
    visited = set()
    pathNodes = set()
    path = []

    def getLoopEdgeIdx(path, i):
        edge = path.pop()
        edge.sort()
        loopIdx = edges.index(edge)
        print(loopIdx)
        while path and path[-1][1] != i: # while not out of loop
            edge = path.pop()
            edge.sort()
            loopIdx = max(edges.index(edge), loopIdx)
            print(loopIdx)
        return loopIdx
    
    # returns edge index
    def dfs(visited, pathNodes, path, i):
        print(i, visited, pathNodes, path)

        # first, handle if this is a loop
        if i in pathNodes:
            return getLoopEdgeIdx(path, i)

        # since it's a tree, might not need this
        elif i in visited:
            # already seen, don't need to continue
            return -1
        
        # prep next cases
        visited.add(i)
        pathNodes.add(i)
        for next in adj[i]:
            path.append([i, next])
            adj[next].remove(i) # taking this path, so don't go back            
            res = dfs(visited, pathNodes, path, next)
            if res != -1:
                return res
            # remove edge to avoid traversing again
            path.pop()
        pathNodes.remove(i)
        visited.remove(i)

        return -1
    res = dfs(visited, pathNodes, path, 1)
    if res == -1: return -1
    return edges[res]

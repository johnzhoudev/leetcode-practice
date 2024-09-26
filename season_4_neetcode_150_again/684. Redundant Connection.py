"""

undirected graph with no cycles = tree
added edge chooses 2 different vertices
edges
return edge that can be removed
- if multiple answers, return last edge in input

ie, find edge in cycle

union find

- all points on their own at first
- edges connect points, add in order of input => edge that connects is last

- if edge connects same, then return that edge

O(n) space
O(n) time

-- Better, use rank to make union more efficient

"""

def solve(edges):
    n = len(edges)
    parentTable = {}
    rank = {}

    for i in range(1, n + 1):
        parentTable[i] = i
        rank[i] = 0

    def parent(i):
        stack = []
        while parentTable[i] != i:
            stack.append(i)
            i = parentTable[i]
        
        for x in stack:
            parentTable[x] = i

        return i
    
    def union(i, j):
        parentI = parent(i)
        parentTable[parentI] = parent(j)
    
    # now solve
    for u, v in edges:
        if (parent(u) == parent(v)):
            return (u, v)
        
        union(u, v)
    
    raise RuntimeError()





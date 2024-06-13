"""

547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/description/


n cities
direct and indirect connection
province - connected cities

total number of provinces?

Seems like just dfs from each province, keep track of what's seen

Union Find?
- each element starts as a lone tree
- go thru adjacency list and union all elements
- at end, go thru and see how many heads there are

"""

# Union find algorithm
def solve(isConnected):
    n = len(isConnected)
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]
    numUnique = n

    def find(x):
        backtrace = []
        while parent[x] != x: # while not the root
            backtrace.append(x)
            x = parent[x]
        
        # efficincy, compress
        for y in backtrace:
            parent[y] = x
        return x

    def union(x, y):
        parX = find(x)
        parY = find(y)
        if parX == parY: return

        # else connecting 2 diff things, decrease num islands
        nonlocal numUnique
        numUnique -= 1

        if rank[parX] < rank[parY]: # x smaller than y, so append x to y
            parent[parX] = parY
            rank[parY] += 1
        else:
            parent[parY] = parX
            rank[parX] += 1
    
    for i in range(n):
        for j in range(i, n):
            if isConnected[i][j]:
                union(i, j)
    
    return numUnique




def solve(isConnected):
    n = len(isConnected)
    seen = set()

    def dfs(i):
        if i in seen:
            return
        seen.add(i)
        for j in range(n):
            if isConnected[i][j]:
                dfs(j)

    numProvinces = 0
    for i in range(n):
        if i not in seen:
            numProvinces += 1
            dfs(i)
    
    return numProvinces






"""

https://leetcode.com/problems/find-eventual-safe-states/

directed graph n nodes
- 0 to n-1
adjacency matrix

terminal node - no outgoing
safe node - every path from node leads to a terminal node or another safe node

- return list of safe nodes, ascending order

- alternative is a loop. 

Ideas: 
Brute force, run a dfs from each node and if there's a loop or you reach an unsafe node, all those nodes are unsafe.
- if you ever reach an unsafe node, you are unsafe

time: O(n^2)
Space: O(n) store visited / unsafe nodes

"""

def solve(graph):
    # init state
    n = len(graph)
    isUnsafe = [False for _ in range(n)]
    visited = set()
    finished = set()

    def dfs(visited, isUnsafe, node):

        # first check cache
        if isUnsafe[node]:
            return True

        if node in visited: # means you have a loop
            isUnsafe[node] = True
            return True
        
        # else no loop, so continue
        visited.add(node)
        for next in graph[node]:
            if dfs(visited, isUnsafe, next): # if unsafe
                isUnsafe[node] = True
                finished.add(node)
                visited.remove(node)
                return True

        visited.remove(node)
        finished.add(node)
        return False
    
    for start in range(n):
        if start in finished: continue
        dfs(visited, isUnsafe, start)
    
    return [x for x in range(n) if isUnsafe[x] == False]

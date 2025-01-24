"""

802. Find Eventual Safe States


given adjacency list

Ideas:
- start search from terminal nodes and expand
    - use queue? push new nodes to front, and if can't, push to back
    - may not be optimal choice
    - once do 1 pass and no nodes can be added, terminate

could be O(n^2) time for that

Alt: dfs with cache?
- do dfs from each node
- cache results? either safe or unsafe
- O(n) time?

Track visited nodes and safe nodes

Tactic:
DFS with cache. Keep visiting, safe and unsafe sets.

"""

def solve(adj):

    visiting = set()
    safe = set()
    unsafe = set()

    def dfs(curr):
        nonlocal visiting
        nonlocal safe
        nonlocal unsafe

        # Check cache
        if curr in safe:
            return True
        elif curr in unsafe:
            return False

        # If loop
        if curr in visiting:
            unsafe.add(curr)
            return False

        visiting.add(curr)

        # If any neighbour is unsafe, fail
        for neigh in adj[curr]:
            if not dfs(neigh): # if unsafe
                unsafe.add(curr)
                return False

        visiting.remove(curr)
        
        # Must be safe
        safe.add(curr)
        return True
    
    for node in range(len(adj)):
        dfs(node)
    
    return sorted(list(safe))






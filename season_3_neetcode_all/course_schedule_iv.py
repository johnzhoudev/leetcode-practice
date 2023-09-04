"""

https://leetcode.com/problems/course-schedule-iv/

numCoureses, 0 to n-1
prerequisites, a, b means take a before b
queries u, v
- answer if u is a prereq of v or not

Ideas:

Graph theory, directed graph, if search from u finds v, it.

DFS?

Could also keep a cache. set of all courses discoverable from u
or do dfs from each course, to build up all courses discoverable...

DFS with cache is my best bet. on each iteration, check cache to see if explored yet...
update cache when exploring unexplored node

if you find a node before, you can stop exploring and keep that node marked as unexplored...
    no...or mark nodes as finished. else must check all neighbours...
so can just return

Fuck it, just write default dfs and cache specificall if you've found or not what you're looking for

Better: just find all reachable from all, and set union? Maybe a little more efficient 
because since you don't have to break early, easier to just get all the results. And the copying 
/ union isn't that bad. In other soln, you're only caching the found node, so work is going to waste.

- in og version, end state would be a total map of what is reachable and what is not. so everything copied 
anyway. Might as well do it more efficiently with better way.


Tactic: DFS, but keep reachable sets for each node and set union / return copies during DFS. global visited (don't rpt), and search from each node before answering

"""
from collections import defaultdict

def solve(n, prereq, queries):
    # setup cache
    reachable = defaultdict(set)
    adjList = defaultdict(lambda: set())
    for a, b in prereq:
        adjList[a].add(b) # take a before b

    visited = set() # global, don't re-search the same node again
    def dfs(node, visited):
        if node in visited:
            return reachable[node].copy()
        
        visited.add(node)
        for next in adjList[node]:
            reachable[node].add(next)
            reachable[node] = reachable[node].union(dfs(next, visited))
        
        return reachable[node].copy()
    
    for node in range(n):
        dfs(node, visited)
    
    return [v in reachable[u] for u, v in queries]


from collections import defaultdict

def solve(n, prereq, queries):
    # setup state
    reachable = defaultdict(lambda: set()) # dict between course and set of courses 
    unreachable = defaultdict(lambda: set())
    adjList = defaultdict(lambda: set())
    for a, b in prereq:
        adjList[a].add(b) # take a before b

    # now write dfs
    def dfs(u, v, visited):
        # first check caches
        if v in reachable[u]:
            return True
        elif v in unreachable[u]:
            return False
        
        # now do dfs
        # if found, else continue
        if u == v:
            reachable[u].add(v)
            return True
            
        for next in adjList[u]:
            if next in visited:
                continue
            visited.add(next)

            if dfs(next, v, visited): # found, break early
                reachable[next].add(v)
                return True

            visited.remove(next)
        
        unreachable[u].add(v)
        return False

    outputs = []

    for u, v in queries:
        if u in reachable and v in reachable[u]:
            outputs.append(True)
        elif u in unreachable and v in unreachable[u]:
            outputs.append(False)
        else:
            outputs.append(dfs(u, v, set()))
    
    return outputs
            

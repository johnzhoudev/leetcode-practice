"""
https://leetcode.com/problems/course-schedule-ii/

numcourses
prereq map
after, before

return ordering to finish all courses

Ideas
- can't with dfs? doesn't get you the ordering
- can do search alg, indegree outdegree
- if impossible = loop, never degree 0

Ideas 2:
could also use dfs. Idea is to build the array in reverse, using finishing order. due to nature of dfs, if you finish visiting smth, means explored all after.
- so thus you can do it.
- also if you detect a loop, ret

"""
from collections import defaultdict

def solveDFS(numCourses, prereqs):

    # first build adj list and deg0 starts
    adj = defaultdict(list)
    deg0 = set(range(numCourses))
    for after, before in prereqs:
        adj[before].append(after)
        if after in deg0: deg0.remove(after)

    path = []
    added = set()

    # returns true if fine, false if fail
    def dfs(node, visited):
        if node in visited:
            return False # loop
        
        visited.add(node)

        for next in adj[node]:
            if not (dfs(next, visited)): # if loop found, break early
                return False
        
        visited.remove(node)
        # since finished, add node
        if node not in added:
            path.append(node) # careful, could add twice
            added.add(node)
        return True
    
    # now need to dfs each 0 indegree
    for start in deg0:
        if not dfs(start, set()): # has loop
            return []
        
    if len(path) != numCourses:
        return []
    
    path.reverse()
    return path










def solveIndegreeBFS(numCourses, prereqs):
    # first build indegree map and deg 0 set
    indegree = defaultdict(lambda : 0)
    adj = defaultdict(list)

    for after, before in prereqs:
        indegree[after] += 1
        adj[before].append(after)
    
    validCourses = []
    for node in range(numCourses):
        if indegree[node] == 0:
            validCourses += [node]
        
    order = []
    while validCourses:
        course = validCourses.pop()
        order.append(course)
        for next in adj[course]:
            indegree[next] -= 1
            if indegree[next] == 0:
                validCourses.append(next)
    
    for val in indegree.values():
        if val != 0: return []
    
    return order

"""

https://leetcode.com/problems/course-schedule/

numCourses
prereqs - a, b => take b before a
Return true if can finish all courses, else false

Basically, topological sort = no loops

- dfs at each node, never revisit a node during the search.
    - if there was a loop, would revisit node
    - if you see a node from outside the loop, end. cannot loop around else would have found earlier.
    so O(n)

- careful, to detect loops could have diamond case. so need to pop off the visited queue. loop only if you return to your current path, not all visited

Better: 
"""

from collections import defaultdict

def solve(numCourses, prereqs):
    # make adjacency lists
    adj = defaultdict(set)
    for after, before in prereqs:
        adj[before].add(after)

    seen_outside_loop = set()
    def dfs(curr, visited):
        if curr in visited:
            return False # has loop
        elif curr in seen_outside_loop:
            return True # fine

        visited.add(curr)
        for next in adj[curr]:
            if dfs(next, visited) == False:
                return False
        visited.remove(curr)
        seen_outside_loop.add(curr) # after exploring a node, if all good, mark as good
        return True
        
    for course in range(numCourses):
        visited = set()
        if dfs(course, visited) == False:
            return False
    
    return True



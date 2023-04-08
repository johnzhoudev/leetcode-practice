"""

https://leetcode.com/problems/course-schedule-ii/

- same as course schedule, courses 0-num-1
- return order of courses to take, any order


- Asking for a topological sort

Ideas
- create pseudo node that will travel to all nodes - then we can start here


- keep track of prereq's completed / added list
- once all prereqs completed, during dfs traversal, then can add that course

- Do a dfs and only add courses to output if all prereqs satisfied
    - also keep an "added" set and short circuit 

- at end, check all courses are added. else have cycle, then return []

Time: O(n), each node processed exactly once
Space: O(n^2), keeping track of prerequisite map / adjacency list

Tactic: Topological sort. do dfs, with visited, processed sets and prereqCount. only advance in dfs if prereq = 0. If didn't process all courses, cycle.

Idea2: Indegree BFS topological sort may be easier.
"""

def solve(numCourses, prerequisites):
    

def solve(numCourses, prerequisites):
    # make adjacency lists / prereq map
    adj = {}
    # prereq = {}
    prereq = [0 for _ in range(numCourses)]

    for x in range(numCourses):
        adj[x] = set()
    for t, f in prerequisites:
        adj[f].add(t)
        prereq[t] += 1
    
    output = []
    processed = set()

    # return True if cycle
    def dfs(node, visited):
        nonlocal output
        nonlocal processed

        if node in visited:
            return True
        
        # already handled only for base 
        if node in processed:
            return False

        # still need to process prerequisites
        if prereq[node] != 0:
            return False
        
        # finished processing prerequisites, can continue
        # only reach here when we can actually take the course
        output.append(node)
        processed.add(node)
        visited.add(node)
        for nextNode in adj[node]:
            prereq[nextNode] -= 1
            if dfs(nextNode, visited):
                return True # short circuit
        visited.remove(node)
        return False
    
    for x in range(numCourses):
        dfs(x, set())

    if len(processed) == numCourses:
        return output
    return []




        

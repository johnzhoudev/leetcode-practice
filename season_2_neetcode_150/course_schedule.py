# Results:
# Runtime: 96ms 82.61%
# Memory Usage: 17.5MB 9.96%

"""

https://leetcode.com/problems/course-schedule/

courses 0 to numc - 1
- have to take 1 course before another
- can you take all courses?

- Can only take a course once you've satisfied prerequisites
    - could have multiple courses be a prerequisite

- must be a DAG? If there is a loop, cannot complete?

- map of course to prerequisite set
- map prerequisite to courses
- start at all courses that don't have prerequisites
- mark as done
- try and add courses that follow the prerequisite

When is it impossible?
- if DAG has a cycle. Else if dag, then can take all. so just have to construct graph and see if there's a cycle.
- Cycle detection algs?

O(n)


time limit exceeded, so now need to maintain meta seen set for dp

Tactic: Equivalent to checking DAG (topological sort). DFS, make sure no cycle. Then if done, mark node as meta-seen since if you hit again, you know it's a dag. Pro tip use array to store multi info
"""

def solve(numCourses, prerequisites):

    prereqMap = {}
    for x in range(numCourses):
        prereqMap[x] = []

    for f, t in prerequisites:
        prereqMap[f].append(t)
    
    # return true if found cycle, else false
    def dfs(node, seen):
        nonlocal prereqMap
        nonlocal isDag

        if node in isDag:
            return False

        if node in seen:
            return True
        
        seen.add(node)
        for nextNode in prereqMap[node]:
            if dfs(nextNode, seen):
                return True
        # not found
        seen.remove(node)

        # if determine false, is dag already
        isDag.add(node)
        return False
    
    isDag = set()
    for x in range(numCourses):
        if dfs(x, set()):
            return False
    return True
    



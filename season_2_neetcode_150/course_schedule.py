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


"""

def solve(numCourses, prerequisites):

    prereqMap = {}
    for x in range(numCourses):
        prereqMap[x] = []

    for f, t in prerequisites:
        prereqMap[f].append(t)
    
    # return true if found cycle, else false
    def dfs(node, seen, isFound=False):
        nonlocal prereqMap

        if node in seen:
            return True
        
        seen.append(node)
        for nextNode in prereqMap[node]

        






    for x in range(numCourses):

    


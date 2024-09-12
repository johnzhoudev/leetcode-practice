"""

0 to numCourses - 1
prereq a b - take b before a

true if can finish all courses, else false

any loops?
limits on all numbers?

Ideas:
- need to topographic sort this graph, basically
- if able to, then can take all. else cannot
- graph of prerequisite chains
- courses with no incoming, start dfs there
- do dfs and see if you hit all courses

O(n) time

- first make adj graph of dependencies
- scan and log all nodes without incoming dependencies
    - keep counter of prereqs for each course. when reduced to 0, can take
- start search, 
- at end, check to see if all good

Tactic: Check if DAG (topological sort). Can do with indegree magic, and dfs. Checking for loops works too, see older version.
- I like indegree better
"""

from collections import defaultdict

def solve(numCourses, prereqs):

    adjList = [[] for _ in range(numCourses)]
    isDag = set()

    # populate adjList
    for a, prereq in prereqs:
        adjList[prereq].append(a)

    # check if cycle, true, else false (dag)
    def dfs(node, visited):
        nonlocal isDag
        nonlocal adjList

        if node in isDag:
            return False

        if node in visited:
            return True
        
        visited.add(node)
        for neigh in adjList[node]:
            if dfs(neigh, visited):
                return True # found cycle
        # is a dag!
        visited.remove(node)
        isDag.add(node)
        return False
    
    for course in range(numCourses):
        if dfs(course, set()):
            return False
    
    return True



def solve(numCourses, prereqs):

    adjList = [[] for _ in range(numCourses)]
    coursesWithNoPrereq = set(range(numCourses))
    prereqCounter = defaultdict(lambda : 0)

    # populate
    for course, prereq in prereqs:
        adjList[prereq].append(course)
        if course in coursesWithNoPrereq: coursesWithNoPrereq.remove(course)
        prereqCounter[course] += 1
    
    # add nodes without dependencies
    state = list(coursesWithNoPrereq)
    coursesTaken = 0

    while state:
        curr = state.pop()
        coursesTaken += 1
        for nextCourse in adjList[curr]:
            prereqCounter[nextCourse] -= 1
            if prereqCounter[nextCourse] == 0:
                state.append(nextCourse)
    
    # check if all courses taken
    return coursesTaken == numCourses






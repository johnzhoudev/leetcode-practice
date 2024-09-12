"""

return an ordering of courses that you sould take to complete
easy, topological sort!

if none, return empty array

tactic: Topological sort! Use indegree
"""


from collections import defaultdict
def solve(numCourses, prereqs):

    adjList = [[] for _ in range(numCourses)]
    indegree = defaultdict(lambda : 0)

    for a, prereq in prereqs:
        adjList[prereq].append(a)
        indegree[a] += 1
    
    state = []
    for course in range(numCourses):
        if indegree[course] == 0:
            state.append(course)

    sortedCourses = []

    while state:
        course = state.pop()
        sortedCourses.append(course)

        for neigh in adjList[course]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                state.append(neigh)
    
    return sortedCourses if len(sortedCourses) == numCourses else []
    

    


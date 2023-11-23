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


"""

def solve(numCourses, prereqs):

    visited = set()
    def dfs(curr):
        if curr in visited:
            return False # has loop

        visited.add(curr)

        for j in range(numCourses):
            if j == curr: continue
            dfs


    # for course in range(numCourses):



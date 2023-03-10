# Results:
# Runtime: 44ms 59.48%
# Memory Usage: 15.3MB 89.92%

"""

https://leetcode.com/problems/maximum-depth-of-binary-tree/

given root, print max depth

Idea:
- iterative, push node and curr depth. 
- keep running max
O(n) time
O(2^h) space, since max all nodes per level

Tactic: store node + currDepth in state, iterative
"""

def solve(root):
    state = [(root, 0)]
    maxDepth = 0

    while state:
        node, currDepth = state.pop() # currDepth not including node
        if node:
            currDepth += 1
            maxDepth = max(maxDepth, currDepth)
            state += [(node.left, currDepth), (node.right, currDepth)]
    return maxDepth
    


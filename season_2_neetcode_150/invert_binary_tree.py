# Results:
# Runtime: 30ms 80.53%
# Memory Usage: 13.8MB 94.56%

"""

https://leetcode.com/problems/invert-binary-tree/

- given root, invert tree

Idea:
- recursive, for each node, left = invert right, right = invert left
O(n) time, process each node once

- Iterative, push nodes to be inverted

Tactic: Iterative, push nodes onto stack to be reversed

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    state = [root]

    while state:
        node = state.pop()
        if node:
            temp = node.left
            node.left = node.right
            node.right = temp
            state += [node.left, node.right]
    
    return root
        



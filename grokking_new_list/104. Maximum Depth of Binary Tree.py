"""

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


- get max depth
- do dfs, keep track of max depth - better for memory?
- or do bfs, see how far you get

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if not root:
        return 0

    nodes = []
    nodes.append((1, root))
    max_depth = 1

    while nodes:
        depth, curr = nodes.pop()
        max_depth = max(depth, max_depth)
        if curr.left:
            nodes.append((depth + 1, curr.left))
        if curr.right:
            nodes.append((depth + 1, curr.right))
    
    return max_depth
        




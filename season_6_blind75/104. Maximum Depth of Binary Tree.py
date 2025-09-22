
"""

dfs?

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if not root:
        return 0

    stack = [(root, 1)]
    best = 1
    while stack:
        node, depth = stack.pop()
        if not node: continue # Skip
        best = max(best, depth)
        stack.append((node.left, depth + 1))
        stack.append((node.right, depth + 1))
    return best



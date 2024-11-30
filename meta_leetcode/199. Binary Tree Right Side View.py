"""

199. Binary Tree Right Side View

- right side of binary tree
- do a bfs, and keep a stack of the nodes from left to right.
- then emit the top of the stack.

O(n) time
O(n) space

Tactic:
BFS easiest. But could also do dfs with level? Then if level visited already, don't emit. Must go right each time

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if root is None: return []
    stack = [root]
    output = []

    while stack:
        output.append(stack[-1].val)

        # now advance all nodes on stack
        nextStack = []
        for node in stack:
            if node.left: nextStack.append(node.left)
            if node.right: nextStack.append(node.right)
        stack = nextStack
    
    return output


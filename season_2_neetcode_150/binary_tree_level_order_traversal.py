# Results:
# Runtime: 40ms 39.7%
# Memory Usage: 14MB 98.14%

"""

https://leetcode.com/problems/binary-tree-level-order-traversal/

Level order traversal

Ideas:
- just go level by level like a BFS. and use for loop to figure out which level it's at

Tactic: Go by level, cound number of items. careful if you include Nones and len(row) == 0, don't append
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def solve(root):
    output = []
    state = deque()
    state.append(root)

    while state:
        n = len(state)
        row = []
        for _ in range(n):
            node = state.popleft()
            if node is None: continue
            row += [node.val]
            state.append(node.left)
            state.append(node.right)
        if len(row) > 0: output += [row]

    return output

    
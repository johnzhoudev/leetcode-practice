# Results:
# Runtime: 29ms 89.73%
# Memory Usage: 13.9MB 59.82%

"""

https://leetcode.com/problems/binary-tree-right-side-view/

Idea:
- dfs, prioritize going right, first node you see at a level is the rightmost node.
Time: O(n), Space: O(n)

Tactic: dfs, prioritize going right, first node you see at a level is the rightmost node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    result = []
    state = [(root, 0)]

    while state:
        node, height = state.pop()
        if node is None:
            continue

        if height >= len(result):
            result += [node.val]
        state += [(node.left, height + 1), (node.right, height + 1)]
    
    return result
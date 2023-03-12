# Results:
# Runtime: 50ms 78.92%
# Memory Usage: 18.5MB 98.41%

"""

https://leetcode.com/problems/balanced-binary-tree/

- depth of subtrees never differs by more than one

Idea:
- recursive get subtree depth, and compare on each level left and right. return false immediately, else return true.
- kind of like a postorder traversal, recursive
O(n) time

Tactic: recursive post order traversal, return -1 if failed. Can do iterative, but harder, and have to keep map of nodes.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):

    def checkDepth(node):
        if node is None: return 0
        left = checkDepth(node.left)
        if left == -1: return -1
        right = checkDepth(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1
    
    return checkDepth(root) != -1
        


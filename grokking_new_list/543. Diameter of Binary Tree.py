"""


543. Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/description/

Idea:
- length is max depth left side and max depth right side, max over all nodes
- recursive func giving max length left, right, and best thru it or under it

Tactic: Get longest in each dir. keep nonlocal global var of max path and update it for each node.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search(node): # returns (max branch, max itself or under)
    if not node: return -1, -1
    maxLeftBranch, maxLeft = search(node.left)
    maxRightBranch, maxRight = search(node.right)
    
    maxBranch = max(maxLeftBranch, maxRightBranch) + 1
    maxValue = max(maxLeft, maxRight, maxLeftBranch + maxRightBranch + 2)
    return maxBranch, maxValue

def solve(root):
    maxBranch, maxValue = search(root)
    return maxValue



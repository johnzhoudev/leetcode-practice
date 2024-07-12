"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/

- return right side view

Ideas:
- bfs, just return rightmost item

O(n) time, O(width) space

Tactic: Do BFS
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
  if not root:
    return []
  
  # do traversal
  output = []
  nodes = [root]
  while nodes:
    output.append(nodes[-1].val)
    nextNodes = []
    for node in nodes:
      if (node.left):
        nextNodes.append(node.left)
      if (node.right):
        nextNodes.append(node.right)
    nodes = nextNodes
  
  return output

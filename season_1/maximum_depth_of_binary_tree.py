# Results:
# Runtime: 61ms 59.37%
# Memory Usage: 15.1MB 98.68%

"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

longest path - num nodes from root to furthest leaf

Ideas:
- DFS
- iterative method: use stack and push children and size.

DFS vs BFS? Well, dfs maybe better since you may reach furthest...? no. need to go thru all anyway.

TODO: 
- recursive version?

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth1(root):

	if (root is None): return 0

	# init stack
	nodeStack = [(root, 1)] # stores root, depth
	maxDepth = 1

	while (len(nodeStack) != 0):
		node, depth = nodeStack.pop()
		if (depth > maxDepth): maxDepth = depth
		if (node.left): nodeStack.append((node.left, depth + 1))
		if (node.right): nodeStack.append((node.right, depth + 1))
	
	return maxDepth









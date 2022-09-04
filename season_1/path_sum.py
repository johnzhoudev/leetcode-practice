# Results:
# Runtime: 74ms 36.96%
# Memory Usage: 15.1MB 56.74%

"""
https://leetcode.com/problems/path-sum/

Root to leaf path equaling target sum

Ideas:
- need to visit all nodes basically. DFS, so we can store the path sum along the path.
- Iterative dfs, push node and currSum onto stack
Time: O(n)
Space: O(n) or O(num leaves) worst case
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum1(root, targetSum):
	if (root is None):
		return False
	
	# DFS init stack
	dfsStack = []
	dfsStack.append((root, root.val))

	# loop
	while (len(dfsStack) != 0):
		node, currSum = dfsStack.pop()
		if (node.left is None and node.right is None and currSum == targetSum):
			return True
		
		if (node.left):
			dfsStack.append((node.left, currSum + node.left.val))
		if (node.right):
			dfsStack.append((node.right, currSum + node.right.val))
	
	return False # found none






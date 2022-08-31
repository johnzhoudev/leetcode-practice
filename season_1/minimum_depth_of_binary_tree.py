# Results:
# Runtime: 571ms 92.78%
# Memory Usage: 49.3MB 87.09%

"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Idea:
BFS - find min fastest - basically first time you find a leaf - that's the height
time: O(n) worst case
space: O(n) stack?
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minBSTDepth(root):
	if (root is None): return 0

	# init state - use a queue
	state = []
	state.append(root)
	height = 1 # height of root
	while (len(state) != 0):
		nextLevel = []
		
		# for each node in the level
		for node in state:
			if (node.left is None and node.right is None): return height
			if (node.left): nextLevel.append(node.left)
			if (node.right): nextLevel.append(node.right)
		
		state = nextLevel
		height += 1
	
	raise Exception("Logical error - should not reach here")

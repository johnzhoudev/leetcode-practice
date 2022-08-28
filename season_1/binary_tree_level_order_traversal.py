# Results:
# Runtime: 50ms 62.10%
# Memory Usage: 14.3MB 27.54%

"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Level order traversal of nodes
- output array of each level

Ideas:
- Maintain a queue, and push items with their level.
Time: O(n)
Space: O(n)
- Is there a way to do this without recording level? Maybe not easily.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def levelOrderTraversal(root):

	if (root is None):
		return []

	# create queue
	nodesQueue = deque()
	nodesQueue.append((root, 0))
	levelResponse = []
	currentLevel = 0
	response = []

	# while queue is not empty, pop one, add to response, and add children if exists with current level += 1
	while (len(nodesQueue) != 0):
		(node, level) = nodesQueue.popleft()

		if (level == currentLevel):
			levelResponse += [node.val]
		else:
			# New level, so append and reset levelResponse and currentLevel
			response += [levelResponse]
			levelResponse = [node.val]
			currentLevel = level
		
		if (node.left):
			nodesQueue.append((node.left, level + 1))
		if (node.right):
			nodesQueue.append((node.right, level + 1))
	
	# Once done, add final level response
	response += [levelResponse]

	return response

print(levelOrderTraversal(TreeNode(3)))
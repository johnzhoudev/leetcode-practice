# Results:
# Runtime: 36ms 89.23%
# Memory Usage: 14.1MB 58.19%

"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

zigzag traversal. Go left to right, then right to left, and so on.

Ideas:
- again, maintain deque. - circular array, resize when necessary. insert / del O(1) amortized.
- keep direction vector that swaps each level, so you remove items in a different order
- keep track of level / level count OR make a new deque

Time: O(n)
Space: O(n)

Tactic: Use a deque, and adjust how you add and traverse the nodes on each level. Can know which level node is by handling all in 1 level at same time.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Direction:
	LEFT = 0
	RIGHT = 1

def zigzagLevelOrderTraversal(root):

	if (root is None):
		return []

	# init deque
	nodesDeque = deque()
	nodesDeque.append(root)
	res = []
	direction = Direction.RIGHT # start with going RIGHT

	# for each level, go thru and add (direction according) to levelRes, and append children in same direction.
	while (len(nodesDeque) != 0):
		# init deque for next level
		nextNodeDeque = deque()
		levelRes = []

		# go thru in correct direction, pop node, add to level res, and add children in same direction
		while (len(nodesDeque) != 0):
			if (direction == Direction.RIGHT):
				node = nodesDeque.popleft()
				levelRes += [node.val]
				if (node.left):
					nextNodeDeque.append(node.left)
				if (node.right):
					nextNodeDeque.append(node.right)
			else:
				node = nodesDeque.pop()
				levelRes += [node.val]
				# add right first
				if (node.right):
					nextNodeDeque.appendleft(node.right)
				if (node.left):
					nextNodeDeque.appendleft(node.left)
		nodesDeque = nextNodeDeque
		res += [levelRes]
		direction = 1 - direction

	return res
			

			


		




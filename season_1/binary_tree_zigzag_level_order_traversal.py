# Results:
# Runtime: 49ms 57.27%
# Memory Usage: 14.1MB 58.19%

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

Alternatives:
- double stack - popping and adding implicitly reverses!
- DFS - process node, then search left, then right. will always append nodes to correct levels from left to right!
- Same soln, but more efficiently, make levelRes a specific size and insert using array indices. Better than 
having multiple cases for popping and pushing items

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
		levelRes = [None for _ in range(len(nodesDeque))]

		# go thru in correct direction, pop node, add to level res, and add children in same direction
		for i in range(len(nodesDeque)):
			node = nodesDeque.popleft()

			if (direction == Direction.RIGHT):
				levelRes[i] = node.val
			else:
				levelRes[-1 - i] = node.val

			if (node.left):
				nextNodeDeque.append(node.left)
			if (node.right):
				nextNodeDeque.append(node.right)

		nodesDeque = nextNodeDeque
		res += [levelRes]
		direction = 1 - direction

	return res
			

			


		




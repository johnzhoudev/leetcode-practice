# Results:
# Runtime: 120ms 63.22%
# Memory Usage: 15.6MB 31.81%

"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Nums sorted in ascending order
convert to height balanced binary tree

Idea:
- add middle and recurse on left and right sides. 
Time: O(n)
space: O(n) for iterative?
- iterative solution: push parent, left and right. OR, some implicit ordering?
	- push parent, isleft / isright, and array indices
- Easier: recursive solution?

Max Recursion Depth!

New Idea: Iterative
- need to store parent, left or right, and array indices

Tactic: Watch for infinite loops. Median calc s + (e-s) // 2. Also watch when using exclusive end!
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def print(self):
      print(self.val)
      if (self.left): self.left.print()
      if (self.right): self.right.print()


# Error: Time Limit Exceeded
# iterative
def sortedArrayToBST2(nums):
	# create state
	state = [] # store (node, isLeft boolean, start, end (exc))
	dummyNode = TreeNode()
	state.append((dummyNode, True, 0, len(nums))) # appends to left node, so return dummy.left

	while (len(state) != 0):
		node, isLeft, start, end = state.pop()

		if (end - start <= 0): continue # do / append nothing

		# create new node
		# get median
		middleIndex = start + (end - start) // 2
		newNode = TreeNode(nums[middleIndex])
		if (isLeft):
			node.left = newNode
		else:
			node.right = newNode
		
		# add new state
		state.append((newNode, True, start, middleIndex)) # nopt including middleIndex
		state.append((newNode, False, middleIndex + 1, end))

	return dummyNode.left

# ERROR: Max recursion depth exceeded
def createNode(nums, start, end): # end not inclusive
	if (end - start <= 0): return None

	# get median
	middleIndex = start + (end - start) // 2

	node = TreeNode(nums[middleIndex])
	node.left = createNode(nums, start, middleIndex)
	node.right = createNode(nums, middleIndex + 1, end)
	
	return node

def sortedArrayToBST1(nums):
	return createNode(nums, 0, len(nums))
	

sortedArrayToBST1([1, 2, 3]).print()


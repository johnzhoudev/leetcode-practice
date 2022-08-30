# Results:
# Runtime: 323ms 23.34%
# Memory Usage: 19MB 70.37%

"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

preorder and inorder traversal
construct the binary tree

Ideas:
- Recursive soln:
	- get root from preorder
	- from inorder, can tell what's on left and right
	- create subarrays and continue.
Time: O(n^2) time to find root, create subarrays, etc.
Space: implicitly store array indices in function calls, O(n)?

- Iterative soln?
	- push array indices onto a stack
	- how will we know which node to build it off? need to also store nodes. too complex. recursive soln?
Space: O(n)

TODO:
Improve speed with hashmap!!! map value to index to make search constant time
- 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildNode(preorder, inorder, preorderStart, preorderEnd, inorderStart, inorderEnd): # ends exclusive
	# First, if no nodes, return None
	if (preorderEnd - preorderStart <= 0): return None

	# first, get root from preorder
	root = TreeNode(preorder[preorderStart])

	# find root index in inorder
	inorderRootIndex = inorderStart
	while (root.val != inorder[inorderRootIndex]):
		inorderRootIndex += 1
	
	numNodesOnLeft = inorderRootIndex - inorderStart

	# now make left and right recursively
	root.left = buildNode(preorder, inorder, preorderStart + 1, preorderStart + 1 + numNodesOnLeft, inorderStart, inorderStart + numNodesOnLeft)
	root.right = buildNode(preorder, inorder, preorderStart + 1 + numNodesOnLeft, preorderEnd, inorderStart + numNodesOnLeft + 1, inorderEnd)
	return root


def buildTree1(preorder, inorder):
	return buildNode(preorder, inorder, 0, len(preorder), 0, len(inorder))










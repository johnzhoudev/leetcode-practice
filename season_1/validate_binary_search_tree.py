# Results:
# Runtime: 52ms 84.47%
# Memory Usage: 17.1MB 15.39%

# Results:
# Runtime: 68ms 55.45%
# Memory Usage: 17MB 15.39%

"""
https://leetcode.com/problems/validate-binary-search-tree/

given root
is valid? -> left valid, right valid, left all less, right all greater

Brute Force / Immediate thinking:
- Recursive
- left and right both valid
- get min from right, get max from left, compare to node
- but recursively, min = min from left, max = max from right. so O(1) to return
Time: 
T(n) = 2T(n/2) + O(n/2) to find max / min = O(n log n)

Better:
O(n) time
- Recursive subroutines to check left and right both valid, but get min from left and max from right
- check middle node is between min and max
- then good.
- each node checked exactly once
- O(1) time per node, since to get max we just get max of right, and min of left. easy
- T(n) = 2T(n/2) + O(1) = O(n) time

TODO: Iterative solution

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# returns (t/f, min, max)
def valBSTHelper(root):
	# Base cases
	if (root is None):
		return [True, float("inf"), float("-inf")] # will be valid for all comparisons checking validity
	else:
		leftValid, leftMin, leftMax = valBSTHelper(root.left)
		rightValid, rightMin, rightMax = valBSTHelper(root.right)
		isRootValid = leftMax < root.val and root.val < rightMin

		# Have to handle if left and right are none, so mins are +- inf
		return [leftValid and rightValid and isRootValid, leftMin if root.left else root.val, rightMax if root.right else root.val]

	# else (root.left is None and root.right is None):
	# 	return [True, root.val, root.val]
	# elif (root.left is None):
		
def valBinarySearchTree(root):
	return valBSTHelper(root)[0]

testBST1 = TreeNode(1)
testBST2 = TreeNode(2, testBST1, testBST1)
print(valBinarySearchTree(None))
print(valBinarySearchTree(testBST1))
print(valBinarySearchTree(testBST2))

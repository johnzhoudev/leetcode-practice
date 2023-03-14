# Results:
# Runtime: 44ms 95.15%
# Memory Usage: 18MB 81.44%

"""

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Idea: 
- in order traversal, and keep count
- yeah, have to check / traverse, else how would you know this is min?
- how to do iteratively?
- recursive better

Idea2: It's possible to do iteratively

Tactic: Inorder traversal. Recursive easy, but there is an iterative way. go left as much as you can, root on stack. process curr, then set root to right.

"""

# Intuition: process left, sure. Then once last right most thing is processed, root = root.right is null and you can pop again.
def solveIterative(root, k):
    stack = []
    while True:
        # Process left by going as left as you can
        while root:
            stack += [root]
            root = root.left
        root = stack.pop() # no left, so process node
        k -= 1
        if k == 0: return root.val
        root = root.right # Now process right, same way


def solve(root, k):

    # Returns (isFound, num Processed) or (True, kth val)
    def traverse(node, numProcessed): # count is number of nodes processed before this node, haven't traversed left yet
        if node is None: return None, numProcessed

        isFound, numProcessed = traverse(node.left, numProcessed)
        if isFound: return isFound, numProcessed

        numProcessed += 1
        if numProcessed == k:
            return True, node.val
        else:
            # process right
            return traverse(node.right, numProcessed)
    
    return traverse(root, 0)[1]






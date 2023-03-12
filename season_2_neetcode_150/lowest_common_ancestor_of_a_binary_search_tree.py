# Results:
# Runtime: 65ms 99.35%
# Memory Usage: 18.7MB 58.49%

"""

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

- given 2 nodes, find lowest common ancestor
- lowest node in tree that has p and q as descendants
- a node is a descendant of itself

Idea:
- all ancestors can be found in a search for the two nodes
- can search from root, and as soon as they differ, previous one is the lowest common ancestor
    - could also be when they find the node
O(log n) time

Tactic: search for both, as soon as on two sides or found, that's the LCancestor

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solve(root, p, q):
    
    while True:
        assert(root)

        if root == p or root == q:
            return root
        
        if root.val < p.val and root.val < q.val:
            root = root.right
        elif root.val > p.val and root.val > q.val:
            root = root.left
        else:
            return root.val # this is where it differs

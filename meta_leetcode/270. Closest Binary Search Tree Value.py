"""

270. Closest Binary Search Tree Value

when searching, at a certain node, 
- lets say you reach a node
- and x is on one side of it. 
- either the answer is on that side, or it's that node value since everything on other side will be 
less or greater
- or a parent.

So each step, keep distance with parent and continue

Tactic:
Do a regular search, keep track of best dist with nodes seen. 

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root, target):

    def dist(a, b):
        return abs(a - b)

    # root guaranteed to be good
    bestDist = dist(root.val, target)
    best = root.val

    def search(node, target):
        nonlocal bestDist
        nonlocal best

        if not node: return

        # compare against best
        d = dist(node.val, target)
        if d < bestDist:
            best = node.val
            bestDist = d
        elif d == bestDist and node.val < best:
            best = node.val
        
        # now go left or right
        if target < node.val:
            search(node.left, target)
        elif target > node.val:
            search(node.right, target)
        else:
            return node.val # equal
    
    search(root, target)
    return best


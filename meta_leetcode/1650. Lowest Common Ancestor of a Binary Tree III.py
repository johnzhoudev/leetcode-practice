"""

1650. Lowest Common Ancestor of a Binary Tree III


given 2 nodes, print lowest common ancestor

- one of the parents they encounter will be the right one
- just make set of all encounterd with 1, and check other?

O(h) time O(h) space complexity

- maybe just advance both at a time? could reduce a bit

O(1) space
- once get to root, just switch. 
- then will converge at parent

Tactic:
Advance both at same time, once nullptr, switch to opposite start. => Meet at correct point.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def solve(p, q):
    pStart = p
    qStart = q

    while p and q:
        if p == q: return p
        p = p.parent
        q = q.parent

        if p is None: p = qStart
        if q is None: q = pStart
    
    raise RuntimeError()

def solve(p, q):
    pValues = set()

    while p:
        pValues.add(p)
        p = p.parent
    
    while q:
        if q in pValues:
            return q
        q = q.parent
    
    raise RuntimeError()

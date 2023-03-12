"""

https://leetcode.com/problems/same-tree/

structurally identicial, nodes have same value

Idea: do iterative traversal, push same nodes at same time. if they differ, return false

Tactic: do any traversal, but keep track of both nodes. if differ, return false. careful of None case.

"""

def solve(p, q):
    state = [(p, q)]
    while state:
        pnode, qnode = state.pop()

        if (pnode is None or qnode is None):
            if pnode != qnode:
                return False
        elif pnode.val != qnode.val:
            return False
        else:
            state += [(pnode.left, qnode.left), (pnode.right, qnode.right)]
    
    return True
            
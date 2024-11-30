"""

236. Lowest Common Ancestor of a Binary Tree

no parent pointer

idea:
- dfs to find 1, remember stack
- dfs to find 2, remember stack
- add all to set, pop from other until found

O(n) time O(h) space

Other idea:
- recursive alg, 
- Idea is the parent is the only one where both the left and right branches 
will contain either of the nodes.
    - will never contain both
    - could contain neither

- so just search 


Tactic:
Fancy way: recurse left and right, return p or q if found. LCP is only node where one found in left and one in right!
Otherwise, dfs with stack. Then turn stack to set and check other stack.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solve(root, p, q):

    if root is None:
        return None
    
    # found one
    if root == p or root == q:
        return root
    
    left, right = None, None

    if root.left:
        left = solve(root.left, p, q)
    if root.right:
        right = solve(root.right, p, q)
    
    if left and right: # found LCP
        return root
    else:
        return left or right # return which one is legit
    
def solve(root, p, q):

    def dfs(node, target, stack):

        if not node:
            return False

        stack.append(node)

        if (node == target):
            return True
        
        if dfs(node.left, target, stack):
            return True
        elif dfs(node.right, target, stack):
            return True
        stack.pop()
        return False
    
    pstack = []
    qstack = []

    assert(dfs(root, p, pstack))
    assert(dfs(root, q, qstack))

    if len(pstack) > len(qstack):
        temp = pstack
        pstack = qstack
        qstack = temp
    
    pset = set(pstack)
    while qstack:
        if qstack[-1] in pset:
            return qstack[-1]
        qstack.pop()
    
    assert(False)



print()





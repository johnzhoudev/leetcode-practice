# Results:
# Runtime: 57ms 91.97%
# Memory Usage: 18.8MB 86.64%

"""

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Idea: 
- preorder gives you pivot / node, and inorder can give you subtrees
- inherently recursive
- can we do iterative? - need to supply parent, and direction to attach

Tactic: preorder gives you pivot, inorder gives u subtrees. Recurse. Use indices faster, plus dict for finding index. Can also pop preorder, if doing left first

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solveFast(preorder, inorder):

    indices = {}
    for i, v in enumerate(inorder):
        indices[v] = i

    def recurse(pStart, pEnd, iStart, iEnd): # exclusive end
        if pEnd - pStart == 0:
            return None
        
        root = TreeNode(preorder[pStart])
        pivot = indices[root.val] # index of pivot in inorder 
        numItemsLeft = pivot - iStart
        root.left = recurse(pStart + 1, pStart + 1 + numItemsLeft, iStart, pivot)
        root.right = recurse(pStart + 1 + numItemsLeft, pEnd, pivot + 1, iEnd)
        return root
    
    return recurse(0, len(preorder), 0, len(inorder))



def solve(preorder, inorder):

    def recurse(preorder, inorder):
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        pivotNum = inorder.index(root.val) # index of pivot also num elts before pivot
        
        root.left = recurse(preorder[1:pivotNum + 1], inorder[:pivotNum])
        root.right = recurse(preorder[pivotNum + 1:], inorder[pivotNum + 1:])

        return root
    
    return recurse(preorder, inorder)



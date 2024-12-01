"""

129. Sum Root to Leaf Numbers

return total sum of all root to leaf numbers
- concat numbers


dfs and sum

O(n)

Tactic:
dfs
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):

    if not root: return 0

    total = 0

    def dfs(node, currnum):
        nonlocal total

        # first add to currnum
        currnum = currnum * 10 + node.val
        if not node.left and not node.right:
            total += currnum
        
        if node.left: dfs(node.left, currnum)
        if node.right: dfs(node.right, currnum)
    
    dfs(root, 0)
    return total
        

        
        



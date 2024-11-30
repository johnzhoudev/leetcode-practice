"""

938. Range Sum of BST


Idea: 
dfs, if value in range, add

O(n)
O(n) space

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root, low, high):

    state = [root]
    total = 0

    while state:
        node = state.pop()
        if not node: continue

        if low <= node.val and node.val <= high:
            total += node.val
        
        if node.left:
            state.append(node.left)
        if node.right:
            state.append(node.right)
    
    return total


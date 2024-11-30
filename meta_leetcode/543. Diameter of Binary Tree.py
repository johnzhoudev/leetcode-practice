"""

543. Diameter of Binary Tree

length of longest path between any 2 nodes

longest path = at each node, take max
- longest path in left node
- longest path in right node
- depth of left + 1 + 1 + depth of right

- update a global variable

O(n) time
O(n) stack space

Tactic:
Traverse tree, return length to node + 1 (no node, 0). Update global var.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    longestPath = 0

    # Return number of nodes = path length to it + 1
    def dfs(node):
        nonlocal longestPath

        if not node:
            return 0 # 
        
        left = dfs(node.left)
        right = dfs(node.right)
        longestPath = max(longestPath, left + right)
        return max(left, right) + 1
    dfs(root)
    return longestPath

def solve(root):
    longestPath = 0

    # returns max path length from leaf to this node
    def dfs(node):
        nonlocal longestPath
        assert(node)

        if not node.left and not node.right:
            return 0
        elif not node.left:
            rightLen = dfs(node.right)
            longestPath = max(rightLen + 1, longestPath)
            return rightLen + 1 # path to itself
        elif not node.right:
            leftLen = dfs(node.left)
            longestPath = max(leftLen + 1, longestPath)
            return leftLen + 1 # path to itself
        else: # both defined
            leftLen = dfs(node.left)
            rightLen = dfs(node.right)
            longestPath = max(leftLen + 1 + rightLen + 1, longestPath)
            return max(leftLen, rightLen) + 1
    
    dfs(root)
    return longestPath


        







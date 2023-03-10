"""

https://leetcode.com/problems/binary-tree-maximum-path-sum/

Idea:

yolo


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    # step 1, generate best solsn ending in a node recursively
    bestPathEndingInNodeMap = {}

    def getBestPath(node):
        global bestPathEndingInNodeMap
        if node.left is None and node.right is None:
            bestPathEndingInNodeMap[node] = node.val
            return node.val
        elif node.left is None:
            bestPathEndingInNodeMap[node] = max(node.val, bestPathEndingInNodeMap[node.right] + node.val)
            return node.val


        
        
        
    


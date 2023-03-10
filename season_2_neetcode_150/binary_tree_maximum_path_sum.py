# Results:
# Runtime: 88ms 73.39%
# Memory Usage: 21.2MB 91.62%\

"""

https://leetcode.com/problems/binary-tree-maximum-path-sum/

- path must be non-empty

Idea:
- do a recursive alg to get the max path ending at a specific node, going upwards
- then do a check on each node and see if linking the left and right paths will give a better sum - since 
this is a binary tree, can only turn once

Better: Post order traversal, calculate best paths ending at node recursively. then for node, compute only node, left, right, and both. update global max

Tactic: Post order traversal, calculate best paths ending at node (NOT INCLUDING BOTH SIDES) recursively. then for node, compute only node, left, right. update global max including max, bestpathtonode, and using both sides 

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    # recursively check, maintain max
    maxPath = root.val

    def calcBestPath(node):
        nonlocal maxPath
        if node is None: return 0
        bestLeft = calcBestPath(node.left)
        bestRight = calcBestPath(node.right)
        bestPathToNode = max(node.val, node.val + bestLeft, node.val + bestRight)
        maxPath = max(maxPath, bestPathToNode, node.val + bestLeft + bestRight)
        return bestPathToNode
    
    calcBestPath(root)
    return maxPath


def solve(root):
    # step 1, generate best solsn ending in a node recursively
    bestPathEndingInNodeMap = { None: 0 }

    # fills out bestPathEndingInNodeMap with best path ending at node
    def getBestPath(node):
        if node is None:
            return
        nonlocal bestPathEndingInNodeMap

        # generate recursive solns
        getBestPath(node.left)
        getBestPath(node.right)

        bestPathEndingInNodeMap[node] = max(node.val, bestPathEndingInNodeMap[node.left] + node.val, bestPathEndingInNodeMap[node.right] + node.val)

    getBestPath(root) # generates best paths for all nodes
    maxPath = bestPathEndingInNodeMap[root]

    # do dfs traversal, check best paths
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node is None: continue
        maxPath = max(maxPath, bestPathEndingInNodeMap[node], bestPathEndingInNodeMap[node.left] + node.val + bestPathEndingInNodeMap[node.right])
        nodes += [node.left, node.right]
    
    return maxPath






        
        
        
    


# Results:
# Runtime: 45ms 74.11%
# Memory Usage: 16.3MB 75.23%

"""

https://leetcode.com/problems/diameter-of-binary-tree/

diameter = longest path between two nodes

Idea:
- longest path = from node, longest path left + longest path right
- post order traversal

Tactic: Post order traversal, max longest paths. Careful with returning longest path, return longest left / right + 1 to account for edge to node, or 0 if none

"""

def solve(root):
    maxPath = 0

    def getLongest(node):
        nonlocal maxPath
        if node is None:
            return 0
        longestLeft = getLongest(node.left)
        longestRight = getLongest(node.right)
        maxPath = max(maxPath, longestLeft + longestRight)
        return max(longestLeft, longestRight) + 1 # Plus 1 here to account for this node reaching another
    getLongest(root)
    return maxPath
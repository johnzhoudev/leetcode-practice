"""

958. Check Completeness of a Binary Tree

check if complete

- all levels are complete except for last level, and last level has nodes to left

Idea:
- do BFS, each level, make sure all output
    - if one level node does not output a node, make sure all other nodes don't output
    - then make sure last level is all leaves

O(n) space

Could also DFS, O(log n) space
- do one left most search to find last level
- prioritize left then right
- keep track of last leaf node seen - if leaf after none, problem.

- if don't get to last level, problem

DFS Too complicated. Too many flags. BFS?


Tactic:
BFS with queue, and foundNull bool easiest.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def solve(root: TreeNode):
    foundNull = False
    queue = deque()
    queue.append(root)

    # queue traverses nodes in level order. So as soon as detect null, rest must also be null
    while queue:
        node = queue.popleft()

        if node:

            if foundNull: return False # if seen a null before

            queue.append(node.left)
            queue.append(node.right)
        else:
            foundNull = True
    return True


def solve(root: TreeNode):
    level = [root]

    leavesStarted = False
    while level:
        nextLevel = []
        for node in level:
            left = node.left
            right = node.right

            # invalid
            if leavesStarted and (left or right):
                return False

            if not left:
                if right: return False
                leavesStarted = True # should be no more leaves
            else:
                nextLevel.append(left)
            
            if not right:
                leavesStarted = True
            else:
                nextLevel.append(right)

        level = nextLevel
    
    return True


class Failure(Exception):
    def __init__(self):
        pass

def solve(root: TreeNode):
    # first get level of leftmost leaf node
    lastLeafNodeLevel = -1
    leftBottomEnded = False

    node = root
    while node:
        lastLeafNodeLevel += 1
        node = node.left

    # level 0 is root
    # lastLeafNodeLevel is fixed
    # When encountering leaf nodes, should be that level
    # Exception if it's 1 before, then set to -1 and set secondLastLeafNodeLevel

    def dfs(node, level):
        nonlocal leftBottomEnded
        nonlocal lastLeafNodeLevel

        if not node: return

        # if leaf node
        if not node.left and not node.right:

            # Case 1, left bottom hasn't ended
            if not leftBottomEnded:
                # still can move up
                if level == lastLeafNodeLevel - 1:
                    leftBottomEnded = True
                    lastLeafNodeLevel = level
                else:
                    raise Failure
            else: # case 2, has ended. So can't go up anymore
                if lastLeafNodeLevel != level:
                    raise Failure
        # not a leaf node
        else:
            # left must exist, else fail
            if not node.left:
                raise Failure

            dfs(node.left, level + 1)

            if not node.right:
                leftBottomEnded = True
                lastLeafNodeLevel = level
            else:
                dfs(node.right, level + 1)
    
    try:
        dfs(root, 0)
    except Failure:
        return False
    
    return True





"""
https://leetcode.com/problems/house-robber-iii/

Recursive binary tree search?

- money = max(value(node) + valueIfCannotUse(next), valueIfCanUse(next))

2 functions, valueIfCanUse and valueIfCannotUse -> just calls value if can use on childs
Use memoization, O(n) time since each node processed only once

Tactic: Technically don't need dp! Since searching a tree, just like a recursive thing. But just need to store value if robbed vs not robbed.
DP also works too

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):

    def robNode(root):
        if not root:
            return 0, 0
        
        # now return both if robbed and if not robbed
        leftIfRob, leftNoRob = robNode(root.left)
        rightIfRob, rightNoRob = robNode(root.right)
        robValue = root.val + leftNoRob + rightNoRob

        return robValue, max(leftIfRob, leftNoRob) + max(rightIfRob, rightNoRob) # can either rob or not?

    return max(robNode(root))


def solveMemo(root):

    state = {}

    def valueIfCannotUse(root):
        if not root:
            return 0
        return valueIfCanUse(root.left) + valueIfCanUse(root.right)


    def valueIfCanUse(root):
        if not root:
            return 0

        if root in state:
            return state[root]
        
        # else do recursive memoization
        value = max(root.val + valueIfCannotUse(root.left) + valueIfCannotUse(root.right), # use the root
                    valueIfCanUse(root.left) + valueIfCanUse(root.right)) # don't use the root
        
        state[root] = value

        return value
    
    return valueIfCanUse(root)

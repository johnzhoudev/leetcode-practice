"""

314. Binary Tree Vertical Order Traversal

vertical order traversal
- count number of times you go left and right in bfs
- append to correct stack
- prioritize bfs to make sure top first
- prioritize left over right

O(n) time and space

Tactic:
Either use lists of root and right, and left stacks, or use hash table and iterate thru range. Then bfs with offset from centre and add to stacks.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def solve(root):
    rootAndRightStacks = [] # going rightwards
    leftStacks = [] # going leftwards

    state = deque()
    state.append((root, 0)) # node, offset (- for left, + for right, 0 = root)

    def getStack(offset):
        if offset >= 0:
            if offset == len(rootAndRightStacks):
                rootAndRightStacks.append([])
            return rootAndRightStacks[offset]
        else:
            offset = (-offset) - 1
            if offset == len(leftStacks):
                leftStacks.append([])
            return leftStacks[offset]

    # do bfs
    while state:
        n = len(state)
        for _ in range(n):
            # add node
            node, offset = state.popleft()

            if not node: continue # empty 

            stack = getStack(offset)
            stack.append(node.val)

            # add childs
            state.append((node.left, offset - 1))
            state.append((node.right, offset + 1))
    
    return leftStacks[::-1] + rootAndRightStacks







    


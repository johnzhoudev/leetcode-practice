"""
173. Binary Search Tree Iterator

Coroutine?? 

Just manually simulate stack

O(log n) space, O(n) time
- store stack of nodes to output - leftmost, then once you output, remove and add all right nodes

Tactic:
Use stack to store nodes. addAllOnLeft helper method. Next = pop(), then addAllOnLeft(node.right).

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def addLeft(self, currNode: TreeNode):
        while currNode:
            self.stack.append(currNode)
            currNode = currNode.left

    def __init__(self, root):
        self.stack = [] # put nodes on the stack
        self.addLeft(root)

    def next(self) -> int:
        if not self.stack:
            raise RuntimeError()
        
        nodeToOutput = self.stack.pop()
        # Add all to left
        self.addLeft(nodeToOutput.right) # add all on right

        return nodeToOutput.val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0
        

"""

in order traversal of bst
takes in root
hasNext
next

inorder - traverse left, val, then right

Idea: keep a stack? idea is inorder traversal, but be able to pause at each step
hasNext - either traverse first, or make sure right and stack aren't empty

Tactic: use stack, store left nodes. when pop, process right.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def add_node_and_left(self, node, stack):
        while node is not None:
            stack.append(node)
            node = node.left

    def __init__(self, root):
        self.stack = []
        self.add_node_and_left(root, self.stack)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.add_node_and_left(node.right, self.stack)
        return node.val

    def hasNext(self) -> bool:
        return True if len(self.stack) != 0 else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
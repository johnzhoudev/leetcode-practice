"""

426. Convert Binary Search Tree to Sorted Doubly Linked List

Idea:

Just do an inorder traversal, update a global variable with the tail and keep appending


inorder - process left, val, right
in place should be possible

O(n) time 

Tactic:
DFS but pass tail of prev segment to attach to. Use sentinel start. Then at end, connect ends.



"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):

    if root is None: return None

    # want to return the node to connect it to
    # attach everything to head
    def dfs(node, head):

        if not node:
            return head # didn't attach anything, connect to head

        if node.left:
            head = dfs(node.left, head) # attach all node.left to head

        # connect with current node
        head.right = node
        node.left = head
        head = node

        # continue right
        if node.right:
            head = dfs(node.right, head)
        
        return head
    
    sentinel = Node(-1)
    lastNode = dfs(root, sentinel)

    # circular connection
    lastNode.right = sentinel.right # connect last to front
    sentinel.right.left = lastNode  # connect back

    return sentinel.right
    


        





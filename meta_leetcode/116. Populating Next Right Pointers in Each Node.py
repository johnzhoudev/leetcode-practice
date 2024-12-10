"""

116. Populating Next Right Pointers in Each Node


given perfect binary tree
populate next node - next node on the level

Idea:
- bfs? then parse thru in order and add next pointer

O(n) time
O(n space)

Must use O(1) extra space, not including stack size!

Idea:
- if node is left, next is just parent.right
- if node is right, next is parent.next.left

Tactic:
Either bfs, or GOATED, pass nextNode in dfs! either parent.right or parent.next.left!

"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def solve(root):
    if not root: return root

    def dfs(node, nextNode):
        if not node: return
        node.next = nextNode
        if not node.left: return
        dfs(node.left, node.right)
        dfs(node.right, nextNode.left if nextNode else None)
    
    dfs(root, None)
    return root

def solve(root):
    if not root: return root

    level = [root]
    while level:
        nextLevel = []

        # first add next pointer
        for i in range(len(level) - 1):
            level[i].next = level[i+1] # last will still be null
        
        # Now add next level
        for node in level:
            if not node.left: break
            nextLevel.append(node.left)
            nextLevel.append(node.right)
        
        level = nextLevel
    
    return root
    



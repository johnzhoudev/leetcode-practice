"""

138. Copy List with Random Pointer


linked list
random pointer to anyhting or null

make deep copy

- go thru first pass every node, make a copy
    - store original node => new node map
- then 2nd pass replace all the pointers

Or 1 pass, make copy of node in hash table.
- then as you go thru, only copy nodes not in hash table

O(n)
O(n) space

Better: O(1) space

- first make nodes point to copies of themselves
    - and copies point to real next
- then on 2nd pass, make copies point to copies (realnode->next == copy)

Tactic:
O(1) space - make nodes point to copies of nodes, then 2nd pass update node.next and node.random to the next (copies)
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def solve(head):

    if not head: return

    curr = head

    # first make all nodes point to copies
    while curr:
        copy = Node(curr.val, curr.next, curr.random)
        curr.next = copy
        curr = copy.next
    
    # now update all copies
    curr = head.next # the copy
    while curr:
        if curr.next: curr.next = curr.next.next # copy of og node
        if curr.random: curr.random = curr.random.next
        curr = curr.next
    
    return head.next

def solve(head):
    if not head: return
    dummy = Node(-1)
    tail = dummy
    curr = head
    nodeMap = {}

    while curr:
        nodeCopy = Node(curr.val, next=None, random=curr.random)
        nodeMap[curr] = nodeCopy
        tail.next = nodeCopy
        tail = tail.next
        curr = curr.next
    
    # now 2nd pass, update random pointers
    curr = dummy.next
    while curr:
        if curr.random:
            curr.random = nodeMap[curr.random]
        curr = curr.next
    
    return dummy.next
    
    


# Results:
# Runtime: 26ms 99.28%
# Memory Usage: 14.9MB 36.18%

"""

https://leetcode.com/problems/copy-list-with-random-pointer/

deep copy list, each node has a random pointer to another node in list or null

Idea:
- copy regular nodes originally, and create array of nodes
- create hash table of node to index
- iterate again, and use hash table to map pointers

Tactic: Hash table for random node. 
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def solve(head):
    # setup state
    nodeToIndex = {}
    copiedNodes = []

    # make node copies
    curr = head
    index = 0
    while curr:
        copiedNodes.append(Node(curr.val, curr.next, curr.random))
        nodeToIndex[curr] = index
        index += 1
        curr = curr.next
    
    # translate
    for node in copiedNodes:
        node.next = None if node.next == None else copiedNodes[nodeToIndex[node.next]]
        node.random = None if node.random == None else copiedNodes[nodeToIndex[node.random]]
    
    return None if head == None else copiedNodes[0]




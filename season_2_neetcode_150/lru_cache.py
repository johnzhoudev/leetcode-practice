"""

https://leetcode.com/problems/lru-cache/

- init with capacity
- get from cache using key
- put, and evict least recently used item
- Average O(1) time

Idea:
- hash table to doubly linked list
- get, just use hash table and remove link in node, and append to front
- put, evict last elt from ll and hash table, and add new node

Need operations to:
- remove node and add to front
- add new node to front
- remove node from back

Tip: Use dummy head and tail values to avoid annoying edge cases

Advanced Idea: Python dict preserves insertion order

Tactic: Use doubly linked list and hash table. Dummy head tail to avoid edge cases. Need ops remove node and add to front. Adv, python dict preserves insert order. dict.pop(key)
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.htable = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.htable:
            return -1
        self.htable[key] = self.htable.pop(key)
        return self.htable[key]

    def put(self, key: int, value: int) -> None:
        if key in self.htable: self.htable.pop(key)
        self.htable[key] = value
        if len(self.htable) > self.capacity:
            self.htable.pop(next(iter(self.htable)))

class LRUCache:

    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def addNodeToFront(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
    
    def removeNode(self, node):
        # edge cases, if it's head or end
        if (self.end == node):
            self.end = node.prev
        
        if (self.head == node):
            self.head = node.next
        
        # now remove
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next
        node.next = None
        node.prev = None
        return node
    
    def __init__(self, capacity: int):
        self.htable = {} # maps to node references
        self.capacity = capacity

        self.head = None
        self.end = None
        

    def get(self, key: int) -> int:
        if key not in self.htable:
            return -1
        node = self.htable[key]
        # remove node and add node to front
        self.removeNode(node)
        self.addNodeToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.htable:
            node = self.htable[key]
            node.val = value
            self.removeNode(node)
            self.addNodeToFront(node)
        else:
            if self.capacity == len(self.htable):
                node = self.removeNode(self.end)
                del self.htable[node.key]
            newNode = self.Node(key, value)
            self.htable[key] = newNode
            self.addNodeToFront(newNode)


"""

146. LRU Cache


- doubly linked list
- hash table to doubly linked list

get - get from hash table, and remove / append
put - get from hash table, remove
    - then add to front

Tactic:
DoublyLinkedList - remove, removeFromBack, addToFront. And hash table of key -> node(key, val).
"""

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def addToFront(self, node):
        assert(node.next is None)
        assert(node.prev is None)

        if self.count == 0:
            self.head = node
            self.tail = node
        else: # at least 1 node, so head not null
            node.next = self.head
            node.next.prev = node
            self.head = node
        
        self.count += 1
    
    def remove(self, node):
        # node must be in list
        assert(self.count > 0)

        if self.count == 1: # only node
            assert(self.head == self.tail and self.head == node)
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
        else: # removing from inbetween
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

            # reset node
            node.next = None
            node.prev = None

        self.count -= 1
        return node

    # returns node
    def removeFromBack(self):
        return self.remove(self.tail)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.hashmap = {}
    
    def getNode(self, key):
        if key in self.hashmap:
            return self.hashmap[key]
        return None

    def get(self, key: int) -> int:
        node = self.getNode(key)
        if not node:
            return -1
        
        # update
        self.dll.remove(node)
        self.dll.addToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.getNode(key)

        # already added, so just update value
        if node:
            node.val = value
            self.dll.remove(node)
            self.dll.addToFront(node)
            return
        
        # not added, may have to remove
        if len(self.hashmap) == self.capacity:
            delnode = self.dll.removeFromBack()
            del self.hashmap[delnode.key]
        
        newnode = ListNode(key, value)
        self.dll.addToFront(newnode)
        self.hashmap[key] = newnode




"""

https://leetcode.com/problems/merge-k-sorted-lists/

merge - can i just use a heap?

Tactic: Use heap - O(n log k), space O(k). Better, divide and conquer recursive. O(n log k), space O(1) since just comparing

"""

import heapq # minheap, sorts by first elt in tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solvednc(lists):

    def mergeLists(l1, l2):
        head = ListNode() # dummy
        curr = head

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

        if l1: curr.next = l1
        else: curr.next = l2

        return head.next
    
    if len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        return mergeLists(lists[0], lists[1])
    else:
        pivot = len(lists) // 2
        return mergeLists(solvednc(lists[:pivot]), solvednc(lists[pivot:]))

def solve(lists):
    heap = []
    n = len(lists)
    head = ListNode() # dummy
    curr = head

    for i in range(len(lists)):
        if lists[i] == None: continue
        heapq.heappush(heap, (lists[i].val, i)) # pushing (val, index)
        # don't remove node yet, just store index of list
    
    while heap:
        val, idx = heapq.heappop(heap)
        # pop node from list
        node = lists[idx]
        lists[idx] = node.next

        # add new node to lists
        if lists[idx]: heapq.heappush(heap, (lists[idx].val, idx))

        # add node to curr
        node.next = None
        curr.next = node
        curr = curr.next
        
    return head.next
        


    

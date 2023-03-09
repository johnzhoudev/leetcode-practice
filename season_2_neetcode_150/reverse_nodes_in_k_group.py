"""

https://leetcode.com/problems/reverse-nodes-in-k-group/

- given head of ll
- reverse k at a time
- if not multiple, remain

Idea:
- can do reversal trick, next node is set as front to reverse a list
- keep head of master list, and tail pointer
- if end, just reverse last part and append to regular
O(n) time, const space

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, k):
    newHead = ListNode() # dummy
    newTail = newHead

    while head:

        # Try to extract k elements
        tempHead = head
        tail = tempHead
        head = head.next
        tempHead.next = None # remove link

        for _ in range(k - 1): # since already added head
            if head is None:
                reversedHead = tempHead
                tempHead = tempHead.next
                reversedHead.next = None
                while tempHead:
                    tempNext = tempHead.next
                    tempHead.next = reversedHead
                    reversedHead = tempHead
                    tempHead = tempNext
                newTail.next = reversedHead
                return newHead.next
            
            # add head to list and advance
            tempNext = head.next
            head.next = tempHead
            tempHead = head
            head = tempNext
        
        newTail.next = tempHead
        newTail = tail

    return newHead.next


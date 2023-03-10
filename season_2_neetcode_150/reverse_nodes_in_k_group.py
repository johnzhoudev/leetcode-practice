# Results:
# Runtime: 47ms 82.28%
# Memory Usage: 15.2MB 31.73%

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

More concise idea: just check k in advance. if all good, reverse, else just append
still O(n)

Tactic: Get group, then reverse. or reverse k, and if can't get k, reverse again. Cautious, make sure to disconnect group before reverse

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Don't know if this is better tbh. 
def solveConcise(head, k):
    dummyHead = ListNode()
    tail = dummyHead

    def reverse(head):
        newHead = head
        count = 1
        lastElt = head
        head = head.next
        newHead.next = None
        while head and count < k:
            tempNext = head.next
            head.next = newHead
            newHead = head
            head = tempNext
            count += 1
        return newHead, lastElt, head 

    while head:

        count = 0
        curr = head
        for _ in range(k):
            if curr is None:
                break
            curr = curr.next
            count += 1
        
        if count == k:
            listToAppend, lastElt, head = reverse(head) # returns list to append, and advances head
        else:
            listToAppend = head
            lastElt = None
            head = None
        
        tail.next = listToAppend
        tail = lastElt
    
    return dummyHead.next
        

        
def solve(head, k):
    dummyHead = ListNode() # dummy
    tail = dummyHead

    while head:

        # Try to extract k elements
        tempHead = head
        tempTail = tempHead
        head = head.next
        tempHead.next = None # remove link

        for _ in range(k - 1): # since already added head

            # If can't reverse, reverse again
            if head is None:
                reversedHead = tempHead
                tempHead = tempHead.next
                reversedHead.next = None
                while tempHead:
                    tempNext = tempHead.next
                    tempHead.next = reversedHead
                    reversedHead = tempHead
                    tempHead = tempNext
                tail.next = reversedHead
                return dummyHead.next
            
            # add head to list and advance
            tempNext = head.next
            head.next = tempHead
            tempHead = head
            head = tempNext
        
        tail.next = tempHead
        tail = tempTail

    return dummyHead.next


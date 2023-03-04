# Results:
# Runtime: 95ms 53.79%
# Memory Usage: 23.9MB 59.31%

"""

https://leetcode.com/problems/reorder-list/

- need to make 1, n, 2, n-1, 3, n-2, ...

Idea:
- get length, and split into 2 lists
- reverse second half of list, so have 2 lists 1 and n
    - or put on a stack? - takes O(n) space
- interleave
O(n)
O(1)

Tactic: find middle (tip, advance one fast and one slow), reverse 2nd half, merge interleave

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solveFancy(head):

    # get halfway point by advancing 2 lists, one twice as fast
    # 1
    # 1 2 3x 4 5
    # 1 2 3x 4 5 6
    fast, slow = head, head
    while fast.next and fast.next.next: # stop earlier a bit
        fast = fast.next.next
        slow = slow.next

    # in both cases, reverse next after slow
    curr = slow.next
    slow.next = None
    backHead = None
    while curr:
        nextCurr = curr.next
        curr.next = backHead
        backHead = curr
        curr = nextCurr
    
    # Merge together, backHead will have same or less values
    count = 0
    finalHead = ListNode()
    curr = finalHead
    while backHead or head:
        if count % 2 == 0:
            curr.next = head
            head = head.next
        else:
            curr.next = backHead
            backHead = backHead.next
        curr = curr.next
        count += 1
    
    head = finalHead.next


def solve(head):
    # get length
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    
    # reverse second half of list
    halfway = n // 2
    curr = head
    while halfway > 0:
        curr = curr.next
        halfway -= 1
    
    prevCurr = curr
    curr = curr.next
    prevCurr.next = None
    backHead = None
    while curr:
        nextCurr = curr.next
        curr.next = backHead
        backHead = curr
        curr = nextCurr
    
    # now merge, interleaving
    finalHead = ListNode()
    curr = finalHead
    count = 0
    while head and backHead:
        if count % 2 == 0:
            curr.next = head
            head = head.next
        else:
            curr.next = backHead
            backHead = backHead.next
        curr = curr.next
        count += 1
    
    if head:
        curr.next = head
    elif backHead:
        curr.next = backHead
    
    # return finalHead.next
    head = finalHead.next


            










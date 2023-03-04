# Results:
# Runtime: 43ms 40.99%
# Memory Usage: 13.8MB 98.52%

"""

https://leetcode.com/problems/merge-two-sorted-lists/

Idea:
- go thru, take larger.

Tactic: Use dummy head, and track tail

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(list1, list2):
    head = ListNode() # dummy head
    tail = head

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    return head.next








# Results:
# Runtime: 42ms 99.45%
# Memory Usage: 17.5MB 58.5%

"""

https://leetcode.com/problems/linked-list-cycle/

Idea:
- keep set, iterate thru

Better:
- tortise and hare technique

Tactic: Tortise and hare pointer, or set. Careful on slow-fast first advance, could be same. start fast 1 ahead
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solveFast(head):
    slow = head
    fast = head.next if head else head

    while fast and fast.next:
        fast = fast.next
        slow = slow.next
        if fast == slow:
            return True
        fast = fast.next
        if fast == slow:
            return True
    
    return False

    

def solve(head):
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    
    return False

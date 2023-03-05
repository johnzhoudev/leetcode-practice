# Results:
# Runtime: 31ms 86.20%
# Memory Usage: 13.8MB 59.7%

"""

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

- remove nth node FROM END OF LIST

Ideas:
- count, then remove
- or, advance fast n times, then advance to end - fast slow method
O(n)

Tactic: fast and slow runners. careful with edge cases
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, n):
    # 1 2 3 4 5
    fast, slow = head, head
    for _ in range(n):
        fast = fast.next

    # edge case, remove first item
    # advance one more for regular case, but edge case, fast already none
    if fast == None:
        return head.next
    else:
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    # now slow is one before one to remove
    slow.next = slow.next.next

    return head
    
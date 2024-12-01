"""

2. Add Two Numbers

reverse order

return sum as linked list

carry!

Tactic:
Use a carry, ifs to get digits or 0, add carry at end, sentinel head

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1, l2):

    carry = 0
    sentinel = ListNode()
    head = sentinel

    while l1 or l2:

        d1 = l1.val if l1 else 0
        d2 = l2.val if l2 else 0
        if l1: l1 = l1.next
        if l2: l2 = l2.next

        sum = d1 + d2 + carry 
        d = sum % 10
        carry = sum // 10

        head.next = ListNode(d)
        head = head.next

    # potentially add carry
    if carry != 0:
        head.next = ListNode(carry)
    
    return sentinel.next


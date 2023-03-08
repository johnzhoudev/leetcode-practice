# Results:
# Runtime: 61ms 93.59%
# Memory Usage: 13.9MB 33.93%

"""

https://leetcode.com/problems/add-two-numbers/

- non empty lists, non-neg integers
- digits stored in reverse order
- add 
- no leading 0 except 0 itself

Idea: 
- do regular addition, have a carry, dummy head
- Trick, just get 0 if list empty

Tactic: Regular addition, carry, dummy head, get 0 if list empty. Watch for extra carry at end
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1, l2):
    # setup
    dummyHead = ListNode()
    curr = dummyHead
    carry = 0

    while l1 or l2:
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0

        sum = (num1 + num2 + carry) % 10
        carry = (num1 + num2 + carry) // 10

        curr.next = ListNode(sum, None)
        curr = curr.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    if carry != 0: curr.next = ListNode(carry, None)

    return dummyHead.next





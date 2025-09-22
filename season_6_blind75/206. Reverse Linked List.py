"""

206. Reverse Linked List

use the head trick


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    new_head = None
    while head != None:
        next = head.next
        head.next = new_head
        new_head = head
        head = next
    return new_head
        

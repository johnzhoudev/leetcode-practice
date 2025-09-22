"""

143. Reorder List

get to halfway, invert, then merge

O(n)

Tactic: Get halfway (slow / fast pointer, or manual), invert, then merge

"""
from math import ceil


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    if not head:
        return head
    
    def reverse(node):
        new_head = None
        while node:
            next_node = node.next
            node.next = new_head
            new_head = node
            node = next_node
        return new_head
    
    def get_len(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    
    def traverse_and_disconnect(node, idx): # traverses to idx and disconnects nodes
        last = None
        while idx > 0:
            last = node
            node = node.next
            idx -= 1
        
        if last:
            last.next = None

        return node

    # Go to middle
    n = get_len(head)
    halfway = traverse_and_disconnect(head, ceil(n / 2)) # get middle
    list2 = reverse(halfway)
    list1 = head

    # Now merge
    dummy_head = ListNode()
    curr = dummy_head

    while list1 or list2:
        curr.next = list1 # attach next
        list1 = list1.next # advance list1
        curr = curr.next # advance curr

        if not list2:
            break
        
        curr.next = list2
        list2 = list2.next
        curr = curr.next
    
    return dummy_head.next


        
        







            
"""

19. Remove Nth Node From End of List


1st pass to get lenght, them remove?

O(n) time O(1) space


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, n):

    # Get length
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    
    # now remove
    curr = head
    node_before_remove = count - n
    if node_before_remove == 0: # Edge case
        return curr.next
    
    # Advance until node before
    curr_count = 1
    while curr_count != node_before_remove:
        curr = curr.next
        curr_count += 1
    # remove next node
    curr.next = curr.next.next
    return head

    

    
    
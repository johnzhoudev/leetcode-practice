"""

708. Insert into a Sorted Circular Linked List

non descending order
node is reference to any value in the list
could be list null

Idea:
- increasing order
- need to find curr elt <= x <= next elt  Then insert.

- If larger than all, also watch out for beginning and end
    - keep reference of head node to watch out for loop, in case of all same number
    - find place where curr > curr.next. If reached there, insert if x >= curr or x <= curr.next


Edge cases: 
- empty list
- 1 element
- loop around, all same element
- insert regualar
- insert at ends (greater than all / smaller than all)

Tactic:
Check valid inserting point, or case if loop around. Also check case of all values same, and reach head again.

"""

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def solve(head, val):

    if not head:
        node = Node(val=val, next=None)
        node.next = node
        return node # circular

    curr = head.next

    while curr != head:

        # first check if valid inserting point
        if curr.val <= val and val <= curr.next.val:
            # do the insert and break!
            break
            # curr.next = Node(val=val, next=curr.next)
            # return head
        
        # otherwise, check if reached loop around
        elif curr.val > curr.next.val and (val >= curr.val or val <= curr.next.val):
            break
            # curr.next = Node(val=val, next=curr.next)
            # return head
        
        curr = curr.next
    
    # if wrapped around to head, just insert at head
    curr.next = Node(val=val, next=curr.next)
    return head









    
"""

23. Merge k Sorted Lists

k linked lists
each sorted in ascending order

merge all into 1 linked list and return

Can we not just use a heap?

O(n log k)

Or divide and conquer

k lists
- k/2, then k/4, then so on - log k merges
- merging n nodes
- n log k

Tactic:
Divide and conquer. Still O(n log k), but O(1) memory!

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(lists, start, end):

    def merge(l1, l2):
        head = ListNode()
        curr = head

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        # could both be null
        return head.next
    
    if end - start == 0:
        return None
    elif end - start == 1:
        return lists[start]
    else:
        pivot = (end - start) // 2
        return merge(solve(lists, start, start + pivot), solve(lists, start + pivot, end))
        

        


# Results:
# Runtime: 32ms 98.80%
# Memory Usage: 13.9MB 79.56%

# Merge Two Sorted Lists
"""
two linked lists heads
merge to make 1 sorted list - splice together nodes of first list

Ideas:
1. compare heads and add smallest. If none to add, add rest.
Time: O(n) n is size of all nodes - best we can do since we need to at least consider the nodes.
space: O(1) auxillary space

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
	head = ListNode()
	tail = head
	# while both not empty, add to a head
	while (list1 is not None and list2 is not None):
		if (list1.val < list2.val):
			tail.next = list1
			list1 = list1.next
		else:
			tail.next = list2
			list2 = list2.next

		tail = tail.next
		
	# if both empty, return 
	# Technically handled already
	# if (list1 is None and list2 is None):
	# 	return head.next
	if (list2 is None): # append list1
		tail.next = list1
	else:
		tail.next = list2 # append list2
	
	return head.next
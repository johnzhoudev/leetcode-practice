# Results:
# Runtime: 67ms 47.67%
# Memory Usage: 13.9MB 74.67%

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

head of sorted linked list
delete nodes with duplicate numbers
	- including the node itself!!!
return linked list sorted

min time O(n)

Ideas:
- iterate thru list, check next. if next has same value, next = next->next to delete
- O(n) time, O(1) space


Simpler
- Traverse array and mark nodes for deletion -> look at next, and if duplicate, mark. and keep marking
- then rebuild array, keep traversing till non-deleted
- can make a hash table to store if something should be deleted or not 
- O(n) aux space



- iterate thru list, but set next as getNext()
- getNext() -> as you go, store left. then if left matches right, duplicate, keep skipping till
- left doesn't match stored. then restart check. returns if left is new, and right doesn't match.
O(n) time, O(1) space

Tactic: If you want to use O(1) space, need to get next node dynamically. Also use dummy head to avoid weirdness.
- just skip all nodes that match.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
      print(self.val)
      if (self.next is not None): self.next.print()

def deleteDuplicates3(head):
	# sentinel head
	sentinel = ListNode(-1, head)
	predecessor = sentinel

	while (head): # either head is beginning of duplicates, or not. either skip, or add.

		# if next is null, all good. add.
		if (head.next is None):
			predecessor.next = head
			head = head.next
			predecessor = predecessor.next
		# if duplicate, advance but do not advance predecessor in case 2 duplicate ranges
		elif (head.next and head.val == head.next.val):
			# If a duplicate, must skip
			while (head.next and head.val == head.next.val): # want to end with head at last one to be deleted
				head = head.next

			head = head.next # skip one more time
			# also set predecessor to skip all duplicates in case ends in duplicate
			predecessor.next = head
		else: # not a duplicate, so add
			predecessor.next = head
			head = head.next
			predecessor = predecessor.next

	return sentinel.next

def deleteDuplicates2(head):

	dummyHead = ListNode(-1, head)
	global currNode
	currNode = dummyHead

	def getNext(): # called on current node we want to append to
		leftNode = currNode.next
		currDuplicateValue = None

		# while loop to do comparisons
		while (leftNode is not None):
			rightNode = leftNode.next

	 		# if rightnode null, reached end so either return None if leftnode duplicate, or leftnode
			if (rightNode is None):
				return None if currDuplicateValue == leftNode.val else leftNode
			elif (leftNode.val == currDuplicateValue or leftNode.val == rightNode.val): # mark as duplicate and continue
				currDuplicateValue = leftNode.val
				leftNode = leftNode.next
			else: # must be a unique leftnode value
				return leftNode

		return None
	
	# then our solution is easy. build list, and use getNext
	# currNode = getNext() # get first non-duplicate node, from dummyHead so it considers all things after.
	# head = currNode

	while (currNode is not None):
		currNode.next = getNext() # first time this runs, currNode is dummyHead so getNext gets first non repeat
		currNode = currNode.next
	
	return dummyHead.next

# deleteDuplicates3(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, None))))))).print()
deleteDuplicates3(ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None))))))).print()
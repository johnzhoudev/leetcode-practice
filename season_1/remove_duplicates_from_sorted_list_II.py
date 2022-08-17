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
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
      print(self.val)
      if (self.next is not None): self.next.print()

def deleteDuplicates2(head):

	global currNode
	currNode = head

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
	currNode = getNext() # get first non-duplicate node
	head = currNode

	while (currNode is not None):
		currNode.next = getNext()
		currNode = currNode.next
	
	return head

# deleteDuplicates2(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, None))))))).print()
deleteDuplicates2(ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None))))))).print()
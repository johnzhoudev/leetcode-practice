# Results:
# Runtime: 61ms 62.52%
# Memory Usage: 13.9MB 72.41%

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

delete duplicates so elt appears only once
sorted list given

Idea: must go thru all elts, so O(n) min time
- keep adding to head, but if next is same as head, don't add and skip

Tactic: Can do naive way, or fancy way where you go thru, but each time next matches curr, curr.next = curr.next.next (delete intermediate)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
      print(self.val)
      if self.next is not None: self.next.print()

def deleteDuplicates2(head):
	cur = head
	while (cur):
		if (cur.next and cur.val == cur.next.val):
			cur.next = cur.next.next # skip duplicate
		else:
			cur = cur.next
	return head
		

def deleteDuplicates1(head):
	originalHead = head
	currNode = head.next if head else None
	while (currNode):
		# either add currNode if unique, or skip.

		if (currNode.val != head.val):
			# head.next = currNode
			head = head.next
			currNode = currNode.next
		else:
			# is a duplicate, so advance.
			currNode = currNode.next
			head.next = currNode # move head.next to next eligible currNode

	return originalHead

# test cases
deleteDuplicates2(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))).print()
deleteDuplicates2(ListNode(1, ListNode(1, ListNode(1, ListNode(1, None))))).print()

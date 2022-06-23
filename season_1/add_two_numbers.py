# Results: 
# Runtime: 87ms 66.83%
# Memory Usage: 14.1 10.21%

# 2 non-empty lniked lists - non neg integers
# Digits stored reverse order
# Each node has single digit
# Add and return as linked list.
# Assume no leading 0, except 0 itself.

# Brute force - dumb adding with carry. n is len of longest list
# Time: O(n) - can't do better, must view at least each thing.
# Space: O(1) - replace longest linked list and possibly add one.

# 1. while both are not none, add both and set result in one and carry in other. 
# 2. when one ends, keep going with just the carry and 0 for the other.
# - this has 2 states, if both are active and if 1 is inactive.
# - maybe best to have adder helper, and pass 0 if one is ended. And another part to advance.
# - reach end of both, add carry to end if not 0.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def printList(self):
		print(self.val, end=' ')
		if (self.next != None):
			self.next.printList()

def addHelper(outList, in1, in2, carry):
	sum = in1 + in2 + carry
	outList.val = sum % 10 # append value
	return sum // 10 # return carry

def addTwoNumbers(list1: ListNode, list2: ListNode):

	# Guaranteed to exist
	# input1
	# input2
	carry = 0

	outListHead = list1
	outListNext = list1
	outListPrev = None

	while (list1 != None or list2 != None):

		input1 = list1.val if list1 != None else 0
		input2 = list2.val if list2 != None else 0
		
		carry = addHelper(outListNext, input1, input2, carry)
		# outListNext value written to

		# advance list1, list2, outListNext
		if (list1 != None):
			list1 = list1.next
		if (list2 != None):
			list2 = list2.next

		if (outListNext.next == None):
			newNode = ListNode(0)
			outListNext.next = newNode
		outListPrev = outListNext
		outListNext = outListNext.next
		
	# on end, both lists are empty. so add carry to last listNode. guaranteed to have one listnode outside
	if (carry != 0):
		outListNext.val = carry
	else:
		outListPrev.next = None
		
	return outListHead

def validate(list1, list2):
	addTwoNumbers(list1, list2).printList()

l1 = ListNode(3, ListNode( 2, ListNode(5)))
l2 = ListNode(3, ListNode( 2, ListNode(5)))

validate(l1, l2)




"""
Search insert position

sorted arr, distinct ints, target val
return index if target found, else return index of where it would be if inserted in order
O(log n)

0 1 2 3 5 6  insert 4 (position 4)

Idea: Binary search, but if one item left and not it, check direction and return index. would be inserted right there.

Tactic:
Binary search but be careful about where you move your pivots. l + r // 2 biases left. check 3 2 1 items left case and 
pivot adjustments to make sure working.
"""

def searchInsert(nums, target):
	# 1. binary search
	left = 0
	right = len(nums) - 1
	while (left <= right): # never a case where left > right
		pivot = (left + right) // 2 # bias lef

		# edge cases: what if insert on the ends?
		# right will work. Since we bias left, we will always hit 1.
		# left? 

		if (nums[pivot] == target):
			return pivot
		elif (left == right): # last item, not equal. so return direction
			return pivot + 1 if nums[pivot] < target else pivot
		elif (nums[pivot] < target): # go right
			left = pivot + 1
		else: # possibility when we go left, that we'll go over. So need to just not reduce
			right = pivot # will be fine since we bias left when we pick the pivot.

	assert(False)

def validate(nums, target, expected):
	if (searchInsert(nums, target) != expected):
		print("TEST FAILED")
		print(nums)
		print(target)
		print("Result: " + str(searchInsert(nums, target)))
		print("Expected: " + str(expected))

validate([0, 1, 2, 3, 5, 6], 4, 4)
validate([0], 4, 1)
validate([1, 3], 0, 0)
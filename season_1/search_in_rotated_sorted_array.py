# Results:
# Runtime: 42ms 94.87%
# Memory Usage: 14.3MB 56.20%

"""
Search in Rotated Sorted Array
nums: int array - ascending order, distinct values
- possibly rotated at unknown pivot index 1 <= k <= len(nums)
	- basically just means shifted over so [k, k+1, ..., n-1, 0, 1, ...k-1]

Given nums after rotation, and int target, return index of target if in nums, or -1 if not in num.
O(log n) runtime.

- empty array?? return null?
- not given shift amount, but sorted in ascending order, distinct values (what if not distinct)??

Ideas:
- ideally we want maybe a binary search, but what happens if it's rotated?
	- can we find the pivot? if we can, we can stitch together the sections and do a binary search
0 1 2 3 4
2 3 4 0 1 -> shift with pivot 2, basically add 2 to index and you'll get original number. but mod len
- take advantage of mod? yea! then becomes regular binary search.
- or find the index where the actual start should be...

start at index 3, so to get original 0, add 3 and mod len(nums)

- how to find pivot in log n time? Need to find smallest number basically.
	- num to left is bigger and num to right is bigger. some binary search?

2 3 4 5x 6 0 1 - how to tell which side it's on? pick 5. end is 2, -> 5 is ascending. but 5 -> 1, not ascending. 
must have wrapped around. Thus go whichever side is less.
2 3 4 5 6 0 1
7 0 1 2 3 4 5x 6
- also as you look, could also do a check if found. might get lucky...

O(log n) time. O(1) space, basically.
Can we do it faster? lower bound on comparison based sorting, yea it's O(log n) minimum. 

"""

def search(nums, target):
	# 1. Need to find which index is the "start" of the array
	# Will do a binary search, and check ends to determine.

	left = 0
	right = len(nums) - 1 # Inclusive. Is it better to write exclusive?
	global startIndex
	startIndex = -1
	while (left <= right):

		if (left == right): # found
			startIndex = left
			break
			
		pivot = left + ((right - left + 1) // 2)
		# check left and right, and adjust
		# 2 3 4 5x 6 0 1
		# 6 0 1 2x 3 4 5
		# 0 1 2 3 4 5 6 Edge case
		# damn, need to be able to eliminate the pivot basically

		# Improvement here: 
		# Crazy stuff! if mid > hi, must be on right and can rule out mid since if mid was start, <.
		# otherwise, must be on left and cannot rule out mid
		# also handles if 0 is start (no rotation). keeps reducing hi
		# always reduces since mid = lo

		# Left bias, mid = (lo + hi) // 2

		# while(lo<hi){
		# 	int mid=(lo+hi)/2;
		# 	if(A[mid]>A[hi]) lo=mid+1;
		# 	else hi=mid;
		# }


		if (pivot != 0 and nums[pivot - 1] > nums[pivot]):
			startIndex = pivot
			break
		elif (nums[left] > nums[pivot]): # go left
			right = pivot - 1
		elif (nums[pivot] > nums[-1]):
			left = pivot + 1
		else: # no shift
			startIndex = left
			break

	assert(startIndex != -1)

	def get(nums, index):
		return nums[(index + startIndex) % len(nums)]
	
	def getIndex(index):
		return (index + startIndex) % len(nums)
	
	# 2. do binary search for item but adjust by startIndex. 
	left = 0
	right = len(nums) - 1

	while (left <= right):
		pivot = left + ((right - left + 1) // 2)

		pivotValue = get(nums, pivot)

		if (pivotValue == target): # if found
			return getIndex(pivot)
		elif (pivotValue < target): # go right
			left = pivot + 1
		elif (pivotValue > target): # go left
			right = pivot - 1
	
	# if nothing found, left > right, so return -1
	return -1

	# return -1 if not in nums

def validate(nums, target, expected):
	if (search(nums, target) != expected):
		print("TEST FAILED")
		print(nums)
		print(target)
		print("Result: " + str(search(nums, target)))
		print("Expected: " + str(expected))
		print()

validate([0, 1, 2], 1, 1)
validate([0, 1, 2], 0, 0)
validate([1, 2, 0], 0, 2)
validate([1, 2, 0], 1, 0)




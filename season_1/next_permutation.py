# Results:
# Runtime: 75ms 32.47%
# Memory Usage: 13.8MB 74.94%

# Next Permutation
"""
permutations of array [1, 2, 3]
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1 -> largest maps back to smallest
- lexicographically increasing in order

- Given array of ints (nums), find next permutation of nums
- Must be in place and use constant memory

Thinking:
Need to get the next largest, lexicographically -> but must have same numbers
How to do it intuitively?
Thinking about swapping algorithms to swap...
- look at closest from back and swap with first that's less x
- if none are less, swap with

Intuitively, say you have a permutation x1 x2 x3 x4...xn
Next permutation? What's the smallest increase you can make here? That's still larger?
Possible moves: basically need to always move a larger number on the right towards the left, and displace others.

Very first instance will be all the nums in sorted order
- so as long as increasing, no worries, can't go backwards

1 2 3 4
1 2 4 3 - made swap part descending
1 3 2 4 - 3 2 4 -> swap 3 with 2, and make rest ascending
1 3 4 2 - 2-4, 2-3, 2-1 (but also want to shift as low as possible) - 4 and 3, then make rest ascending
1 4 2 3 - 3-2 - switch
1 4 3 2 - descending order
- 2-3, 2-4, 3-4, 2-1 (so for each far out, try from back to front)
2 1 3 4 - 4-3
2 1 4 3 - 3-4 3-1
2 3 1 4

Strategy
- check from the right, and compare until you see the first one that goes in descending order - O(n^2)
- then swap and sort the rest in ascending order - in place sorting??? O(n^2)

Why does this work?
- to increase, always want to move a larger number to the left
- but once we make a move, the next smallest will have numbers to the right of it in ascending / lowest order
- and the smallest move we can make is the closest one on the right

Questions:
- Duplicates?
"""

def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

# Sorts nums in place from index [i:]
# O(n^2) just find the min and swap
def sortRest(nums, sortIndex):
	for i in range(sortIndex, len(nums)):
		# For each index after sortIndex
		minIndex = i

		# Get min
		for j in range(i, len(nums)):
			if (nums[j] < nums[minIndex]):
				minIndex = j
		
		# swap current index with min
		swap(nums, i, minIndex)


def nextPermutation(nums):
	# 1. Try and find smallest from right to swap with
	# Check each item from right, and go in order from right to see if less.

	# i is the potential one to switch
	# [2 1 4 3] - consider 4-3, then 1-3, 1-4, so on

	for i in range(len(nums) - 2, -1, -1):
		for j in range(len(nums) -1, i, -1):
			if (nums[j] > nums[i]):
				isLastPermutation = False
				swap(nums, j, i)
				sortRest(nums, i + 1) # safe if at end
				return

				# if you find the closest one to swap, do the swap and sort the rest
				# Edge case: Handle when there is no next (descending order)

	# If reached here, did not find a switch area
	# So must sort whole thing	
	sortRest(nums, 0)

def validate(nums, expected=None):
	nextPermutation(nums)
	if (expected != nums):
		print("Expected: ")
		print(expected)
		print("Result: ")
		print(nums)
		print()

validate([1, 2, 3], [1, 3, 2])
validate([1, 3, 2], [2, 1, 3])
validate([2, 1, 3], [2, 3, 1])
validate([2, 3, 1], [3, 1, 2])
validate([3, 1, 2], [3, 2, 1])
validate([3, 2, 1], [1, 2, 3])

"""

https://leetcode.com/problems/maximum-subarray/

int array nums
contiguous subarray with at least 1 num with largest sum, and return sum.
subarray = continuous. no breaks.
guaranteed at least 1 number

Ideas:
1. some dynamic programming? no, O(n^2) since subproblems are start and end...
2. Rolling window? 

Trick: ends are also max points from start to middle. can use DP to figure out.

Idea 2: rolling window
2 -1000 32 34 -3 56 -333 34 43
max range, to left, any subarray that ends one to the left of the range, or starts one to the right must be 
a negative total sum else could have been added. So we can scan the array from left to right, keeping max
- if positive, keep scanning. If negative, start decrementing from left. if hit end, done.
- Will we always hit the solution? if we hit negative, cannot be part of solution.

"""

def maxSubArray(nums):


def maxSubArray2(nums):
	# 1. go thru and get the rolling sum going rightwards from leftmost elt to end
	# largestFromLeft = [None for _ in range(len(nums))]
	# largestFromLeft[0] = nums[0]
	currSum = nums[0]
	currMaxFromLeft = currSum
	# rightIndex = 0
	for i in range(1, len(nums)):
		currSum += nums[i]
		if (currSum > currMaxFromLeft):
			currMaxFromLeft = currSum
			# rightIndex = i
	
	# extract total
	total = currSum

	# now do right side
	currSum = nums[-1] # from end
	currMaxFromRight = currSum
	# leftIndex = len(nums) - 1
	for i in range(len(nums) - 2, -1, -1):
		currSum += nums[i]
		if (currSum > currMaxFromRight):
			currMaxFromRight = currSum
			# leftIndex = i
	
	# Now return the sum
	return currMaxFromRight + currMaxFromLeft - total
	
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))

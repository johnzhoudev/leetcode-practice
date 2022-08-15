# Results:
# Runtime: 1211ms 39.81%
# Memory Usage: 28.5MB 9.99%

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

Thinking V3:
- min time complexity O(n) to check each element
- Brute force: get all ranges O(n^2) * O(n) to check size.
	- dp get size in O(1), but still check O(n2) ranges

Another DP solution?
- d[i] = max thing ending at index i, then d[i+1] = d[i] + A[i+1] or 0
	- just get max of that
	- O(n) time
	- O(1) aux space since we just need to keep the last one

"""

# Careful: what if all negative? cannot choose 0
# Best ending at i is either previous best + i or just i (don't use previous best)

def maxSubArray(nums):
	previousIndexBest = 0
	best = nums[0]
	for num in nums:
		# new is previousIndexBest + num or num
		previousIndexBest = num if previousIndexBest <= 0 else previousIndexBest + num
		best = previousIndexBest if previousIndexBest > best else best

		# previousIndexBest = max(previousIndexBest + num, num) # current best is now just using num, or previous
		# best = max(previousIndexBest, best) # if we add num, use previous index best + num. Else use 0
	
	return best


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
print(maxSubArray([-1]))

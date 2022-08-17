# Results:
# Runtime: 37ms 90.30%
# Memory Usage: 14MB 82.71%

"""
https://leetcode.com/problems/subsets/

nums of unique elements
return all possible subsets
soln cannot contain duplicate subsets

ideas:
- to iterate over subsets, just decide for each elt, is it in or out?
- can also maybe do DP wise, ie if you have all subsets from 0 to i, i+1 decide if in or out, and append to those.
- guaranteed to be unique!
- can dynamically build those subsets, not store at each stage. only store most recent stage
Time: O(num subsets) -> each subset added once
Space: O(num subsets)
already best we can do

notes: use + and += operators for arrays. more intuitive and easier.

"""

def getSubsets(nums):
	# start with 0 items
	allSubsets = [[]]
	# print(subset for subset in allSubsets)

	for i in range(len(nums)):
		allSubsets.extend([subset + [nums[i]] for subset in allSubsets])

	return allSubsets


print(getSubsets([1, 2, 3]))
print(getSubsets([0]))
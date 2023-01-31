# Results:
# Runtime: 29ms 95.32%
# Memory Usage: 14.1MB 32.53%

"""

https://leetcode.com/problems/subsets/

Need to return all subsets
- an iterative solution, add one element at a time? also no duplicate subsets
- can iterate, but how to avoid duplicates? - have a table for added already
- maybe at each level, keep an index of which one you added?
- choose 1, then get subsets of 2 and 3

1 2

1 - added 1
12 - added 2
1 - added 2 already
2

123
1
12
123
12 - 2, 3 already added
1 - 2,  already added
13 - 2 already added?

Idea 1: Generate sets num by num, and just add on. O(N*2^N), since O(N) to copy each subset
Idea 2: So okay to take O(N) time to build each subset. So do backtracking alg and build. Use indexes in order to prevent duplicates.


"""

def solve2(nums):
	out = [[]]
	curr = []
	def backTrackSearch(idx, curr):
		nonlocal out
		# create new subset
		curr += [nums[idx]]
		# add
		out += [curr[:]]
		# backtrack
		for newI in range(idx+1, len(nums)):
			backTrackSearch(newI, curr)
		# pop and return
		curr.pop()

	for start in range(len(nums)):
		backTrackSearch(start, curr)
	return out

print(solve2([1, 2]))

def solve(nums):
	out = [[]]
	for num in nums:
		out += [subset + [num] for subset in out]
	return out

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

Can you do backtracking iteratively?
- Yes, but you need to copy state. if you want to dynamically build the array, must be recursive since you need to know
- when your "dfs" part is done to remove.

Tactic: Either cascading, or recursive backtracking to save space. Think of it like a DFS. Backtrack - either add / don't add and bt 2x, or add a random one and bt once

"""

def solveBacktracking2(nums):
    state = []
    solns = []

    def backtrack(solns, state, i): # haven't added i yet
        solns.append(state.copy())

        for j in range(i, len(nums)):
            state.append(nums[j])
            backtrack(solns, state, j + 1)
            state.pop()

    backtrack(solns, state, 0)
    return solns



def solveBacktracking(nums):
    state = []
    solns = [[]]

    def backtrack(solns, state, i):
        # either add i, backtrack / dfs, and then remove

        if i + 1 < len(nums):
            backtrack(solns, state, i+1)

        state.append(nums[i])
        solns.append(state.copy())

        if i + 1 < len(nums):
            backtrack(solns, state, i+1)
        
        state.pop() # remove

    backtrack(solns, state, 0)
    return solns

# Idea: backtracking alg / search alg, either include or dont' include elt
# only copy to solution on add?
# okay soltuion first, build and add to state. only add new sets on add
# Cascading solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        state = [[]]

        for num in nums:
            toAppend = []
            for s in state:
                # add num
                sCopy = s.copy()
                sCopy.append(num)
                toAppend.append(sCopy)

            state.extend(toAppend)
        
        return state


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

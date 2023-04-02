# Results:
# Runtime: 32ms 93.12%
# Memory Usage: 14.1MB 88.55%

"""

https://leetcode.com/problems/subsets-ii/

- nums could contain duplicates
- Return all possible subsets

Ideas:

- how to avoid duplicate entries?
    - sort first. then do same idea as before, add one at a time at indexes.
    - Don't think we even need to sort?

Edge cases

all 2's 2 2 2 2 2 2 2
- ah, so we could add different 2's but still have same result.
    - so we need to figure out how many of each, O(n) skim, then at each step figure out how many we want to add.
- Backtrack on how many of each number we want to add

Time: O(n) + O(2^n)?

Better:
- First sort
- then do backtracking / dfs, but either you add the thing or you skip to the next value
- this generates all the solutions

Tactic: Either generate freq and pick next letter / do for all freq, or sort first and either add or skip to next letter without adding any.
 
"""

def solve(nums):
    nums.sort()

    def backtrack(solns, state, i):
        if i == len(nums):
            return

        # either add item, or skip to next
        # only if you add an item, add to solns
        state.append(nums[i])
        solns.append(state.copy())
        backtrack(solns, state, i+1)
        state.pop()

        # or skip to the next, without adding the item
        while i+1 != len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(solns, state, i+1)
    
    solns = [[]]
    backtrack(solns, [], 0)

    return solns


def solveInvalid(nums):
    nums.sort()

    def backtrack(solns, state, i):
        solns.append(state.copy())

        if i == len(nums):
            return

        # either add item, or skip to next
        state.append(nums[i])
        backtrack(solns, state, i+1)
        state.pop()

        # or skip to the next, without adding the item
        while i+1 != len(nums) and nums[i] == nums[i+1]:
            i += 1
        i += 1

        # then pick the next one to copy
        # this is actually the error. can't just pick randomly which one to add. will have duplication.
        for k in range(i, len(nums)):
            state.append(nums[k])
            backtrack(solns, state, k + 1)
            state.pop()

    solns = []
    backtrack(solns, [], 0)

    return solns
        

def solve(nums):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    
    uniqueNums = list(set(nums))

    solns = []

    def backtrack(state, i): # i is not added yet
        nonlocal uniqueNums

        # first add new valid state to output
        solns.append(state.copy())

        # then backtrack on the next number to add, and how many to add
        for k in range(i, len(uniqueNums)):
            numToAdd = uniqueNums[k]
            for _ in range(freq[numToAdd]):
                state.append(numToAdd)
                backtrack(state, k+1)
            for _ in range(freq[numToAdd]):
                state.pop()
            
    
    backtrack([], 0)

    return solns





        




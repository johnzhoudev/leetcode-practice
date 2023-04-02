"""

https://leetcode.com/problems/combination-sum-ii/

- nums, can contain dup, target
- each num can only be used once
- all combos that sum to target?

Idea:
- sort first
- backtracking on how many of a number you put in. Either you put in the number, or skip to next number.
    - avoids the duplication issue.

- Or generate frequency, then backtrack on amount / number of nums 
Time: O(n log n) + O(num combos, maybe 2^n)

Damn, not fast enough.

Idea2: 

"""

def solve(nums, target):

    nums.sort()

    solns = []

    def backtrack(state, rollingSum, i):
        nonlocal solns
        if rollingSum == target:
            solns.append(state.copy())
            return
        elif rollingSum > target or i >= len(nums):
            return
        
        # either add current num, or skip to next unique num

        # add current num, creates a new base
        state.append(nums[i])
        backtrack(state, rollingSum + nums[i], i+1)
        state.pop()

        # or don't add current num, and skip to next valid
        while i+1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(state, rollingSum, i+1)
    
    backtrack([], 0, 0)
    return solns

        





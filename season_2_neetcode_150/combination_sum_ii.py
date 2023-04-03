# Results:
# Runtime: 49ms 84.54%
# Memory Usage: 13.9MB 89.9%

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

- We are recursing on a lot of states where nothing was added. Instead, always be adding something in the new state

Tactic: Sort first, the backtrack either add curr or skip to next new number to avoid dupe. Tip, don't advance state without adding anything. always add, else recurse on lots of states with no addition.

"""

def solve(nums, target):

    nums.sort()

    solns = []

    def backtrack(solns, state, rollingSum, i):
        if rollingSum == target:
            solns.append(state.copy())
            return
        elif rollingSum > target or i >= len(nums):
            return
        

        for k in range(i, len(nums)):

            if rollingSum + nums[k] > target:
                break

            # either add current, or add a next
            # but add first in case of repeats.
            if k == i or nums[k] != nums[k-1]:
                state.append(nums[k])
                backtrack(solns, state, rollingSum + nums[k], k+1)
                state.pop()

    backtrack(solns, [], 0, 0)
    return solns

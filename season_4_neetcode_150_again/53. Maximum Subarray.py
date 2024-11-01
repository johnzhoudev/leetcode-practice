"""

53. Maximum Subarray

find subarray with largest sum and return?

Ideas:
- greedy approach
- either take current sum, or just the current value, whichever is larger

O(n)

Tactic:
Greedy, add to total if total + num >= total, else just take num

"""


def solve(nums):
    best = nums[0]
    total = nums[0]
    for num in nums[1:]:
        if total + num < num:
            total = num
        else:
            total += num
        
        best = max(total, best)
    return best
    
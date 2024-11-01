"""

1. Two Sums

indices of 2 nums st they add up to target
must be diff indices

Idea:
- hash table with remaining to idx
- 1 loop to compute remaining, then check

Tactic:
Use hash table to store complement (target - num) -> idx. 2nd pass, check for complement and idx not same.
"""

def solve(nums, target):
    negsums = {}
    for idx, num in enumerate(nums):
        negsums[target - num] = idx
    
    for idx, num in enumerate(nums):
        if num in negsums and negsums[num] != idx:
            return (idx, negsums[num])
        
    raise RuntimeError("No solution")
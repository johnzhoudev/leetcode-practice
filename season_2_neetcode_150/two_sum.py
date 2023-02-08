# Results:
# Runtime: 59ms 90.34%
# Memory Usage: 15.4MB 11.62%

"""

https://leetcode.com/problems/two-sum/

Classic question, array nums and int target
- 1st pass build hash table of numbers to reach target, and index of prev
    - as you build, keep checking. if a solution exists, you will create an entry for the first and the second should succeed.

Tactic: use hash map to map value needed
"""

def solve(nums, target):
    state = {}
    for idx, num in enumerate(nums):
        if num in state:
            return idx, state[num]
        else:
            state[target - num] = idx
    
    assert(False)

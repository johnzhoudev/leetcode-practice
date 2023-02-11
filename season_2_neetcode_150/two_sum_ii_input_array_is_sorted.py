# Results:
# Runtime: 142ms 37.84%
# Memory Usage: 14.9MB 84.39%

"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

1 index arr nums, sorted in non-decreasing (increasing)
find 2 nums adding to target
constant extra space

Ideas:
- for each num, binary search for next. O(nlogn)
- 2 pointers - slide together - O(n)


Tactic: 2 pointers, close in on target
"""

def solve(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:
        pivot = nums[left] + nums[right]
        if pivot == target:
            return [left + 1, right + 1]
        elif pivot < target:
            left += 1
        else:
            right -= 1
    
    raise RuntimeError()
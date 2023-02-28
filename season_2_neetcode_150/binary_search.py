# Results:
# Runtime: 246ms 71.63%
# Memory Usage: 15.5MB 61.62%

"""

https://leetcode.com/problems/binary-search/

binary search

"""

def solve(nums, target):
    # setup state
    left = 0
    right = len(nums) # exclusive

    while left < right:
        pivot = left + ((right - left) // 2) 
        if nums[pivot] < target: # go right
            left = pivot + 1
        elif nums[pivot] > target:
            right = pivot
        else:
            return pivot
    
    return -1


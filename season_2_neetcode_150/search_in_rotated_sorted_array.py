# Results:
# Runtime: 41ms 79.51%
# Memory Usage: 14.2MB 85.88%

"""

https://leetcode.com/problems/search-in-rotated-sorted-array/

ascendign order, distinct values
rotated by unknown amount
search for target

Ideas:
- 4 5 6 1 2 3 4

- without knowing pivot, can't tell given pivot if you should go left or right
- first search for min val in log(n) time, and index
- then search for val, using regular technique

Tactic: First find min. Then find target

"""

def solve(nums, target):
    # first find min
    left = 0
    right = len(nums) - 1

    while left < right:
        pivot = left + (right - left) // 2 # bias left
        if nums[pivot] <= nums[right]: # in order, min to left
            right = pivot
        elif nums[pivot] > nums[right]:
            left = pivot + 1
    
    minIdx = right

    # regular search
    left = 0
    right = len(nums) - 1
    while left <= right:
        pivot = left + (right - left + 1) // 2
        realPivot = (minIdx + pivot) % len(nums)
        if nums[realPivot] > target:
            right = pivot - 1
        elif nums[realPivot] < target:
            left = pivot + 1
        else:
            return realPivot
        
    return -1


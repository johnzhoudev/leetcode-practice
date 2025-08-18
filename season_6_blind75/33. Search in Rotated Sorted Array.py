"""


33. Search in Rotated Sorted Array


Array is rotated

search for target
sorted
distinct values

say you search
if pivot is bigger, on left or right if wraps around

Binary search to find pivot, then regular binary search with adjustment?

- if rightmost is smaller than pivot, go right
- if right is larger than pivot, go left
"""

def solve(nums, target):
    # first, find rotation

    def find_rotation(nums):
        if nums[0] <= nums[-1]:
            return 0 # No rotation

        left = 0
        right = len(nums) - 1
        rightmost = nums[-1]

        # Find point where left is larger than right
        while left < right:
            pivot = left + (right - left) // 2  # Bias left

            if rightmost < nums[pivot]: # go right
                left = pivot + 1
            else: # go left
                right = pivot
        
        assert left == right
        return left 
    
    start = find_rotation(nums)

    def get(idx):
        return nums[(idx + start) % len(nums)]
    
    # Regular binary search using adjusted idx
    left = 0
    right = len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        val = get(pivot)
        if val == target:
            return (start + pivot) % len(nums)
        elif val < target: # go right
            left = pivot + 1
        else:
            right = pivot - 1
    
    return -1
            




# Results:
# Runtime: 42ms 70.77%
# Memory Usage: 14.1MB 93.33%

"""

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

find minimum element
- don't know how many times rotated

Idea:
- binary search, consider 
larger end ... min ... smaller end
- pivot on left of min will be greater than right end
- pivot on right of min smaller than right end
- based on this, go right or left
- narrow down onto one elt, then good
- make sure don't disclude right end

- numbers are all unique. no duplicates, so easier. don't have to worry about not shifting.
- if numbers were not unique, could skip over pivot. can't binary search then.

Tactic: Binary search, based on pivot and right end. bias left and keep right vals
"""

def solve(nums):
    # binary search
    left = 0
    right = len(nums) - 1 # inclusive

    while left < right: # end when one number, left == right
        pivot = left + (right - left) // 2 # make sure can't freeze. bias left
        if nums[pivot] > nums[right]: # left of real val
            left = pivot + 1
        elif nums[pivot] <= nums[right]:
            right = pivot # still keep, inclusive

    return nums[right]


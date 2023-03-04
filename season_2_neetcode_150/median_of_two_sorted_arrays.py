# Results:
# Runtime: 94ms 73.23%
# Memory Usage: 14.3MB 16.84%

"""

https://leetcode.com/problems/median-of-two-sorted-arrays/

Final boss lets go

Idea:
1289
34567

1234
56789
- median is 5
- pretty much want to find 28 and 45
- binary search shorter one first

- pivot = the left value on each
    - edge case, whole array happens to be on right - can we pad arrays?
    - pad left and right with +- inf, so will always have pairs 
- if on right, pivot should be greater than right of other array
- if on right of target, pivot + 1 should be less than left of other array
- binary search


Tactic: Pad with -inf, inf, then binary search for 4elt mid. think out examples. edge case, only 1 elt
"""

def solve(nums1, nums2):
    if len(nums1) > len(nums2):
        temp = nums2
        nums2 = nums1
        nums1 = temp
    
    # edge case, only 1 elt. all other cases work with >=2 elts
    if (len(nums1) == 0 and len(nums2) == 1):
        return nums2[0]

    # nums1 now the shorter one
    nums1 = [float("-inf")] + nums1 + [float("inf")]
    nums2 = [float("-inf")] + nums2 + [float("inf")]

    # do binary search, pivot is left of pair
    left = 0
    right = len(nums1) - 2 # can't start at end

    pivot1 = -1
    pivot2 = -1

    while left <= right:
        pivot1 = left + (right - left) // 2 # bias left, doesn't matter
        # p1 + 1 + p2 + 1 = len // 2
        pivot2 = ((len(nums1) + len(nums2)) // 2) - 2 - pivot1

        if nums1[pivot1 + 1] < nums2[pivot2]: # too left, shift right
            left = pivot1 + 1
        elif nums1[pivot1] > nums2[pivot2 + 1]:
            right = pivot1 - 1
        else:
            # perfectly aligned. can return
            break

    mids = sorted([nums1[pivot1], nums1[pivot1 + 1], nums2[pivot2], nums2[pivot2 + 1]])
    if (len(nums1) + len(nums2)) % 2 == 0:
        return (mids[1] + mids[2]) / 2
    return mids[2]

"""

Keep making range larger

O(n)

"""


def solve(nums):
    largest = 0
    curr = 0

    while curr < len(nums) and curr <= largest and largest < len(nums) - 1:
        largest = max(largest, curr + nums[curr])
        curr += 1
    
    return largest >= len(nums) - 1
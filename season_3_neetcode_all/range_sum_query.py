"""
https://leetcode.com/problems/range-sum-query-immutable/

- given int array nums
- sum of elts  in nnuums between left and right indices inclusive

Idea:
- maintain cumulative sum of numbers
- for left to right, it's state[right] - state[left] (or 0)

"""

class NumArray:

    def __init__(self, nums):
        self.cumsum = []
        total = 0
        for x in nums:
            total += x
            self.cumsum += [total]

    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right] - (self.cumsum[left-1] if left-1 >= 0 else 0)
        
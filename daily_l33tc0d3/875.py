"""
https://leetcode.com/problems/koko-eating-bananas/

Idea:
- binary search on values, test if valid
- O(n log n)

"""
from math import ceil

def solve(piles, h):

    left = 1
    right = max(piles)

    def validate(piles, h, k):
        totalHours = 0
        for pile in piles:
            totalHours += ceil(pile / k)
            if totalHours > h:
                return False
        return True
            
    while left < right:
        pivot = left + (right - left) // 2 # bias left

        # if can fit, could be smaller so go left
        if (validate(piles, h, pivot)):
            right = pivot
        else: # cannot fit, go right
            left = pivot + 1
    
    return left

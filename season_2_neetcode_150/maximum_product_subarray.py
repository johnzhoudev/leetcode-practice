"""

https://leetcode.com/problems/maximum-product-subarray/


- find max subarray with max product of ints

Idea:
- calc all subarrays and products, O(n^3)

DP: product = prev product subarray * next, O(n^2) time, O(n^2) space

- isn't it just longest continuous sequence without containing a negative number or 0? - or no, could be 2 negatives make pos
- soln is between 0's, and is either everything (pos), or not including rightmost, or not including leftmost.
O(n)

Idea2: iterate thru, maintain max and min so far. On negative number, max becomes num * min, min becomes num * max

Tactic: keep large and small - largest / smallest prod up to last point. if num 0, reset large / small to 1. Take max.

"""

def solve(nums):
    res = max(nums)
    # large and small - what's the largest / smallest prod up to the last point?
    large = nums[0]
    small = nums[0]

    for num in nums[1:]:

        if num == 0:
            # reset large and small and skip. don't compare with res
            large = 1
            small = 1
            continue
        elif num < 0:
            oldl = large
            large = max(small * num, num)
            small = min(oldl * num, num)
        else:
            large = max(large * num, num)
            small = min(small * num, num)

        res = max(large, res)
    return res


def solve(nums):
    # max and min are for the set so far including at the number
    l = nums[0]
    s = nums[0]
    overallMax = nums[0]

    for num in nums[1:]:
        if num < 0:
            l = max(s * num, num)
            s = min(l * num, num)
        else:
            l = max(l * num, num)
            s = min(s * num, num)
        
        overallMax = max(l, overallMax)
    
    return overallMax
        
def solve(nums):
    left = 0
    right = 0 # inclusive

    maxProduct = nums[0]
    currProduct = nums[0]

    while left <= right and right < len(nums):

        # first, if right and left is at a 0, skip to next
        if left == right and nums[left] == 0 and nums[right] == 0:
            maxProduct = max(maxProduct, 0)
            right += 1
            left = right
            if right < len(nums):
                currProduct = nums[right]
        
        # if both right and left cannot advance (same as right), advance both
        elif left == right and (right+1 == len(nums) or nums[right+1] == 0): # advance onto 0
            left += 1
            right += 1
        # if right cannot advance, and can advance left, advance. Else if left same, advance both
        elif right+1 == len(nums) or nums[right+1] == 0:
            currProduct /= nums[left]
            left += 1
        # else advance right
        else:
            right += 1
            currProduct *= nums[right]

        maxProduct = max(maxProduct, currProduct)
    
    return int(maxProduct)



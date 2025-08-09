"""

Given integer array nums
find subarray with largest sum

Must be non-empty

Tactic: Sliding window, either take the number with the current or just take the number and start anew

O(n)

Challenge: Divide and conquer approach?


Divide and conquer
- Split to left and right
- need to know best of each side + best partial of left and best partial of right
    - so need to return total sum + best partial left + best partial right + best

Base case: 1 element
- total = elt, best partial left = elt or None, best partial right = elt or None, best = elt or None

- total = sum of a and b, best partial left = best partial left of left or all of left + best partial left of right or don't use
best = max best of left, best of right, best partial left + best partial right

"""

# def solve(nums):


def solve(nums):
    best = nums[0]
    total = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < total + nums[i]: # better to continue range
            total += nums[i]
        else: # Start anew
            total = nums[i]
        best = max(best, total)
    return best




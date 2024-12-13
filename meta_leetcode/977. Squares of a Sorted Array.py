"""

977. Squares of a Sorted Array

array of squares, sorted in non-decreasing order
- already sorted in non-decreasing order (inc)

Idea:
- find < 0 and >= 0 parts
    - compute squares while you go
- then mergesort the two arrays

O(n) time
O(n) space, can be done O(1) in place

Better: Go from ends, and order by largest then reverse at end! Genius

Tactic:
Go from ends, add larger squared number. Then reverse at end.

"""

def solve(nums):
    i1 = 0
    i2 = len(nums) - 1
    output = []

    while i1 <= i2:
        if nums[i1]**2 > nums[i2]**2:
            output.append(nums[i1] ** 2)
            i1 += 1
        else:
            output.append(nums[i2] ** 2)
            i2 -= 1
    
    return output[::-1]



def solve(nums):
    # square everything, also check when >= 0
    idx = len(nums)
    for i in range(len(nums)):
        if idx == len(nums) and nums[i] >= 0: idx = i
        nums[i] = nums[i] * nums[i]
    
    if idx == 0: # no neg numbers
        return nums
    
    # Now, mergesort in place
    i1 = idx - 1
    i2 = idx

    output = []
    # add in non-decreasing order
    while i1 >= 0 or i2 < len(nums):
        if i1 < 0:
            output.append(nums[i2])
            i2 += 1
        elif i2 >= len(nums):
            output.append(nums[i1])
            i1 -= 1
        elif nums[i1] < nums[i2]:
            output.append(nums[i1])
            i1 -= 1
        else:
            output.append(nums[i2])
            i2 += 1
    
    return output










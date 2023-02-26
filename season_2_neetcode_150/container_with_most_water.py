# Results:
# Runtime: 746ms 83.86%
# Memory Usage: 27.5MB 46.27%

"""

https://leetcode.com/problems/container-with-most-water/

Array of heights, representing walls
- get max area of water that can be stored

Idea:
Brute Force: for each pair, calculate and get max. O(n^2)

if both decreasing, shift the one that's smaller?

- In any case, you can only have a better area if the smaller side gets larger. 
- So just shift the smaller side, and check. and if same size, shift random

Tactic: Shift pointers by smaller height. for each state, to be bigger, smaller edge must get bigger

"""

def solve(heights):
    left = 0
    right = len(heights) - 1
    maxArea = 0

    while left < right:
        maxArea = max((right - left) * min(heights[left], heights[right]), maxArea)

        if (heights[left] < heights[right]):
            left += 1
        else:
            right -= 1
    
    return maxArea

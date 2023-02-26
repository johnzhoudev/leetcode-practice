# Results: solve2
# Runtime: 124ms 77.46%
# Memory Usage: 15.9MB 75.25%

"""

https://leetcode.com/problems/trapping-rain-water/

elevation map input
how much water can it trap?

Brute force:
- for each pixel, check left and right and see what's max. O(n*maxheight) * O(n)

Idea:
- record arrays, where val is highest wall right of point.
- same with left side
- then for each part, volume = min of the walls - value, and if neg, bad 
O(n) space and time. optimal

Better:
- Now we use 2 pointers. Trick here is, if the max we've seen on the left is smaller than the max 
we've seen on the right, then the left max determines the water level. and keep iterating until left 
max bigger than right

Tactic: either DP max height left right, or smarter 2ptr, water level limited by smaller of left / right max currently seen
"""

def solve2(heights):
    # setup state
    left = 0
    right = len(heights) - 1
    maxHeightLeft = heights[left]
    maxHeightRight = heights[right]
    total = 0

    while left <= right:
        if (maxHeightLeft < maxHeightRight):
            maxHeightLeft = max(maxHeightLeft, heights[left])
            # then current water determined by maxHeightLeft, for left
            total += maxHeightLeft - heights[left]
            left += 1
        else:
            maxHeightRight = max(maxHeightRight, heights[right])
            # use and advance right
            total += maxHeightRight - heights[right]
            right -= 1
    
    return total


def solve(heights):

    # setup state
    maxHeight = 0
    highestWallLeft = []
    for height in heights:
        highestWallLeft += [maxHeight]
        maxHeight = max(maxHeight, height)

    maxHeight = 0
    highestWallRight = [None for _ in range(len(heights))]
    for i in range(len(heights) - 1, -1, -1):
        highestWallRight[i] = maxHeight
        maxHeight = max(maxHeight, heights[i])
    
    # solve
    totalArea = 0
    for idx, height in enumerate(heights):
        left = highestWallLeft[idx]
        right = highestWallRight[idx]

        addedArea = min(left, right) - height
        if addedArea > 0:
            totalArea += addedArea
    
    return totalArea

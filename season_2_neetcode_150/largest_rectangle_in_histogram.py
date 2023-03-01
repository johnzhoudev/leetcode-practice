# Results:
# Runtime: 949ms 92.42%
# Memory Usage: 28.1MB 82.91%

"""

https://leetcode.com/problems/largest-rectangle-in-histogram/

Histogram

Idea:
- strafe right idea, mark every top as visited if you do. keep track of max.
Time: O(n^2) worst case, all ascending

Idea 2:
- use a decreasing stack, storing height and original start.
    - when you encounter larger stuff, push.
    - when smaller, pop until can fit, since those rectangles are ended

O(n) time
O(n) space worst case

Tactic: Stack, descending heights. iterate thru heights, pop heights larger and check maxArea. Careful finding startIdx and emptying stack at end
"""

def solve(heights):
    stack = [] # (height, idx)
    # invariant: we update maxArea when we pop from the stack, that way we cover everything
    maxArea = 0

    for idx, height in enumerate(heights):
        # remove all stuff larger on stack
        # also find start idx, since could start from one of the larger or equal to ones
        startIdx = idx
        while stack and stack[-1][0] >= height:
            otherHeight, startIdx = stack.pop() # since things added in idx order
            maxArea = max(maxArea, otherHeight * (idx - startIdx)) # check area of popped
        
        # Add current height to stack
        stack.append((height, startIdx))
    
    while stack:
        otherHeight, otherIdx = stack.pop()
        maxArea = max(maxArea, otherHeight * (len(heights) - otherIdx))

    return maxArea


# Time limit exceeded
def solveSlow(heights):
    # setup state
    visited = [False for _ in range(len(heights))]
    maxArea = 0

    # go thru
    for idx, height in enumerate(heights):
        if visited[idx]:
            continue

        # starting from a non-visited one, go as far right as you can
        currHeight = heights[idx]
        end = idx # exclusive
        while end != len(heights):
            # advance first by adding end
            currHeight = min(currHeight, heights[end])
            if currHeight == heights[end]:
                visited[end] = True
            end += 1
            maxArea = max(maxArea, currHeight * (end - idx))
    
    return maxArea
        


        

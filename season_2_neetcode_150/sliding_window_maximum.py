# Results:
# Runtime: 1752ms 76.23%
# Memory Usage: 29.6MB 97.5%

"""

https://leetcode.com/problems/sliding-window-maximum/

Idea:
Use a heap? Just maintain a max heap
- Nope. Heap only supports push and pop. Can't remove specific element.

time: O(n log k) for each operation
space O(k)

Idea 2: Use a deque, monotonically decreasing to keep track of maximum.
- pretty much, as you add new stuff, if it's bigger you can pop everything smaller since it'll 
always be part of the window

Tactic: Use a monotonic decrease deque to track max of window. each shift, pop from back until all smaller gone.
"""

from collections import deque

def solve(nums, k):

    # setup state
    queue = deque([nums[0]]) # monotonically decreasing. Left is max

    # load in first k numbers
    for i in range(1, k):
        # pop from back until larger
        while len(queue) > 0 and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])
    
    results = []
    # iterate thru, i is index of thing to add
    for i in range(k, len(nums) + 1):
        # process current window
        results.append(queue[0])

        if i == len(nums):
            return results

        # shift window
        if nums[i - k] == queue[0]:
            queue.popleft()
                
        # add next digit
        while len(queue) > 0 and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])
    
    raise RuntimeError()

        

        
        




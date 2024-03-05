"""

https://leetcode.com/problems/sliding-window-maximum/description/

- hashset of items in the range - so adding and removing O(1)
    - or defaultdict with count
- then also maintain a heap and pop when topmost not in set

O(n log k) amortized since each item is added and popped only once

Better: Monotonically decreasing queue. each time, pop all on right that are smaller then add to right.
- and if left is the largest, then pop it. All other large ones would have been popped by adding to right.

"""

from collections import defaultdict
from heapq import heappop, heappush

def solve(nums, k):
    def push(heap, x):
        heappush(heap, -x)
    def pop(heap):
        return -heappop(heap)
    def peek(heap):
        return -heap[0]

    # create hashset
    counts = defaultdict(lambda: 0)

    # create max heap
    heap = []

    for i in range(k):
        counts[nums[i]] += 1
        push(heap, nums[i])
    
    soln = [peek(heap)] # see largest elt

    # go thru
    for i in range(k, len(nums)):
        counts[nums[i - k]] -= 1
        counts[nums[i]] += 1
        push(heap, nums[i])

        while counts[peek(heap)] == 0:
            assert counts[peek(heap)] >= 0
            pop(heap)
        
        soln += [peek(heap)]

    return soln


# Better
from collections import deque

def solve(nums, k):
    window = deque() # monotonically decreasing

    def add(window: deque, x):
        # Remove all smaller than x on left
        while len(window) > 0 and window[-1] < x:
            window.pop()
        
        window.append(x)

    # Load deque
    for i in range(k):
        add(window, nums[i])
    
    soln = [window[0]]

    # now process all
    for i in range(k, len(nums)):
        num = nums[i]

        add(window, num)

        # remove - only matters if removing max, otherwise would already have been removed when adding max.
        if nums[i-k] == window[0]:
            window.popleft()

        soln.append(window[0])
    
    return soln

    



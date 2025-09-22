"""

239. Sliding Window Maximum

sliding window, return max as it slides

max heap, store value and index? keep popping stuff 

O(n log k) time

monotonically decreasing queue
- popleft all that are smaller and add element
- when leaving window, if that's the element, pop

O(n) time
"""
from collections import deque

def solve(nums, k):

    output = []

    mdq = deque()

    # add first k elements
    for i in range(k):
        num = nums[i]
        # add to queue
        while mdq and mdq[-1] < num:
            mdq.pop() # pop all elts smaller
        mdq.append(num)
    output.append(mdq[0])

    for i in range(k, len(nums)):
        num = nums[i]
        # add to queue
        while mdq and mdq[-1] < num:
            mdq.pop() # pop all elts smaller
        mdq.append(num)

        # pop last
        if nums[i - k] == mdq[0]:
            mdq.popleft()
        
        output.append(mdq[0])
    return output

        

    

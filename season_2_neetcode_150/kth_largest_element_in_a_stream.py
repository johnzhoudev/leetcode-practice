"""

https://leetcode.com/problems/kth-largest-element-in-a-stream/

- add, add elt to stream and return kth largest element

Ideas
- min heap of k items, add and get min 
O(log k) to add and get min

Tactic: Use min heap. edge case, may be init with one less element, then on add, becomes whole. 

"""

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = [] # min heap
        
        for num in nums:
            heapq.heappush(self.heap, num) 
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]



        

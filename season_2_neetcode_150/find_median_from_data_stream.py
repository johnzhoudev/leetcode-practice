"""

https://leetcode.com/problems/find-median-from-data-stream/

Idea:
- maintain 2 heaps, a max and min
- add to max, and if max has 2, pop and push to min
- Find median, and based on if < or > than median, add to left or right

Add - O(log n)
find median, O(1) just view root and len

Tactic: Use 2 heaps and balance between to find median.

"""

import heapq

class MedianFinder:

    def __init__(self):
        self.lower = [] # maxheap, 
        self.upper = [] # minheap

    def addNum(self, num: int) -> None:
        median = self.findMedian()

        if median and num > median: # add to upper
            heapq.heappush(self.upper, num)
        else: # num <= median
            heapq.heappush(self.lower, -num)
        
        if (len(self.lower) - len(self.upper) == 2):
            heapq.heappush(self.upper, -heapq.heappop(self.lower)) # transfer over
        elif (len(self.upper) - len(self.lower) == 2):
            heapq.heappush(self.lower, -heapq.heappop(self.upper)) # transfer over

    def findMedian(self) -> float:
        if len(self.lower) == 0: return None
        if len(self.lower) == len(self.upper):
            return (-self.lower[0] + self.upper[0]) / 2
        return -self.lower[0]

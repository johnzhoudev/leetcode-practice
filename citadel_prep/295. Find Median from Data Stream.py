"""

295. Find Median from Data Stream


use 2 heaps
kind of messy

"""

import heapq

class MedianFinder:

    def __init__(self):
        self.smaller = [] # has more or the same as larger. use neg values
        self.larger = []
        
    def addNum(self, num: int) -> None:
        if self.smaller and num > (-self.smaller[0]):
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.smaller, -num)
        
        # rebalance
        while not(len(self.smaller) - len(self.larger) == 1 or len(self.smaller) == len(self.larger)):
            if len(self.smaller) < len(self.larger):
                heapq.heappush(self.smaller, -heapq.heappop(self.larger))
            else:
                heapq.heappush(self.larger, -heapq.heappop(self.smaller))

    def findMedian(self) -> float:
        if (len(self.smaller) + len(self.larger)) % 2 == 0: # even, get both
            return (-self.smaller[0] + self.larger[0]) / 2
        else:
            return -self.smaller[0]

        
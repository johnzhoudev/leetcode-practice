"""

973. K Closest Points to Origin

Can i just use a heap?

Go thru, calc distance for all points
Then use heap 

O(n log k) time, O(k) space

Tactic:
Use heap.

"""

import heapq

def solve(points, k):

    heap = []

    def dist(x, y):
        return x**2 + y**2 # don't care abt sqrt

    for x, y in points:
        heapq.heappush(heap, (-dist(x, y), (x, y))) # min heap, so do neg dist to pop max
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [x[1] for x in heap]


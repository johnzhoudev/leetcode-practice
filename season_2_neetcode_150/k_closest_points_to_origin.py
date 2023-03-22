# Results:
# Runtime: 780ms 84.78%
# Memory Usage: 20.3MB 58%

"""

https://leetcode.com/problems/k-closest-points-to-origin/

- k closest points to origin

Idea:
- could just map to distance and sort, but that's n log n
- using heap, n log k

Tactic: heap faster than sorting. Careful, use max heap to keep smallest points
"""

import heapq

def solve(points, k):
    heap = [] # maxheap, keep closest points (smallest)
    distances = [x * x + y * y for x, y in points]

    for idx, dist in enumerate(distances):
        heapq.heappush(heap, (-dist, idx))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [points[idx] for dist, idx in heap]






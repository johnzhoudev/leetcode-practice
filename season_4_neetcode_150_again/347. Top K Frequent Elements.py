"""

347. Top K Frequent Elements


nums
k
return k most frequent elements

- heap
- count everything
O(n + n log k)

Tactic:
num counts, and use heap to get top k

"""

from collections import defaultdict
import heapq
def solve(nums, k):
    counts = defaultdict(lambda : 0)
    for num in nums:
        counts[num] += 1
    
    # now get top k
    heap = []
    for num in counts:
        heapq.heappush(heap, (counts[num], num)) # min heap, discards min!
        if (len(heap) > k):
            heapq.heappop(heap)
    
    return [num for _, num in heap]
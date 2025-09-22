"""

347. Top K Frequent Elements

nums, k
return k most frequent elements

count counts, then sort with heap

O(n) + O(n log k)

"""

from collections import Counter
import heapq

def solve(nums, k):
    counts = Counter(nums)

    heap = []
    for num, count in counts.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [x for _, x in heap]
    


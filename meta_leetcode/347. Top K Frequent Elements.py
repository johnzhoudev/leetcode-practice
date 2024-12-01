"""

347. Top K Frequent Elements


k most frequent elements
- just do frequency mapping, then heap 

O(n) time to make freq, O(x log k) time to get most frequent

Tactic:
Use a heap!

"""

from collections import defaultdict
import heapq

def solve(nums, k):
    counts = defaultdict(lambda : 0)

    for num in nums:
        counts[num] += 1
    
    heap = []
    for num in counts:
        heapq.heappush(heap, (counts[num], num))
        if len(heap) > k:
            heapq.heappop(heap) # get rid of the min / smallest element
        
    return [x[1] for x in heap]
        
    



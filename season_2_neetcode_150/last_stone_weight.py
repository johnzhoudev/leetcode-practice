# Results:
# Runtime: 36ms 45.78%
# Memory Usage: 13.9MB 50.59%

"""

https://leetcode.com/problems/last-stone-weight/

- given array of weights
- each turn, smash. if weights equal, both destroyed. else y = y - x
- what is weight of last remaining stone?

Edge Cases:
- end game with 1 stone
- end game with no stones, equal weight

Idea:
- pretty much have to simulate
- use max heap, pop 2 largest - O(log k) * num turns

Tactic: simulate, use max heap
"""
import heapq

def solve(stones):
    heap = [] # min, so use negative

    for stone in stones:
        heapq.heappush(heap, -stone)
    
    while len(heap) > 1:
        x = -heapq.heappop(heap)
        y = -heapq.heappop(heap)
        if x == y: continue
        x -= y
        heapq.heappush(heap, -x)
    
    return -heap[0] if len(heap) > 0 else 0

    


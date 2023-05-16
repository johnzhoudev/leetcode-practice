"""

https://leetcode.com/problems/minimum-interval-to-include-each-query/

size of interval is right - left + 1

queries array
- want to find size of smallest interval i s.t. query value contained in i. else -1
- everything is too big to hash.

Brute force: O(nq), check each interval

Operations
- sorting intervals, O(n log n)

- say you were able to look up 

Idea:
- Preprocess intervals to make non-overlapping intervals, and interval index
    - put all intervals into min heap start time, with size and index too.
    - extract interval, check if overlaps 
    - if no overlap, add and continue
    - if overlaps out
        - if new larger or equal, cut and put new 2nd back in
        - if new smaller, cut last interval and add new interval, but don't put anything back
    - if overlaps in
        - must be smaller, cut previous, put new, and put rest back in with size
- then do binary search on big part

"""

import heapq

def solve(intervals, queries):
    minIntervals = []
    for idx, (f, t) in enumerate(intervals):
        heapq.heappush(minIntervals, (f, t, idx, t - f + 1)) # left, right, i, size
    
    newIntervals = []
    while minIntervals:
        f, t, idx, size = heapq.heappop(minIntervals) 

        if not newIntervals:
            newIntervals.append((f, t, idx))
        
        lastF, lastT, lastIdx, lastSize = newIntervals[-1]

        # now go thru cases
        # 1. No overlap
        if lastT < f: # strictly less
            newIntervals.append((f, t, idx, size))
        # 2. overlap outwards, strict
        elif f <= lastT and t > lastT:
            if size < lastSize:
                newIntervals.pop()
                if (f-1) - lastF + 1 > 0:
                    newIntervals.append((lastF, f-1, lastIdx, lastSize))
                newIntervals.append((f, t, idx, size))
            else: # don't, just cut and add back 
                heapq.heappush(minIntervals, (lastT+1, t, idx, size))
        # overlap inwards
        elif f <= lastT and t <= lastT:
            # must be smaller, or equal. So just replace
            newIntervals.pop()
            if (f-1) - lastF + 1 > 0:
                newIntervals.append((lastF, f-1, lastIdx, lastSize))









    
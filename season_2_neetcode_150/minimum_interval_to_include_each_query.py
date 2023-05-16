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
- Scrap, too hard to code

Idea 2:
- From neetcode, had to look it up
- Sort intervals and queries
- then go interval by interval and add them to a heap
    - if interval left of point, drop
    - if interval contains point, add
    - if interval right of point, leave
- Then, pop from heap until top has min size and also includes interval
    - tiebreakers, by endpoint? **
    - and output that

Tactic: Tricky q. sort intervals and queries and go in order. put intervals in heap while q inside, then pop from heap if interval not in. remove by endpoint tiebreaker.
"""

import heapq

def solve(intervals, queries):
    # first sort intervals and queries
    intervals.sort(key=lambda x : x[0])

    # need to keep track of index
    output = [-1 for _ in range(len(queries))]
    queries = [(q, idx) for idx, q in enumerate(queries)]
    queries.sort()

    # create heap and state
    smallest = []

    # go thru main while loop
    currIdx = 0
    for q, idx in queries:

        # first, add all relevant intervals
        # add all intervals that contain q, and drop all that are before
        while currIdx < len(intervals) and intervals[currIdx][0] <= q:
            interval = intervals[currIdx]

            # if interval left of q, drop
            # if interval[1] < q:
            #     currIdx += 1

            # if interval contains q, add
            if interval[0] <= q and interval[1] >= q:
                heapq.heappush(smallest, (interval[1] - interval[0] + 1, interval[1])) # size, endpoint (tiebreaker)

            currIdx += 1

        # while does not contain q
        # smallest contains all that start before q, so just check end
        while smallest and smallest[0][1] < q:
            heapq.heappop(smallest)
        
        if smallest:
            output[idx] = (smallest[0][0])
        # else:
            # output.append(-1)
    
    return output


        



    




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









    
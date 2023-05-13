"""

https://leetcode.com/problems/non-overlapping-intervals/

Ideas:
- greedy? go thru, and remove interval that overlaps with the most intervals?
    - but how to determine?
- overlap count? remove until overlap count is 0 for all remaining

O(n^2), go thru and for each interval, count how many it overlaps with. store.

- every interval, either choose to keep it in or to remove it 
    - search alg, keep and remove all else?
    - is there any way to tell which one to remove? unless you do some preprocessing
    - Maybe do some DP, dp[i] = best way to add all intervals up to i without overlap
    - dp[i] = either don't use i and add dp[i-1], or keep i and add first one that doesn't overlap with i (since would have to remove all)
- O(n log n) to sort
- then build hash table or array to store index after which no overlap O(n log n)
- then do dp backwards, O(n)

so total O(n log n)

Simpler
- Sort, then if overlap with last, add one with smallest endpoint

Tactic: O(nlogn) sort, go thru, if overlap, choose to add interval with least end point.

"""

def solve(intervals):
    intervals.sort(key=lambda x : x[0])

    # now, keep track of last added thing and go thru..
    lastEnd = intervals[0][1]
    numDeleted = 0

    for idx, [start, end] in enumerate(intervals):
        if idx == 0: continue
        
        if lastEnd <= start:
            # new one
            lastEnd = end
        else: # overlaps
            numDeleted += 1
            lastEnd = min(end, lastEnd)
    
    return numDeleted

        

        





import heapq

def solve(intervals):
    # first, sort
    intervals.sort(key=lambda x : x[0])

    # Then, build table where last index no overlap
    nextIndex = [(-1, -1) for _ in range(len(intervals))] # -1 means no other one. 2nd space is the number of intervals skipped
    # use a heap? min heap
    ends = []
    for idx, [f, t] in enumerate(intervals):
        # first, add current interval
        heapq.heappush(ends, (t, idx))

        # if, at this idx, the end is <= the front, set index
        while ends and ends[0][0] <= f: 
            end, index = heapq.heappop(ends)
            nextIndex[index] = (idx, idx - index - 1)
    
    # now, do dp
    dp = [float('inf') for _ in range(len(intervals))]
    dp[-1] = 0 # don't need to remove anything for the last

    for i in range(len(intervals) - 2, -1, -1):
        # case 1, remove it. then one less + 1
        # case 2, don't remove it. then must remove all within
        if nextIndex[i][0] != -1:
            dp[i] = min(dp[i+1] + 1, nextIndex[i][1] + dp[nextIndex[i][0]])
        else:
            dp[i] = dp[i+1] + 1
    
    return dp[0]



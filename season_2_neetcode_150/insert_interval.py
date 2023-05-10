"""

- given bunch of intervals, sorted by ascending order by start
    - non-overlapping
- newInterval - rep start and end of another interval

Ideas:
- brute force easy, just go thru and when you see overlapping intervals, accumulate. Just add to new list

- binary search for start interval, perhaps.

- since all intervals non-overlapping, 
    - just need to find the interval this lands on and left is min(left, intervalleft) and right is similar
    - just need to get leftmost interval with a piece in it (guaranteed only 1 at most)
    - and rightmost interval with a piece in it
    O(n log n)

Finalized Idea:
- Do binary search on left to get largest left that is outside of interval, and if contained then merge. else use left bound (others must be within)
- do 2nd binary search on right to get largest left still within right bound. if ends within new range, save. merge.
- use memory to just add intervals as they come?
- removing might still take O(n) time. or if add one at a time, still O(n)!

So perhaps, first try just simple method. Check intervals. If contained, dont' add. else add

Edge case: what if you just need to insert the interval?
- so if not inserted yet and next start is past end, just insert.
- also if no elements in array, just insert at end if not inserted yet.

Better:
- just do it in 3 parts:
1. add all intervals before new interval
2. go thru and while overlapping, combine intervals
3. add all remaining

Tactic: Keep it straightforward, do in 3 parts. Add all before, merge and add middle, then add all remaining. 
"""

def solve(intervals, newInterval):
    # step 1, add intervals before new interval
    i = 0
    output = []
    while i < len(intervals) and intervals[i][1] < newInterval[0]: # end is < than start
        output.append(intervals[i])
        i += 1
    
    # combine intervals that overlap (until start > end)
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    output.append(newInterval)

    # add remaining intervals
    while i < len(intervals):
        output.append(intervals[i])
        i += 1
    
    return output

    

def solve(intervals, newInterval):
    output = []
    ns, ne = newInterval
    insertedYet = False
    for start, end in intervals:
        if not insertedYet and start > ne:
            output.append([ns, ne])
        elif not (end < ns or start > ne):
            # contained within
            ns = min(start, ns)
            ne = max(end, ne)
            if not insertedYet:
                insertedYet = True
                output.append([ns, ne])
            else:
                output[-1] = [ns, ne]
        else:
            output.append([start, end])

    if not insertedYet:
        output.append([ns, ne])
    return output


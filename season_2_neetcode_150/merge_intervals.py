"""

https://leetcode.com/problems/merge-intervals/

- merge all intervals in the input

Ideas:
- input is not sorted... can we do without?

- easy way:
- sort by start
- iterate thru and while overlaps with next, merge. then output once no overlap.

Is there an O(n) soln? if unsorted, hard to know. non-triv.
- could maybe use a hash table, somehow? but since intervals, hard to tell. What if some overlap but non have common values?
say 1,3 and 2,4. How would you be able to konw they overlap, without sorting?
Yeah, sort

Better: add first, then for all subsequent, if start is less than prev end, update end
"""

def solve(intervals):
    output = []
    intervals.sort(key=lambda x : x[0])
    output.append(intervals[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] <= output[-1][1]:
            output[-1][1] = max(output[-1][1], intervals[i][1])
        else:
            output.append(intervals[i])
    return output




def solve(intervals):
    output = []
    intervals.sort(key=lambda x : x[0])

    mergeleft, mergeright = -1, -1
    for i in range(len(intervals)):
        left = intervals[i][0]
        right = intervals[i][1]

        # interval overlapping with last
        if not (right < mergeleft or left > mergeright):
            mergeleft = min(mergeleft, left)
            mergeright = max(mergeright, right)
            output[-1] = [mergeleft, mergeright]
        else: # not overlapping, reset
            mergeleft = left
            mergeright = right
            output.append([left, right])
    
    return output


            
        



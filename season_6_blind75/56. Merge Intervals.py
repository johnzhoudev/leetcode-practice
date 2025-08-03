"""

56. Merge Intervals

merge all overlapping intervals

Sort intervals by start point, keep largest end point and if start > end, add interavl

O(n log n)

Tactic: Sort by start, and go thru. If overlap, add largest endpoint. If start > end, add interval.
"""

def solve(intervals):
    intervals.sort(key=lambda x: x[0])
    output = []
    i_start, i_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= i_end: # Overlapping
            i_end = max(end, i_end)
        else: # start > i_end
            output.append((i_start, i_end))
            i_start = start
            i_end = end
    return output + [(i_start, i_end)]
            




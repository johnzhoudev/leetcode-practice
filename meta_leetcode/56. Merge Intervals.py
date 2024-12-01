"""

56. Merge Intervals

Sort by end

go thru, if overlap with previous, merge. Keep stack.

O(n log n)

Sort by start????
Then only check last one!!!

Tactic:
Sort by START, then add (and if overalpping with prev in result, merge)

"""

def solve(intervals):
    intervals.sort()

    result = [intervals[0]]

    for x1, x2 in intervals[1:]:
        if x1 <= result[-1][1]: # overlap
            y1, y2 = result.pop()
            result.append((y1, max(x2, y2)))
        else:
            result.append((x1, x2))
    
    return result
            




def solve(intervals):
    intervals.sort(key=lambda x : x[1]) # sort by end

    output = [intervals[0]]

    for x1, x2 in intervals[1:]:
        # continue popping until no overlap
        while output and x1 <= output[-1][1]: # overlapping
            y1, y2 = output.pop()
            x1 = min(x1, y1)
            x2 = max(x2, y2)

        else: # not overlapping, so just append
            output.append((x1, x2))
    
    return output






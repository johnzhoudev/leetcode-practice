"""

56. Merge Intervals


not sorted list of intervals, merge

Idea:
- sort first by start
- append function checks last interval and merges if necessary
O(n log n) for sort

"""

def solve(intervals):
  intervals.sort()
  result = []
  for start, end in intervals:
    if not result:
      result.append([start, end])
      continue
  
    # non empty, check end 
    s, e = result[-1]
    # if overlap, merge
    if e < start:
      result.append([start, end])
    else:
      result.pop()
      result.append([min(s, start), max(e, end)])
  return result

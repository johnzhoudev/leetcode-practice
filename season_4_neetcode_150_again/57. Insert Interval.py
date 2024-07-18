"""

57. Insert Interval


sorted ascending intervals by start
- insert interval
- merge if overlap

Idea:
- to insert, it's O(n)
- so just go thru and merge when necessary, then insert

- isOverlap - and merge, always check with alst

- Damn, that was bad.

Better: go in groups. collect left, then overlapped, then right.


Tactic: Collect left, and collect right. Else must be in between, do min max. Combine after.
"""

def solve(intervals, newInterval):
  s, e = newInterval
  left = []
  right = []
  for start, end in intervals:
    if end < s: # to left
      left.append([start, end])
    elif e < start:
      right.append([start, end])
    else: # must be overlapped
      s = min(s, start)
      e = max(e, end)
  
  return left + [[s, e]] + right


def solve(intervals, newInterval):

  def isOverlap(start1, end1, start2, end2):
    if start1 > start2:
      return isOverlap(start2, end2, start1, end1)
    
    return end1 >= start2
    
  def appendToResult(start, end):
    if not result:
      result.append([start, end])
      return

    start2, end2 = result[-1]

    if isOverlap(start, end, start2, end2):
      result.pop()
      result.append([min(start, start2), max(end, end2)])
    else:
      result.append([start, end])


  result = []
  newStart, newEnd = newInterval
  isAppended = False
  for start, end in intervals:
    if isAppended:
      appendToResult(start, end)
      continue
    
    if end < newStart: # before
      appendToResult(start, end)
    elif isOverlap(start, end, newStart, newEnd):
      # combine and merge
      appendToResult(min(start, newStart), max(end, newEnd))
      isAppended = True
    else: # must be after, so append 
      appendToResult(newStart, newEnd)
      appendToResult(start, end)
      isAppended = True

  if not isAppended:
    result += [[newStart, newEnd]]

  return result

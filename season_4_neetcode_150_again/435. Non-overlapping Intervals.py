"""

435. Non-overlapping Intervals

min to remove to make rest non-overlapping

Idea:
- greedy, remove intervals overlapping the most
- sort by start, and then end
- if overlap, going thru sorted by start, remove the one with the furthest end (affects more)

- technically can sort by end and greedily take

"""

def solve(intervals):
  intervals.sort(key = lambda x : x[1]) # sort by end
  prevS, prevE = intervals[0]
  numRemoved = 0
  for start, end in intervals[1:]:
    # if not overlapping
    if start >= prevE:
      prevS = start
      prevE = end
      continue # no overlap
    else:
      # already taken by sort one with end
      numRemoved += 1
  
  return numRemoved

def solve(intervals):
  intervals.sort() # sort by start
  prevS, prevE = intervals[0]
  numRemoved = 0
  for start, end in intervals[1:]:
    # if not overlapping
    if start >= prevE:
      prevS = start
      prevE = end
      continue # no overlap
    else:
      if end < prevE: # remove end
        prevS = start
        prevE = end
      numRemoved += 1
  
  return numRemoved
    

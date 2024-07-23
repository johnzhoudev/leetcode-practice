"""

sort intervals and queries
put intervals into heap by start location, and pop by size
if point not in heap interval, pop interval
go until done

n intervals m points

Time: O(n log n) + O(m log m) + O(m log n)

Tactic: Sort intervals and queries, put intervals into heap and pop when not in range of query
"""
import heapq
from collections import defaultdict

def solve(intervals, queries):
  intervals.sort(reverse=True) # smallest at end, so easy to pop
  oldQueries = [x for x in queries]
  queries.sort()

  def intervalContains(q, interval):
    return interval[0] <= q and q <= interval[1]
  
  def intervalLen(interval):
    return interval[1] - interval[0] + 1

  # now go thru
  results = defaultdict(lambda : -1)

  intervalsHeap = [] # (size, left, right)
  for q in queries:
    # add any valid intervals
    while intervals and intervals[-1][0] <= q: # start less than q
      interval = intervals.pop()
      heapq.heappush(intervalsHeap, (intervalLen(interval), interval))
    # Remove invalid intervals and add
    while intervalsHeap and not intervalContains(q, intervalsHeap[0][1]):
      heapq.heappop(intervalsHeap)
    if intervalsHeap:
      results[q] = intervalsHeap[0][0]
  
  resultsArr = [results[q] for q in oldQueries]
  return resultsArr


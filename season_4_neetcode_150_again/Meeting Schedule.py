"""

https://neetcode.io/problems/meeting-schedule

ordered list of meetings
- can person attend all meetings?
- non inclusive ends

Tactic: Just go thru, check if start time is after previous end time, sorted
O(nlogn)
"""

def solve(intervals):
  intervals = [(interval.start, interval.end) for interval in intervals]
  intervals.sort()
  lastEnd = None
  for start, end in intervals:
    if lastEnd:
      if start < lastEnd: return False
    lastEnd = end
  return True


"""

https://neetcode.io/problems/meeting-schedule-ii

- find min number of days / rooms to schedule all without conflicts

Ideas:
- Greedy approach?
- sort in ascending order by end time, then by start time
- keep array of last meetings, each time you can't schedule, add a new column
- to schedule meeting, schedule where possible with largest end time (most optimal) - keep in a heap?


Tactic: Sort in ascending by end time and start time, keep heap of meeting end times and append to largest end time possible
"""

import heapq

def solve(intervals):
  intervals = [(interval.start, interval.end) for interval in intervals]
  intervals.sort(key=lambda x : (x[1], x[0])) # should sort wrt end, then start

  # Now, greedy
  rooms = [] # keep maxheap of largest end times (endtime)
  for start, end in intervals:
    poppedRooms = []
    while rooms and -rooms[0] > start:
      poppedRooms.append(heapq.heappop(rooms))
    if rooms:
      # Append to top room
      heapq.heappop(rooms)
      heapq.heappush(rooms, -end)
    else:# add a new room
      heapq.heappush(rooms, -end)
    for room in poppedRooms:
      heapq.heappush(rooms, room)
  
  return len(rooms)

    

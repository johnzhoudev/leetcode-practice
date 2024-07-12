"""

https://leetcode.com/problems/minimum-number-of-refueling-stops/description/

target miles east
stations = [position east, fuel]
startFuel

Min stops?

Ideas:
- max range?

- brute force, search alg try all combos of gas stations, O(2^n)
- to stray from optimal, discard one gas station and you can't reach another
- Greedy? Or DP?

- maybe maintain ranges and number of gas stations required to get there
- get max gas station and slowly extend range? keep heap of stuff? - greedy, choose which gas stations to visit

Tactic: Greedy, use heap to always extend range with max gas reachable

"""

import heapq

def solve(target, startFuel, stations): # stations is sorted
  numStations = 0
  maxRange = startFuel

  fuelHeap = []
  notAddedYetIdx = 0

  # Load start stations
  for (position, fuel) in stations:
    if position > startFuel: break
    heapq.heappush(fuelHeap, -fuel) # Minheap, so get neg
    notAddedYetIdx += 1

  while fuelHeap and maxRange < target:
    newFuel = -heapq.heappop(fuelHeap)
    numStations += 1
    maxRange += newFuel

    # Add stations and range
    while notAddedYetIdx < len(stations) and stations[notAddedYetIdx][0] <= maxRange:
      heapq.heappush(fuelHeap, -stations[notAddedYetIdx][1])
      notAddedYetIdx += 1

  return numStations if maxRange >= target else -1

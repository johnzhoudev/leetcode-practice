# Results:
# Runtime: 892ms 93.91%
# Memory Usage: 36.3MB 46.45%

"""

https://leetcode.com/problems/car-fleet/

target miles away
position and speed of n cars

once catch up with car, become convoy
how many convoys reach the end?

Idea:

compute time to reach destination for each car
- all cars in fleet will have position behind lead car, and time finishing before lead car
- so just need to store lead car position and time
- lead car could also become convoy for another car too - then need to re-eval all convoys
- but can't become a lead car for a convoy and also hit another convoy in the same move.

Brute force: keep array of convoys, for each car check if it's part of a convoy.
O(n^2) time, O(n) space
Maybe improve to O(n log n) if we maintain sorted order and do binary searches

Is this optimal? could we do a monotonic stack here?
yolo

Optimization 2: get rid of leading case by inserting always in order of position

Optimization 3: Since we're doing it by sorted order, we don't need to check every covoy. just the convoy
right in front of it.

O(n log n) to sort, plus O(n) to go thru

Tactic: Sort by position and iterate thru going away from target, only comparing with furthest convoy. car mergest with convoy if position before and finish time before. also only keep latest

"""

# optimized, don't use stack, just keep latest and count
# didn't actually optimize much. sorting the array and making a tuple copy takes the most memory

def solve2(target, position, speed):
    posSpeed = [(position[i], speed[i]) for i in range(len(position))]
    posSpeed.sort(key=lambda x : x[0], reverse=True) # sorted descending in terms of position

    convoyPos, convoySpeed = posSpeed[0]
    convoyTime = (target - convoyPos) / convoySpeed
    numConvoys = 1

    for i in range(len(position)):
        pos, speed = posSpeed[i]
        time = (target - pos) / speed

        if not (pos <= convoyPos and time <= convoyTime):
            numConvoys += 1
            convoyPos, convoyTime = pos, time

    return numConvoys
        


def solve(target, position, speed):
    posSpeed = [(position[i], speed[i]) for i in range(len(position))]
    posSpeed.sort(key=lambda x : x[0], reverse=True) # sorted descending in terms of position

    convoys = [] # (position, finishTime). Ordered so top is furthest convoy from target

    for i in range(len(position)):
        pos, speed = posSpeed[i]
        time = (target - pos) / speed

        if not convoys:
            convoys.append((pos, time))
            continue

        convoyPos, convoyTime = convoys[-1]
        if not (pos <= convoyPos and time <= convoyTime):
            convoys.append((pos, time)) # becomes its own convoy

    return len(convoys)
        



                



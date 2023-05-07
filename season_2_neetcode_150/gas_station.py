"""

https://leetcode.com/problems/gas-station/

- n gas stations in circle
- gas at ith station is gas[i]
- no limit to gas tank
- cost[i] gas to travel from i to i+1
- begin journey with empty tank at on of gas stations

- given gas and cost arr, return index of start if possible to travel
    - travelling: get gas at station, and travel to next in row. Deduct gas. Gas balance must always be positive.

Ideas:
- pick arbitrary start point, and have 2 ptrs front and back. 
- if have gas, go forward
- if have negative gas or cannot, backpedal until you do
O(n)

Proof correctness: if pick soln start, will always have gas. If not, eventually hit point where you don't have enough gas. then go left until.

- if you reach right and still have negative balance, then -1. No possible start
    - if start == end, and not possible.

2 3 4
3 4 3

start + m mod n = end mod m
end - start mod n = m mod n

0 1 2 3
start = 3, end = 1

Tactic: pick arbitrary. start and end ptrs. invariant, b/w start and end, have added end gas but haven't stepped yet. distance modulo. Careful with currBalance. if can go, ++end. Else --start.
"""

def solve(gas, cost):
    start = 0
    end = 0 # inclusive
    currBalance = gas[0]
    n = len(gas)

    # distance
    def d(start, end):
        if end >= start:
            return end - start + 1
        else:
            return (end - start + 1) + n

    # invariant: if node in range, means we are trying to step from end and have already reached start
    # at start, already processed gas 0
    while d(start, end) < n:
        if currBalance >= cost[end]:
            currBalance -= cost[end]
            end += 1
            currBalance += gas[end]
        else:
            # try at different start
            start -= 1
            if start < 0:
                start = n + start
            currBalance += gas[start] - cost[start] # could be negative, in which case we can continue going backwards
    
    # so now take last step
    if currBalance < cost[end]:
        return -1
    return start
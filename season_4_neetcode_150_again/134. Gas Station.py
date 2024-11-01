"""

134. Gas Station

n gas stations, circular route
- costs[i] of gas to get to next station

- can start at any station, but start with 0 gas
- return starting station if possible to do a loop, or -1

Ideas:
- like jump game
- go thru, and if hit a gas station that is unreachable, start at that gas station and go again
    - no, have to implement going backwards...?
O(n)

- 2 methods
- go forwards - sub cost, and add gas
- can go forwards - cost <= currGas
- go backwards - add gas, sub cost
    - keep going until gas amount >= 0
    - if never 0, then false

Simpler idea:
- go from start. if can't reach next, then all in chain are bad. then try again from next. 
- if next can reach the end and back around, then all good as long as total surplus larger than 0
- if next stops again, 

- If total amount of gas is >= total cost, then a solution exists.
    - why? if there's a thing you can't cross, that means net gas of traversing from any point is negative.
    - thus, for every segment of places you can't cross, net gain is negative so total must be negative.

Tactic:
Simplest way: sum of gas - cost >= 0 => solution, since if there's a thing you can't cross then traversing that segment is neg.
So just check if soln exists, then go thru and if you can't pass over, restart from next.
Else, can do forward and backwards stepping. remember, going backwards don't re-add gas if already visited (start)

"""

def solve(gas, cost):
    if sum(gas) - sum(cost) < 0: return -1

    #otherwise a solution must exist, so go until you can't cross and find

    start = 0
    currGas = 0
    for i in range(len(gas)):
        currGas += gas[i] - cost[i]
        if currGas < 0: # bad advance from i to i+1
            currGas = 0
            start = i + 1
    
    return start



def solve(gas, cost):

    currGas = -1
    currIdx = -1
    goalIdx = -1
    # first find valid goal and curr to take 1st step
    for i in range(len(gas)):
        if gas[i] >= cost[i]:
            currIdx = (i + 1) % len(gas)
            goalIdx = i
            currGas = gas[i] - cost[i] + gas[currIdx]
    
    if currGas == -1: return -1 # impossible

    def inc():
        nonlocal currIdx
        currIdx = (currIdx + 1) % len(gas)
    
    def dec():
        nonlocal goalIdx
        if goalIdx == 0: goalIdx = len(gas) - 1
        else: goalIdx -= 1

    def canGoForwards():
        nonlocal currIdx
        return cost[currIdx] <= currGas

    def goForwards():
        nonlocal currIdx
        nonlocal currGas
        assert(canGoForwards())
        currGas -= cost[currIdx]
        inc()
        currGas += gas[currIdx]
    
    def goBackwards():
        nonlocal currGas
        nonlocal goalIdx
        dec()
        currGas -= cost[goalIdx]
        if goalIdx != currIdx: currGas += gas[goalIdx] # only add gas if gotten before
    
    while True:
        if currIdx == goalIdx:
            return goalIdx if currGas >= 0 else -1

        if canGoForwards(): goForwards()
        else: goBackwards()

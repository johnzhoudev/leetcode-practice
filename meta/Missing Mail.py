"""

Missing Mail

- shipment schedule v of money
- can pay c dollars to go into room and remove packages
- probability s it will get stolen afterwards

maximum expected profit?

Simple case:

[10, 2]
theft chance = 0.5

if enter on first day, 100% chance 10 is there. So expected profit is 10
if enter on 2nd day, 100% chance 2 is there, 50% chance 10 is there.
So expected profit is 10*.5 + 2

Some dynamic programming thing?

depending on what you chose before, chance of having a package is diff

Entering a room restarts the state

states[i] = max expected profit if i was the last room you entered, what's the best?
states[i+1] = max(states[j] for j <= i + expected profit of room i+1)
- room i+1 profit will be the residuals + day i

get max

Tactic:
states[i] = max expected profit if i was last room u entered. states[i+1] = max prev states + residual + v[i+1] - c, return max.

"""

def solve(n, values, cost, stealProb):
    expectedProfits = []

    for v in values:
        bestExpectedProfit = 0

        # iterate backwards to build steal probabilities
        remainingProb = 1 - stealProb
        stolenResiduals = 0 # expected values of stuff before taken
        for i in range(len(expectedProfits) - 1, -1, -1):
            bestExpectedProfit = max(bestExpectedProfit, expectedProfits[i] + stolenResiduals)
            stolenResiduals += values[i] * remainingProb
            remainingProb *= (1 - stealProb)
        
        bestExpectedProfit = max(bestExpectedProfit, stolenResiduals) # didn't take at all case

        # now add current
        expectedProfits.append(bestExpectedProfit + v - cost) # looked
    
    return max(max(expectedProfits), 0)
        

N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.5
print(solve(N, V, C, S))
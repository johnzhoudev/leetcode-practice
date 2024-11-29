"""

n competitors
solve programming problems
points 1 or 2 for a problem

ith competitor has score si


minimum number of problems in the contest?

Must be possible to make the scores on the scoreboard

Greedy? just add necessary to make score?
- have set of all possible sums, adding will create more

Every odd number can be attained by evens + 1

so if all even, just largest / 2
if odd, still largest - 1 / 2



"""
def solve(n, s):
    isOdd = False
    for x in s:
        if x % 2 == 1:
            isOdd = True
    largest = max(s)
    return (largest // 2) + (1 if isOdd else 0)

    
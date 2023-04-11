"""

https://leetcode.com/problems/min-cost-climbing-stairs/

- cost i = cost of stepping at step i
- cost 0 or 1 start
- step 1 or 2

- min cost of getting to top?

- si = min cost of getting to stair i
- si = min(si-1 + ci-1, si-2 + ci-2)

Tactic: si = min cost getting to stair i, si = min(si-1 + ci-1, si-2 + ci-2)
"""

def solve(cost):
    s0 = 0
    s1 = 0
    for x in range(2, len(cost) + 1):
        tmp = min(s1 + cost[x-1], s0 + cost[x-2])
        s0 = s1
        s1 = tmp
    return s1
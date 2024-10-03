"""

746. Min Cost Climbing Stairs

cost - cost of ith step on staircase
- once pay cost, can either climb 1 or 2 steps
- start on step 0 or step 1

min cost to reach top of floor?

dp[i] = min cost to get to i
dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

"""

def solve(cost):
    n = len(cost)
    state = [0 for _ in range(n + 1)]
    state[0] = 0
    state[1] = 0

    for i in range(2, n + 1):
        state[i] = min(state[i-1] + cost[i-1], state[i-2] + cost[i-2])
    
    return state[n]
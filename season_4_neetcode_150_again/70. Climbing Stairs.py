"""

70. Climbing Stairs

n steps reach top
either climb 1 or 2 steps
how many distinct ways to climb to top

dp[i] = num ways to get to i
dp[i] = dp[i-1] + dp[i-2]
"""

def solve(n):
    state = [0 for _ in range(n + 1)]
    # base cases
    state[0] = 1
    state[1] = 1

    for i in range(2, n+1):
        state[i] = state[i-1] + state[i-2]
    return state[n]


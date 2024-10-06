"""

inf num each kind of coin
fewest coins to make amt
-1 of not

Knapsack?


dp[i] = least ways to make sum i
dp[i] = min(1 + dp[i-c1], 1+dp[i-c2], etc)

O(ncoins * sum)

Tactic:
DP on amount, backpack problem. s[x] = fewest coins making amount x, s[x] = min(s[x - coin]) over all coins

"""

def solve(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]

    # base cases
    dp[0] = 0

    for total in range(1, len(dp)):
        minCoins = float('inf')
        for c in coins:
            if total - c < 0: continue
            minCoins = min(minCoins, 1 + dp[total - c])
        
        dp[total] = minCoins

    return dp[amount] if dp[amount] != float('inf') else -1



"""

coins, different denominations, infinite number of each
amount

ret num combos to make up amount
else 0

Brute force:
- search alg
- dfs(quantity remaining, k idx of coins left to use) = number of ways to get to the end with the coins
- avoid duplicate ie we use coin 1, then 2, then 1 again vs 1 1 2

- so at each step, either use coin k or use another one

Bottom up?
dp[coins][amt] = num ways to get to amt using coins (0 to coins)

- either use the coin or don't
dp[coins][amt] = dp[coins-1][amt] + dp[coins][amt - coin val]

O(amount * coins)

Tactic:
knapsack: dp[coinidx][amt] = num ways to get amt using coins[0:coinIdx]. either use coin or don't. Sum up ways. 
can do dfs with memo, but slower? 
Can also optimize with 1d dp, for each coin and each subamt, dp[subamt] += dp[subamt - coin]. accumulates ways. Smart!

"""

# TLE
def solve(amount, coins):
    cache = {}

    def dfs(amt, coinIdx): # using coins[coinIdx:]
        # when do we break
        if amt > amount: return 0
        if amt == amount: return 1 # 1 way

        if (amt, coinIdx) in cache: return cache[(amt, coinIdx)]

        # now we handle main cases
        # amt < amount
        # try each coin!
        numWays = 0
        for nextCoinIdx in range(coinIdx, len(coins)):
            numWays += dfs(amt + coins[nextCoinIdx], nextCoinIdx)
        
        cache[(amt, coinIdx)] = numWays
        return numWays
    
    return dfs(0, 0)


def solve(amount, coins):
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

    # base cases, 
    for i in range(len(coins)):
        dp[i][0] = 1 # 1 way to make a sum of 0
    
    # dp step

    for coin in range(len(coins)):
        for amt in range(1, amount + 1): # Don't touch base cases
            # either use the coin, or don't
            if coin - 1 >= 0:
                dp[coin][amt] += dp[coin-1][amt]
            
            if amt - coins[coin] >= 0:
                dp[coin][amt] += dp[coin][amt - coins[coin]]
    
    return dp[-1][-1]

"""
dp represents all the ways to get to a specific amount between 0 and amount
for each new coin, add that to each subamount in increasing order. So handles multiple added coins.

wow!

"""
def solve(amount, coins):
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1 # 1 way for nothing

    for coin in coins:
        # for each coin, we're adding the number of ways to reach a specific sum with that coin
        for subAmt in range(coin, amount + 1):
            dp[subAmt] += dp[subAmt - coin]
    
    return dp[-1]
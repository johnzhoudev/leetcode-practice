"""

309. Best Time to Buy and Sell Stock with Cooldown

prices [i]
- after sell, cannot buy the next day (cooldown 1 day)
- buy 1 share and sell 1 share

Idea:

Brute force?:
- search alg, buy a certain day vs sell
- O(2^n)
- repeating work!

dp?
- dp[i][buy/sell] = best profit you could do up until day i, rdy to buy or sell?
- dp[i] = buy and sell 

Maybe compute deltas
deltas[k] = best i to sell at to maximize profit?
    - but maybe not if you can make multiple transactions

Ideas:
- dfs with memoization
- (day i, can BUY or SELL)
- dfs(i, BUY / SELL) - give max profit from that
O(n) time

- Alternative, is state machine
    - 3 possible states
    - get best profit at each state
    - 3 states (buy mode, sell mode, cooldown mode), and actions aren't determined by value 
        - so just take max value of any of the 3 states


Tactic:
dfs with memoization. (day, BuyState or SellState) is key. O(n). Can also use state machine...

"""

def solve(prices):
    # Init states
    buyState = 0
    sellState = float('-inf') # can't be in sell state unless bought already, so buy first elt
    cooldownState = 0

    for price in prices:
        # either chill, or come from cooldown
        newBuyState = max(buyState, cooldownState)
        newSellState = max(sellState, buyState - price) # either chill, or buy something
        newCooldownState = sellState + price # sell!

        buyState = newBuyState
        sellState = newSellState
        cooldownState = newCooldownState

    return max(buyState, sellState, cooldownState)


def solve(prices):
    cache = {}

    # give me the best profit if you're on day I and in the buyOrSEll mode
    def dfs(i, shouldBuy):
        
        if i >= len(prices): return 0 # can't do anything

        # Cache check
        if (i, shouldBuy) in cache: return cache[(i, shouldBuy)]

        bestProfit = 0

        if shouldBuy:
            # either wait, or buy right now
            bestProfit = max(dfs(i+1, True), dfs(i+1, False) - prices[i])
        else:
            # sell - either wait, or sell now
            # Handle cooldown
            bestProfit = max(dfs(i+1, False), dfs(i+2, True) + prices[i])
        
        cache[(i, shouldBuy)] = bestProfit

        return bestProfit

    return dfs(0, True)








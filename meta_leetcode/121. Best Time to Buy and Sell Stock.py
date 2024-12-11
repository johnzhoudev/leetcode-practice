"""

121. Best Time to Buy and Sell Stock

single day to buy and sell (in future)

Iterate backwards, best time to buy

Tactic:
Iter backwards, track max price

"""

def solve(prices):

    maxPrice = prices[-1]
    bestProfit = 0

    for i in range(len(prices) - 1, -1, -1):
        maxPrice = max(maxPrice, prices[i])
        bestProfit = max(bestProfit, maxPrice - prices[i])
    
    return bestProfit





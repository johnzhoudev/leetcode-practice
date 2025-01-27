"""

121. Best Time to Buy and Sell Stock

single day to buy, diff to sell
- backwards

"""

def solve(prices):
    bestSell = prices[-1]
    bestProfit = 0
    for i in range(len(prices)-1, -1, -1):
        bestSell = max(bestSell, prices[i])
        bestProfit = max(bestProfit, bestSell - prices[i])
    return bestProfit
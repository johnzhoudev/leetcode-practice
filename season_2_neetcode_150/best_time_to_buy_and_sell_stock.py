# Results:
# Runtime: 1136ms 43.39%
# Memory Usage: 25MB 32.74%

"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


single day to buy, and single day to sell
prices[]

Idea: iterate backwards, highest sell day, check profit. 

"""

def solve(prices):

    maxProfit = 0
    maxPriceSeen = prices[-1]

    for price in reversed(prices):
        maxPriceSeen = max(price, maxPriceSeen)
        maxProfit = max(maxProfit, maxPriceSeen - price)
    
    return maxProfit


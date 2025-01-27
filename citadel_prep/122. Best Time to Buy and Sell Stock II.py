"""

122. Best Time to Buy and Sell Stock II

can only hold once, but can buy and sell

just ride all high waves - any time it goes up, buy and sell. going down, don't

"""

def solve(prices):
    total = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:
            total += prices[i+1] - prices[i]
    return total
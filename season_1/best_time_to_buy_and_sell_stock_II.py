# Results:
# Runtime: 134ms 16.62%
# Memory Usage: 15.3MB 25.39%

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

prices
on each day, can choose to buy or sell. can hold at most 1 share at any time.
Max profit?

Ideas:
- Can make multiple trades: DP solution?
- can't consider just the best day to sell. have to consider all days selling. anytime you have a profit.
- from back, d[i] = max profit you can make if you start on day i 
- d[i] = max d[i+1] (don't buy), buy i and any time you make profit selling + d[post sell]
Time: O(n^2) solution. Can we do better? Greedy soln? - no. can't tell if you take the profit trade or not, without knowing others.


Brute force: O(n^2) time to generate all profit selling trades, then string together the max.

TODO:
- O(n) solution
- Basically just need to catch all the upticks. 
- if next is higher than current, buy current and sell at next price.
	- else, can still buy current but "sell" at current price

Tactic: Think graphically. Maximize profit by getting all upticks.
"""

def maxProfit2(prices):
	# setup state
	totalProfit = 0

	# from 0 to 2nd last
	for i in range(len(prices) - 1):
		if (prices[i] < prices[i + 1]):
			totalProfit += prices[i + 1] - prices[i]
	
	return totalProfit

# Time limit exceeded.
def maxProfit1(prices):
	# setup state
	bestProfit = [0 for _ in range(len(prices) + 1)] # account for overflow if you sell on last day

	for buyDay in range(len(prices) - 2, -1, -1):

		# if we buy at i, any time we can make a profit, check
		for sellDay in range(buyDay + 1, len(prices)):
			profit = prices[sellDay] - prices[buyDay] 
			if (profit > 0):
				bestProfit[buyDay] = max(profit + bestProfit[sellDay + 1], bestProfit[buyDay])
		
		# also check if we don't buy
		bestProfit[buyDay] = max(bestProfit[buyDay], bestProfit[buyDay + 1])

	return bestProfit[0]






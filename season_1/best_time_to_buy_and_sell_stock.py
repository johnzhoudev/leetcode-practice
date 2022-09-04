# Results:
# Runtime: 963ms 99.13%
# Memory Usage: 25.1MB 38.20%

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

prices[i] is price on ith day
choose day to buy, and day after to sell.

- return max profit. if all descending, can make no trades, 0. 

Ideas:
- Maybe we can do some DP solution? clear

- Brute force: For each day, scan after and choose lowest and max. O(n^2)
- O(n) minimum to read all values.

Idea:
- iterate from right and Store highest selling points for each day. Then check against day price.
Time: O(n) 
Space: O(1) if we just keep the min rolling

Tip for efficiency: Minimize array accesses and use array enumeration
"""

# optimized
def maxProfit3(prices):
	maxSeen = prices[len(prices) - 1]
	maxProfit = 0

	for price in prices[:-1:-1]:
		if (price > maxSeen):
			maxSeen = price

		if (maxSeen - price > maxProfit):
			maxProfit = maxSeen - price

	return maxProfit


def maxProfit1(prices):
	# setup state
	maxPriceSeen = 0
	maxProfit = 0

	for i in range(len(prices) - 1, -1, -1):
		maxPriceSeen = max(prices[i], maxPriceSeen)
		maxProfit = max(maxPriceSeen - prices[i], maxProfit)
	
	return maxProfit


# OLD SUBMISSION
def maxProfit2(prices):

	# Safety check
	if (len(prices) <= 0):
		return 0

	# Create highest price array
	# highestPriceAfterDay = [0 for i in range(len(prices))]

	# Poplate highest price after day 
	# [2 3 4 1 5 7 3 2]
	maxSeen = prices[len(prices) - 1]
	maxProfit = 0

	for i in range(len(prices) - 1, -1, -1):
		if (prices[i] > maxSeen):
			maxSeen = prices[i]

		if (maxSeen - prices[i] > maxProfit):
			maxProfit = maxSeen - prices[i]

	return maxProfit

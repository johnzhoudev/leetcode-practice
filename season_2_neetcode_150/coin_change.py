"""

https://leetcode.com/problems/coin-change/

- fewest num of coints to make up amount
- given denominations, and amoutn

Idea:
- search alg, choose amount of next coin to add
    - goes thru all possible combos, O(num combos < amount)
    - since 12 denoms, could easily be greater than O(10^4)
Space: O(combo)

DP: s[x] = fewest coins to make up to amount x
s[x] = min(s[x-coin denom])
O(amount, 10^4)
Space: O(amount)

Tactic: DP on amount, backpack problem. s[x] = fewest coins making amount x, s[x] = min(s[x - coin]) over all coins
"""

def solve(coins, amount):
    state = [-1 for _ in range(amount+1)] # -1 indicates no way to make this sum
    state[0] = 0
    # base case:
    for i in range(0, amount + 1):
        for coin in coins:
            prevSum = i - coin
            if prevSum < 0 or state[prevSum] == -1:
                continue
            if state[i] != -1:
                state[i] = min(state[i], state[prevSum] + 1) # adding 1 coin
            else:
                state[i] = state[prevSum] + 1
    
    return state[amount]




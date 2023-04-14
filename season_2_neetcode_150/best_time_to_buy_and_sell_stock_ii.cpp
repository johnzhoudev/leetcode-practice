/*

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


- prices i, price on day
- after you sell, cannot buy on the next day

Ideas:

- could do search algorithm, either buy, wait or sell on any given day

DP: if you buy on day i and sell on day j, maxProfit on that day is that + max profit if sold 1 day before.

state[i] = max profit if last sale is sold on or before day i 
state[i] = max(states[0 - i-1], states[0 - i-1] + (pricei - pricek)) // buy on day i, sell on day k

O(n^2) time

Idea 2: 
- there are 3 states, buy hold or sell.
- you can just track the max profit in each of these states as you iterate thru

- like search algorithm - check out each state, and realize if you reach a state on iteration i, can just take max. 
- then 3 total states.

- Alternatively, just do search alg but cache with buy or sell bool, and index 

Tactic: dfs search alg, with memoization. state is (index, isBuy or isSell). If selling on day i, + price to dfs result and same with buying

*/
#include <map>
using namespace std;

typedef pair<int64_t, bool> key;

class Solution {
public:

    // prices, cache, i, buySellBool
    // At each state, if in buy state, either buy or don't. Also 
    int64_t dfs(vector<int> &prices, map<key, int64_t> &cache, int i, bool isBuy, int64_t currPrice) {
        if (i >= prices.size()) {
            return 0; // no profit from this
        }

        // If contained, just return value
        if (cache.count(key(i, isBuy)) == 1) {
            return cache.at(key(i, isBuy));
        }

        // Else go thru cases and store max
        // 1. don't do anything

        int64_t cooldown = dfs(prices, cache, i+1, isBuy, currPrice);

        if (isBuy) {
            // buy current
            int64_t buy = dfs(prices, cache, i+1, false, currPrice) - prices[i]; // simulate buy, lose money
            cache[key(i, isBuy)] = max(buy, cooldown);
        } else {
            // sell current now, next is delayed to next next day
            int64_t sell = dfs(prices, cache, i+2, true, currPrice) + prices[i]; // simulate sell, gain prices
            cache[key(i, isBuy)] = max(sell, cooldown);
        }

        return cache[key(i, isBuy)];

    }

    int maxProfit(vector<int>& prices) {
        map<pair<int64_t, bool>, int64_t> state;

        return dfs(prices, state, 0, true, 0);
    }
};
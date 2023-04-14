/*

- can you make amount using unlimited coins?
- return number of ways to make up amount, or 0

Idea:
- search alg? adding each type and amount at a time?
    - but could have lots of duplication if same coins add to same amount

- search alg with memoization? if you get to a state, how many ways to make rest of sum?
    - problem is that could be updated, 

Idea:
- knapsack problem, cache number of ways to make up a sum using coins 0 to i
- O(coins * amount) time
- state[i][amt] = sum(state[i-1][amt], state[i-1][amt - val[i]]) // either use coin or don't, and many times
- base case, state[all][0] = 1

- *** But the thing is in calculating, we've calculated state[i][prev sums] already

- slow, must iterate thru many states since could use coin multiple times.

Tactic: Knapsack. s[i][amt] = ways using coins 0-i to make amt. s[i][amt] = s[i-1][amt] (don't use) + s[i][amt - coin[i]]

*/

#include <vector>
using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> state(coins.size() + 1, vector<int>(amount + 1, 0));

        // base case
        for (int i = 0; i <= coins.size(); i++) {
            state[i][0] = 1;
        }

        // dp
        for (int i = 1; i <= coins.size(); i++) {
            for (int amt = 1; amt < amount + 1; amt++) {

                if (amt - coins[i-1] >= 0) {
                    state[i][amt] = state[i-1][amt] + state[i][amt - coins[i-1]];
                } else {
                    state[i][amt] = state[i-1][amt];
                }
            }
        }

        return state[coins.size()][amount];
    }
};
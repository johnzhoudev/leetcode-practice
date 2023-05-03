/*

- Add + or - in front of each num
- return number of different expressions you could build which eval to target

Idea: 01Knapsack?
- could have pos or neg, but this is bounded.
- s[i][amt] = num ways to use 0-i to work up to amount
- s[i][amt] = s[i-1][amt - xi] + s[i-1][amt + xi], either add amt + or -

Search alg with memoization
- each state is + or -
- cache s[i][amt], which in total gives O(n * sum(items)) - but could have pos or neg sum
    - represents number of ways to get from s[i][amt] to target

Tactic: dp/dfs with memoization, 01 knapsack. s[i][amt] = num ways to get amt

jsut use vector.

*/

class Solution {
public:

    // haven't used i yet
    int dfs(vector<int> &nums, int *state, int i, int currAmt, int target, int col) {
        // First, if out of bounds, return
        if (i >= nums.size()) {
            return currAmt == target ? 1 : 0; // if at end, then check if you're at the target.
        }

        // if cached, return cache val
        if (state[i*col + currAmt] >= 0) {
            return state[i*col + currAmt];
        }

        // Else handle and continue dfs
        // either add or subtract current number
        int ifAdd = dfs(nums, state, i+1, currAmt + nums[i], target, col);
        int ifSub = dfs(nums, state, i+1, currAmt - nums[i], target, col);

        state[i*col + currAmt] = ifAdd + ifSub;
        return state[i*col + currAmt];
    }
    
    int findTargetSumWays(vector<int>& nums, int target) {
        int total = accumulate(nums.begin(), nums.end(), 0) + 1;

        int state[nums.size()][total * 2]; // middle is halfway point, we start at total
        memset(state, -1, sizeof(int) * nums.size() * total * 2);

        return dfs(nums, &state[0][0], 0, total, target + total, total * 2);
    }
};

/*
#include <map>
using namespace std;

typedef pair<int, int> key;

class Solution {
public:

    // haven't used i yet
    int dfs(vector<int> &nums, map<key, int> &state, int i, int currAmt, int target) {
        // First, if out of bounds, return
        if (i >= nums.size()) {
            return currAmt == target ? 1 : 0; // if at end, then check if you're at the target.
        }

        // if cached, return cache val
        if (state.count(key(i, currAmt)) > 0) {
            return state[key(i, currAmt)];
        }

        // Else handle and continue dfs
        // either add or subtract current number
        int ifAdd = dfs(nums, state, i+1, currAmt + nums[i], target);
        int ifSub = dfs(nums, state, i+1, currAmt - nums[i], target);

        state[key(i, currAmt)] = ifAdd + ifSub;
        return state[key(i, currAmt)];
    }
    
    int findTargetSumWays(vector<int>& nums, int target) {
        int total = 0;
        for (auto num : nums) {
            total += num;
        }

        map<key, int> state; // map of key to num ways 

        return dfs(nums, state, 0, 0, target);
        // return state[nums.size()][target];
    }
};
*/

// Try 2
/*

return num expr you can build that eval to target

- 0, 1 knapsack, 
- each elt either add or subtrack from sum
- can you get to target

dp[i][w] = using elts 0 to i-1, can we make a sum of weight w?
- max weight is either +- sum of all weights

dp[i][w]
- either subtract item i, so dp[i-1][w-i]
- or add item i, so dp[i-1][w+i]
Base case: dp[0][0] = true, dp[0][x] anything else false

- also need to count, so it's numways

*/
#include <vector>

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {

        int maxSum = 0;
        for (auto num : nums) {
            maxSum += num;
        }

        vector<vector<int>> dp(nums.size() + 1, vector<int>(2 * maxSum + 1, 0)); // weight = i - maxSum

        // base case
        dp[0][maxSum] = 1;
        // everything else false

        // Goal: find if dp[nums][maxSum + target] == True

        for (int i = 1; i <= nums.size(); i++) {
            for (int j = 0; j < 2 * maxSum + 1; j++) {
                dp[i][j] = 0;

                if (j-nums[i-1] >= 0) {
                    dp[i][j] += dp[i-1][j-nums[i-1]];
                }

                if (j+nums[i-1] < 2 * maxSum + 1) {
                    dp[i][j] += dp[i-1][j+nums[i-1]];
                }
            }
        }

        return dp[nums.size()][maxSum + target];

        
    }
};
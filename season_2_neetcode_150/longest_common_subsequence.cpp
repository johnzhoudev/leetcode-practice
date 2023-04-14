/*
https://leetcode.com/problems/longest-common-subsequence/description/

- return length of longest common subsequence

Brute Force: get every subsequence and cross reference? 2^n

DP: one letter at a time

- base case, 0, last added -1

Tactic: dp[x][y] = subsequence length x / y chars in. dp[x][y] = dp[x-1][y-1] if nx == ny (use), else dp[x][y] = max(dp[x-1][y], dp[x][y-1])
*/
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    // void debug(vector<vector<pair<int, int>>> &state) {
    //     for (int w = state.size()-1; w >= 0; w--) {
    //         for (int h = 0; h < state[w].size(); h++) {
    //             cout << "(" << state[w][h].first << "," << state[w][h].second << ") ";
    //         }
    //         cout << endl;
    //     }
    //     cout << endl;
    // }

    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.length();
        int m = text2.length();

        int state[text1.length()+1][text2.length()+1]; // init to 0

        for (int nidx = 1; nidx < n+1; nidx++) {
            for (int midx = 1; midx < m+1; midx++) {
                // if equal, use prev
                if (text1[nidx-1] == text2[midx-1]) {
                    state[nidx][midx] = state[nidx-1][midx-1];
                } else {
                    state[nidx][midx] = max(state[nidx-1][midx], state[nidx][midx-1]);
                }
            }
        }

        return state[n][m];

    }
};

// class Solution {
// public:
//     int longestCommonSubsequence(string text1, string text2) {
//         int n = text1.length();
//         int m = text2.length();

//         vector<vector<pair<int, int>>> state(n, vector<pair<int, int>>(m, pair<int, int>(0, -1)));

//         for (int nidx = 0; nidx < n; nidx++) {
//             char c = text1[nidx];
//             // walk thru all chars in text2 and see if matches
//             for (int midx = 0; midx < m; midx++) {
//                 // If c equals and position after last added, add.
//                 if (c == text2[midx] && state[nidx-1][midx].second < midx) {
//                     state[nidx][midx].first = state[nidx-1][midx].first + 1;
//                     state[nidx][midx].second = midx;
//                 } else {
//                     state[nidx][midx] = state[nidx-1][midx]; // same as without char in n
//                 }
//             }
//         }

//         return state[n-1][m-1].first;
//     }
// };
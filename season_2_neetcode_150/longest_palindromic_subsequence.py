"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Longest palindromic subsequence
- subsequence - delete some or no elements
- needs to be palindromic?


eg. bbbab

Idea:
- 2d dp, and build from centre. how long is the palindromic subsequence from dp[start][end]
- dp[i][j] = dp[i+1][j-1] + 2 if sides equal else 0
    - what if you miss one?
        - if you build from small to big, you're fine. would have already considered all smaller ones, so no way to build with smaller.

WRONG
- dp[i][j] = max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1] + 2 if sides equal else 0)
"""

def solve(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    # base cases
    for x in range(len(s)):
        dp[x][x] = 1 # 1 letter is a palindrome
    
    # main solve. solve each size at a time
    # k is number of advances, so size is k + 1. from 2 to len(s)-1
    for k in range(1, len(s)):
        for start in range(0, len(s)-k):

            if (start+1) <= start+k-1: # not 2x2
                dp[start][start+k] = dp[start+1][start+k-1] # equals prev, else 0

            if s[start] == s[start+k]:
                dp[start][start+k] += 2
            
            dp[start][start+k] = max(dp[start][start+k], dp[start][start+k-1], dp[start+1][start+k])
    
    return dp[0][len(s)-1]



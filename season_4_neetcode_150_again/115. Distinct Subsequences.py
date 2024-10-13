"""

115. Distinct Subsequences

s and t
number of distinct subsequences equalling

Brute Force:
- take all subsequences of s and compare to t
- O(2^n) where n is len of s

- rpt work? 
- if subsequence s[0:k] fits t[0:r], still going to have to recalculate a lot of stuff
if there's another way to get t[0:r] from s[0:k]. count each thing once for ever time
we fit the rest of the string. so better to just cache that value and use it again?


dp[i][k] = number of ways you can form subsequences from s[0:i-1] to fit t[0:k-1]
- either you use the ith value or not
dp[i][k] = dp[i-1][k] + dp[i-1][k-1] (if s[i] == t[k])

base cases:
- dp[0][0] = 1

O(nm) time to solve!

Tactic:
dp[i][k] = num ways s[0:i-1] subsequences make t[0:k-1]. Either use or don't 
dp[i][k] = dp[i-1][k] + dp[i-1][k-1] (if s[i] == t[k])
"""

def solve(s, t):
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)] # dp[i][k] = s[0:i-1] and t[0:k-1]

    # base case
    for i in range(len(s) + 1):
        dp[i][0] = 1

    # dp step
    for i in range(1, len(s) + 1): # using 1st term
        for k in range(1, len(t) + 1): # not empty
            dp[i][k] = dp[i-1][k] + (dp[i-1][k-1] if s[i-1] == t[k-1] else 0)
    
    return dp[-1][-1]


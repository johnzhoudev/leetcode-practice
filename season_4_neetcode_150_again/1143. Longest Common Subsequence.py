"""

1143. Longest Common Subsequence

- two strings
- what is the lnogest subsequecne
    - can delete elements, but have to be in order

Brute force way:
- test every subsequence and see if it's a subsequence in the next
    - O(2^n) * O(n) (to verify)

DP?
- dp[i][j] = longest subsequence starting s[i] ending s[j] present?
- dp[i][j] = longest subsequence of elements starting from 0, i in s1 and 0, j in s2, and ending in s[i] and s2[j]

either use element in subsequence or not

- dp[i][j] = max(dp[i-k][j - l] + 1) for each s[k] == s2[l]
    - largest subsequence 

- dp[i][j] = max dp[i-1][k] or dp[i][k-1] or dp[i-1][k-1] if s[i]==s2[k]
- dp = best longest subsequence using terms up to i and k for s and s2
O(n^2)

Tactic:
dp[i][j] = longest subsequence using elts s[0:i] an s2[0:j], but may or may not include i or j. dp[i][j] = max(dp[i-1][j], dp[i][j-1], 1 + dp[i-1][j-1] if s1[i]==s2[j])
"""

def solve(text1, text2):
    n = len(text1)
    m = len(text2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)] # add +1 to allow for -1 entries

    # Base cases 
    dp[0][0] = 1 if text1[0] == text2[0] else 0

    # DP
    for i in range(len(text1)):
        for j in range(len(text2)):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], 0 if text1[i] != text2[j] else 1 + dp[i-1][j-1])
    
    return dp[n-1][m-1]


print(solve())
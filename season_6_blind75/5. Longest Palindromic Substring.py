"""

idea: 
- O(n^2) go thru each, smallest first
- do dynamic programming

Better: Expand from center

"""


def solve(s: str):
    n = len(s)

    dp = [[False for _ in range(n)] for _ in range(n)] # Start stop inclusive

    # Base cases
    for start in range(n):
        dp[start][start] = True # 1 letter always palindromic
    best = 0, 0
    
    for start in range(n-1):
        if s[start] == s[start + 1]:
            dp[start][start + 1] = True
            best = start, start+1
    
    # Now for dp
    for length in range(2, n): # Length diff, so start + length = end
        for start in range(n - length):
            end = start + length
            if s[start] == s[end] and dp[start + 1][end - 1]:
                dp[start][end] = True
                best = start, end
    
    return s[best[0]:best[1]+1]
    



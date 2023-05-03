"""

https://leetcode.com/problems/regular-expression-matching/

. matches any char
* matches 0 or more of the preceding element
- given s, and p pattern

Brute Force
- go thru p and match, and if encounter ., parse any char, and if encounter *,
then do backtracking and match as many as possible, then less, then etc.

Ideas:
- hint is 2d dp
- dp[x][y] = does s[:x+1] match p[:y+1]
- dp[x][y] = 
    - if p[y] is alphabet or ., check if matches + dp[x-1][y-1]
    - if p[y] is *, 
        - use *, so check if p[y-1] matches s[x] and check dp[x-1][y] (use again) or dp[x-1][y-2]    
        - or 
        - don't use *, check dp[x][y-2]

Tactic: dp[x][y] = s[:x+1] matches p[:y+1]. careful with base case if p=c*a*b and s=aab, c* matches "".
"""

def solve(s, p):
    # setup dp
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
    dp[-1][-1] = True

    def charMatch(c1, c2):
        if c1 == '.' or c2 == '.':
            return True
        return c1 == c2

    # do dp
    for x in range(-1, len(s)):
        for y in range(len(p)):
            if p[y] == '*':
                if x == -1:
                    dp[x][y] = dp[x][y-2] # skip kleene star
                elif charMatch(p[y-1], s[x]):
                    dp[x][y] = dp[x][y-2] or dp[x-1][y] or dp[x-1][y-2]
                else:
                    dp[x][y] = dp[x][y-2]
            elif x != -1:
                dp[x][y] = charMatch(p[y], s[x]) and dp[x-1][y-1]
            # skip cases where x == -1 and there's a character. won't match, default to false.
    
    return dp[len(s)-1][len(p)-1]


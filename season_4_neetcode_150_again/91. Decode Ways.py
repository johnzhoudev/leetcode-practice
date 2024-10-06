"""

91. Decode Ways

1-26
- misinterpret 2 digit num
- number of ways to decode
or 0 

Idea:
- walk thru, accumulate num ways to decode 
- always check 

ie: 22222
2 - 1 way
2 2 - all previous ways (1) + all previous ways if doubling up

Accumulate all prev and all prev 2 ways
last
lastlast

22 - lastWays + lastlast ways
else just lastWays

- need to check one before too in case character must be wrapped

Idea 2:
- go thru, and for each thing, look ahead. dfs with memoization?
- keep track of last 2 ways
- look ahead once to see if have to wrap

- Coroutine?

Idea 3:
- look behind at last 2 to see num possibilities
- look ahead 1 to see if current character must be used with 0
- check if 0 on consume - kills
- otherwise use prev and prev prev 

dp[i] = num ways to make number from s[0:i] inc

- *** Decode Ways - if 1-9, add dp[i-1]. If 10-26, add dp[i-2]. If nothing added, return 0. TRICKY!

Can you rewrite as coroutine?

"""

def solve(s):
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1
    if s[0] == '0': return 0
    dp[1] = 1

    for i in range(1, len(s)):
        valid = False
        if int(s[i]) > 0: #123456789
            dp[i+1] += dp[i] # just add 1 number
            valid = True

        if 10 <= int(s[i-1:i+1]) and int(s[i-1:i+1]) <= 26:
            dp[i+1] += dp[i-1]
            valid = True

        if not valid:
            return 0
    
    return dp[-1]


def solve(s):
    prevWays = 0
    prevPrevWays = 0

    # Check first element and setup prev and prev prev
    # Manually handle first and second element

    def potentialTwoWays(c1, c2):
        if c1 == '1' and c2 in '0123456789':
            return True
        if c1 == '2' and c2 in '0123456':
            return True
        return False
        
    # Handle first character
    if s[0] == '0': return 0
    prevWays = 1
    prevPrevWays = 1

    idx = 1
    while idx < len(s):
        c = s[idx]
        numWays = 0

        if c == '0': return 0 # invalid

        # Handle look ahead must consume
        if idx + 1 < len(s):
            nextC = s[idx + 1]
            if nextC == '0': # Must consume
                numWays = prevWays
            else: # Don't have to consume
                if potentialTwoWays(s[idx-1], c):
                    numWays = prevWays + prevPrevWays
                else:
                    numWays = prevWays
        else: # No look ahead
            if potentialTwoWays(s[idx-1], c):
                numWays = prevWays + prevPrevWays
            else:
                numWays = prevWays
        
        prevPrevWays = prevWays
        prevWays = numWays
        idx += 1
    
    return prevWays

        
            







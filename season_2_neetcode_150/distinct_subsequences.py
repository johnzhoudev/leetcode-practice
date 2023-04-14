"""

https://leetcode.com/problems/distinct-subsequences/

given s, t, return number of distinct subsequences of s equaling t
- equivalently, how many ways can you delete chars from s to make a string in t
- also have to make sure characters are in the right order, can't just delete same quantity.

opt - check len, check fingerprint

2 categories of letters
- letters not in t
- 

babgbag
bag

- think greedy!

- subproblems, iterate from start of s to get first letter, then finish rest, if possible.
- search alg + memoization
- state[rest of s][rest of t], num ways (inc 0)
- base case, next letter not found. else add one letter at a time
O(n*m) due to memoization

- next cases: either use the char in s, or don't and advance s

Alt: state[i][j] = num ways s[0:i+1] contains t[0:j+1] as subsequences
- either use current s char, or don't.
- s[i][j] = s[i-1][j] (don't use) + s[i-1][j-1] (if you use)
- base case, s[x][-1] = 1 // not using anything from t
- s[-1][t] = 0 // no ways

Tactic: either classicdp s[i][j] = s[i-1][j] (don't use) + s[i-1][j-1] (if you use), careful with base cases.  or search + memo s[rest of s][rest of t] = num ways to have. either use s or don't

"""

def solve(s, t):
    state = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for x in range(len(s)+1):
        state[x][-1] = 1
    
    for tidx in range(len(t)):
        for sidx in range(len(s)):
            if s[sidx] == t[tidx]:
                state[sidx][tidx] = state[sidx - 1][tidx] + state[sidx - 1][tidx - 1]
            else:
                state[sidx][tidx] = state[sidx - 1][tidx]
    
    return state[len(s)-1][len(t)-1]


def solve(s, t):
    if len(t) > len(s):
        return 0
    state = [[-1 for _ in range(len(t))] for _ in range(len(s))]

    def dfs(i, k):

        # base case, finish when t matched completely
        if k == len(t):
            return 1
        if i >= len(s) or k >= len(t): # break if out of range
            return 0 # 0 ways to do this
        
        if state[i][k] != -1:
            return state[i][k]
        
        # now solve
        # skip / don't use
        numWays = dfs(i+1, k)
        if (s[i] == t[k]):
            numWays += dfs(i+1, k+1)
        
        state[i][k] = numWays
        return numWays
    
    return dfs(0, 0)
        
        
        


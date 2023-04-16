"""

https://leetcode.com/problems/edit-distance/

Idea:
- Basically scan string left to right, and each time you have to figure out where to add the correct letters
    - can either do a replace
    - find the next existing
    - or add

- DFS + memoization alg
state[i][j] = min steps to convert s[:i] into t[:j]

Idea2: bottom up dp
- state[i][j] = min steps to solve s[:i+1] into t[:j+1]
- state[i][j] = 
    - to get here, either
    - 1. s[i] == t[j], then use state[i-1][j-1]
    - 2. replace character at si, 1 + state[i-1][j-1]
    - 3. are skipping and dropping characters, 1 + state[i-1][j] 
    - 4. added a character, 1 + state[i][j-1]

- base cases, state[-1][i] = i + 1. just add.
- state[x][-1] = x + 1 # no. needs to have deletions
- state[-1][-1] = 0

Tactic: Either top down dfs + memo, dp[i][j] = min steps to convert s[:i] into t[:j]. Or bottom up dp[i][j] = min steps to solve s[:i+1] into t[:j+1]. Intuit, scan left to right, how to transform. either exact match, or replace, or add / del.

"""

def solve(s, t):
    state = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    # base cases
    for j in range(len(t)):
        state[-1][j] = j + 1
    for i in range(len(s)):
        state[i][-1] = i + 1
    
    # solve
    for j in range(len(t)):
        for i in range(len(s)):
            if (s[i] == t[j]):
                state[i][j] = min(state[i-1][j-1], state[i-1][j] + 1, state[i][j-1] + 1)
            else:
                state[i][j] = min(state[i-1][j-1] + 1, state[i-1][j] + 1, state[i][j-1] + 1)

    return state[len(s)-1][len(t)-1]

def solve(s, t):
    # turn s into t

    state = [[-1 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    def dfs(state, i, j):
        # base cases
        if i == len(s) and j == len(t):
            return 0 # found match, return 0
        elif i == len(s): # finished s before t
            return len(t) - j # have to add rest of t
        elif j == len(t):
            return len(s) - i # delete rest of s
        
        if state[i][j] != -1:
            return state[i][j]
        
        # solve
        cost = float("inf")
        # case 0, best case, it matches
        if (s[i] == t[j]):
            cost = min(cost, dfs(state, i+1, j+1))
        # case 1, just replace next character
        cost = min(cost, dfs(state, i+1, j+1) + 1)
        # case 2, skip until next match, if found. Delete curr char
        cost = min(cost, dfs(state, i+1, j) + 1)
        # case 3, add new char
        cost = min(cost, dfs(state, i, j+1) + 1)

        state[i][j] = cost
        return cost
    
    return dfs(state, 0, 0)







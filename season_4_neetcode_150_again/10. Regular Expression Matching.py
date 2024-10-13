"""

10. Regular Expression Matching

regexp matching of letters, ., *
- * = 0 or more of preceeding element

Ideas:
- Greedy go in order
- * is the only challenge
    - do dfs on star? match 0, or more, increasing at a time if cannot match rest

Are we repeating work?
- could be. ie, a*a*a*bc on aaaaaaaab
    - first try none none x
    - none a x
    - none aa x
    - a aa

On a *, consume 0 to as many as you can and match rest

O(nm)

What's the bottom up dp way?
dp[i][k] = does s[:i] match p[:k]?
- if p[k] is not *, then just match
- if pk is *, then
    - don't use, so check dp[i][k-2]
    - use once, check dp[i-1][k] or dp[i-1][k-2] // use once and more, or just use once 

Tactic:
dfs + memo: compare ordinarily, if star then try 0, 1, 2, or more. cache (i, k) (match s[:i] p[:k])
bottom up df: dp[i][k] = does s[:i] match p[:k]. if not star, compare and check past. if star, 
either use kleene 0 times, 1 time (and past remove kleene) or multiple times

"""

def solve(s, p):
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

    def isStar(k):
        if k + 1 >= len(p): return False
        return p[k+1] == '*'

    def compare(c1, c2):
        if c1 == '.' or c2 == '.': return True
        return c1 == c2

    # base cases
    dp[-1][-1] = True
    # Stars will match nothing as well
    k = 0
    while k < len(p):
        if not isStar(k):
            break
        dp[-1][k+1] = True
        k += 2

    # Now do dp part
    for i in range(len(s)):
        for k in range(len(p)):
            if p[k] != '*':
                dp[i][k] = compare(s[i], p[k]) and dp[i-1][k-1]
            else:
                # special case, handle kleene star
                # do not use, use once, use many times
                if compare(p[k-1], s[i]):
                    dp[i][k] = dp[i][k-2] or dp[i-1][k-2] or dp[i-1][k]
                else:
                    dp[i][k] = dp[i][k-2]
        
    return dp[len(s) - 1][len(p) - 1]





def solve(s, p):
    cache = {}

    def isStar(i):
        if i == len(p) - 1: return False
        else: return p[i + 1] == '*'
    
    def equals(c1, c2):
        if c1 == '.' or c2 == '.': return True
        return c1 == c2

    # Does s[i:] match p[k:]
    def dfs(i, k):
        # end cond
        if i == len(s) and k == len(p): return True
        if k == len(p): return False # one is ended, but other has not - not true if star
        if i == len(s) and not isStar(k): return False # else continue

        # check cache
        if (i, k) in cache: return cache[(i, k)]

        res = False
        # do the actual work
        if not isStar(k):
            res = dfs(i+1, k+1) if equals(s[i], p[k]) else False
        else:
            # consume 0, then 1, then 2, .. until we cannot
            # First consume 0
            res = dfs(i, k + 2)
            if not res:
                consumedIdx = i
                while consumedIdx < len(s) and equals(s[consumedIdx], p[k]):
                    res = dfs(consumedIdx + 1, k + 2)
                    if res: break
                    consumedIdx += 1
            # at this point, res is valid

        cache[(i, k)] = res
        return res
    
    return dfs(0, 0)



"""

1216. Valid Palindrome III


string is k palindrome if can be palindrome by removing at most k characters

remove up to k characters

dynamic programming?
- dp[i][j][k] = is s[i][j] a k palindrome?

dp[i][j][k] = dp[i][j][k-1] or s[i] == s[j] && dp[i+1][j-1][k] or yeah

O(n^2 k)

Brute force, search alg. 
at most k levels deep, each branch 2 ways. so O(n 2^k) or something?

If ends match:
- dp[i][j][k] = dp[i+1][j-2][k]
- if end not in range, then must be the none case. so still True

If ends don't match
dp[i][j][k] = dp[i][j-1][k-1] or dp[i+1][j-1][k-1]


O(n^2 k)?

Other idea: cache, stores k edit distance to make i, j palindromic
- O(n^2) time
- O(n^2) space

dp[i][j] = dp[i+1][j-1] if match
dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j]) if no match

Tactic:
Top down or bottom up dp, dp[i][j] = num of replacements to make palindrome.

"""

def bottomup(s, k):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))] # max moves

    # base cases, 0 steps for all of size 1

    for regionSize in range(2, len(s) + 1):
        for start in range(len(s) - regionSize + 1):
            end = start + regionSize - 1

            # base case, right next to each other
            if start == end - 1:
                dp[start][end] = 0 if s[start] == s[end] else 1
            elif s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1]
            else:
                dp[start][end] = 1 + min(dp[start+1][end], dp[start][end-1])

    return dp[0][len(s) - 1] <= k



def solve(s, k):

    cache = {} # (start, end) => number of edits to make palindromic

    def dfs(start, end):
        # base cases
        if start == end:
            return 0
        
        if start == end - 1:
            return 0 if s[start] == s[end] else 1
        
        # check cache
        if (start, end) in cache: return cache[(start, end)]

        # compute
        if s[start] == s[end]:
            res = dfs(start + 1, end - 1)
        else:
            res = 1 + min(dfs(start + 1, end), dfs(start, end - 1))
        
        cache[(start, end)] = res
        return res
    
    return dfs(0, len(s) - 1) <= k 


def solve(s, k):

    cache = {} # (start, end, k) => ispalindrome or not

    def dfs(start, end, k):
        if (start, end, k) in cache: return cache[(start, end, k)]

        # check base case
        result = False
        if (start == end or start - 1 == end):
            result = True
        elif s[start] == s[end]:
            result = dfs(start + 1, end - 1, k)
        elif k > 0:
            result = dfs(start + 1, end, k-1) or dfs(start, end - 1, k-1)
        else:
            result = False
        
        cache[(start, end, k)] = result
        return result
    
    return dfs(0, len(s) - 1, k)


# TLE as well. Processing too many cases. Memoization best?
def solve(s, k):
    # create state
    dp = [[[False for _ in range(k + 1)] for _ in range(len(s))] for _ in range(len(s))]
    # dp[i][ size 0 to len(s) - 1 ][k]

    # base cases, all anagrams of len 1 are true
    for start in range(len(s)):
        for K in range(k + 1):
            dp[start][0][K] = True

    # also anagrams of len 2
    # for start in range(len(s) - 1):
    #     for K in range(k+1):
    #         if s[start] == s[start + 1]:
    #             dp[start][1][K] = True
    
    # now build up
    for K in range(k + 1):
        for size in range(1, len(s)):
            for start in range(len(s)):
                end = start + size # inclusive

                # too far
                if end >= len(s):
                    break
                
                # case 1, if the ends match. Then don't need to decrease k
                if s[start] == s[end]:

                    # special case, if size is out of bounds
                    if size == 1: # only 2 letters
                        dp[start][size][K] = True
                    else:
                        dp[start][size][K] = dp[start][size][K-1] or dp[start + 1][size - 2][K]
                
                elif K > 0: # ends don't match
                    dp[start][size][K] = dp[start+1][size-1][K-1] or dp[start][size-1][K-1]
                else:
                    dp[start][size][K] = False
    
    return dp[0][len(s) - 1][k]



print(solve("bacabaaa", 2))



# too slow
def solve(s, k):
    if k < 0: return False
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return solve(s[1:len(s) - 1], k)
    else:
        return solve(s[1:], k-1) or solve(s[:len(s) - 1], k-1)



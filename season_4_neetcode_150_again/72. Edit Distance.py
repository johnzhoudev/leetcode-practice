"""

72. Edit Distance

min operations to convert w1 to w2
- insert, delete, or replace a character

brute force idea:
- randomly insert, delete, or replace characters

replacing a character better than delete and insert
    => only delete and insert when no characters or too many characters

- find subsequences of w1 that match up to w2?
    - replace / delete outside of that...

- reuse existing characters as much as possible
    - at a specific character, either you can reuse it 
    - or swap it out and use prev
    - or delete it and use prev

dp[i][k] = steps to convert w1[0:i-1] to w2[0:k-1]

base case:
dp[0][0] = 0 # no steps to convert empty string

dp[i][k] = min (dp[i-1][k-1] if w1[i]==w2[k]
    or swap it out dp[i-1][k-1] + 1 if w1[i] != w2[k]
    or delete it dp[i-1][k] + 1
    or insert it? dp[i][k-1] + 1

Tactic:
bottom up dp or dfs + memo. dp[i][k] = steps to convert w1[0:i] to w2[0:k]. either swap, delete, or insert, or match char (use corresp. dp)

"""

def solve(word1, word2):
    cache = {}

    # get edit distance to change word1[i:] to word2[k:]
    def dfs(i, k):
        # end cases
        if i == len(word1) and k == len(word2): return 0
        if i == len(word1): return len(word2) - k # just add the remaining characters
        if k == len(word2): return len(word1) - i # delete characters from word1

        # check cache
        if (i, k) in cache: return cache[(i, k)]

        # handle
        editDistance = min(
            dfs(i+1, k+1) if word1[i] == word2[k] else dfs(i+1, k+1) + 1, # swap or match case,
            dfs(i+1, k) + 1, # delete character
            dfs(i, k+1) + 1# insert character
        )

        cache[(i, k)] = editDistance
        return editDistance
    
    return dfs(0, 0)








def solve(word1, word2):
    dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    # Base cases
    for k in range(len(word2) + 1):
        dp[0][k] = k # must always add, takes k steps
    
    for i in range(len(word1) + 1):
        dp[i][0] = i # i steps to delete

    # dp step
    for i in range(1, len(word1) + 1):
        for k in range(1, len(word2) + 1):
            dp[i][k] = min(
                dp[i-1][k-1] if word1[i-1] == word2[k-1] else float('inf'),
                dp[i-1][k-1] + 1,
                dp[i-1][k] + 1,
                dp[i][k-1] + 1
            )
    
    return dp[-1][-1]

def solve(word1, word2):
    dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    # Base cases
    for k in range(len(word2) + 1):
        dp[0][k] = k # must always add, takes k steps
    
    for i in range(len(word1) + 1):
        dp[i][0] = i # i steps to delete

    # dp step
    for i in range(1, len(word1) + 1):
        for k in range(1, len(word2) + 1):
            if word1[i-1] == word2[k-1]:
                dp[i][k] = dp[i-1][k-1]
            else:
                dp[i][k] = min(
                    dp[i-1][k-1] + 1,
                    dp[i-1][k] + 1,
                    dp[i][k-1] + 1
                )
    
    return dp[-1][-1]
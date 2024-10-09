"""

dict and string, can you segment into words

dp?

dp[i] = can you segment s[:i] (inc) into words

brute force: ?

s = len(n)
words = k
word len = t
time: O(n k t)

Another idea:
- dp[i] = possible to make with s[:i-1]?
- then dp[i+k] = dp[i] and s[i:k] in words
- Simple!

Tactic: 
dp[i] = can s[:i] (inc) be segmented into words? Then dp[i], check for each word.
OR, dp[i] = is s[:i-1] (inc) segmented into words? Then dp[j] and s[j:i] in word set => dp[i] true.


"""

def solve(s, wordDict):
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    words = set(wordDict)

    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
    
    return dp[-1]

def solve(s, wordDict):
    dp = [False for _ in range(len(s))]

    for endIdx in range(len(s)):
        for word in wordDict:
            beginIdx = endIdx - len(word) + 1
            if dp[endIdx]: continue # Skip if match already found
            if beginIdx < 0 or word != s[beginIdx:endIdx + 1]: continue
            # Word matches
            if beginIdx - 1 >= 0:
                dp[endIdx] = dp[beginIdx - 1]
            else:
                dp[endIdx] = True
    
    return dp[-1]

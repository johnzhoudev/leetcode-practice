"""

139. Word Break

can s be segmented into sequence of 1 or more dictionary words?

dynamic programming? 
- take each segment and see if it's in input?

O(n^2), for each letter, do all substrings?

Tactic: For each letter, take all substrings and check if word is in set and dp.

"""

def solve(s, wordDict):
    words = set()
    for word in wordDict:
        words.add(word)
    
    dp = [False for _ in range(len(s) + 1)] # dp[i] = does s[:i] work?
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if s[j:i] in words and dp[j]:
                dp[i] = True
                break
    return dp[-1]

print(solve("leetcaode", ["leet", "code"]))
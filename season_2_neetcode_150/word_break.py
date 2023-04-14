"""

https://leetcode.com/problems/word-break/

- given word dict
- can you segment word with words in dict?

Ideas:
- search alg, match word prefix and continue? one where you match, one where you continue and maybe match another word
- searches all possibliities. 
- actually think not bad. well, could get bad. dict = "a", "aaaaaab", word = "aaaaaaaaaaaaaaaaaaabaa"

- prefix trie to lookup words?

DP: si = if 0toi can be rep as words
- check if each word fits prefix, and also if prev part all good??
O(n*m) time. for each letter, check m things

Idea: Could also do a bfs / dfs / search alg, with the next available word at each point.

Tactic: Either dp[x] = if word up to x can be split, or dfs/bfs from start using indices. Maintain visited set too for speed.

"""

def solveBFS(s, wordDict):
    state = [0] # idx to keep searching at
    visited = set()

    while state:
        idx = state.pop()
        if idx in visited:
            continue
        visited.add(idx)
        if idx == len(s):
            return True
        for word in wordDict:
            if idx + len(word) - 1 >= len(s):
                continue
            if s[idx:idx+len(word)] == word:
                state.append(idx + len(word))
    return False
    


def solve(s, wordDict):
    state = [False for _ in range(len(s) + 1)] # -1 will wrap around
    state[-1] = True

    for idx in range(len(s)):
        for word in wordDict:
            # if word is valid
            if idx - len(word) >= -1 and state[idx - len(word)] == True and s[idx-len(word)+1:idx+1] == word:
                state[idx] = True
                break
        
    return state[len(s)-1]



"""

139. Word Break

can you segment words in string into dictionary

DP?
Prefix trie

Brute force:
- prefix trie, and search alg - branch every time you find a word
- probably the best runtime

- Make prefix trie class
- do a search alg, 

feel like this is fast? Not gonna be more work than the DP method

Idea:
1. Make prefix trie
2. Have a method in solve that walks thru s.
    - returns True if works, or False

Problem: Edge cases, bunch of repeating values. Checking multiple times

Tactic:
dp[i] = can s[:i+1] be made of words. Then iter thru all, if dp[i-1] and s[i:k+1] matches word, then dp[k]=True.
Checking match can be made faster with Trie.

"""


# Attempt number 2 - cleaner Trie

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = {}


def solve(s, wordDict):
    # first, add all words to trie
    root = TrieNode()

    for word in wordDict:
        curr = root
        for c in word:
            if c not in curr.next:
                curr.next[c] = TrieNode()
            curr = curr.next[c]
        curr.isWord = True
    
    # Now do a search. dp[i] = can s[:i + 1] be split?
    dp = [False for _ in range(len(s))]

    for i in range(len(s)):
        if not (i == 0 or dp[i-1]): # can s[:i] be a thing?
            continue

        # Then try and match more
        curr = root
        for k in range(i, len(s)):
            c = s[k]
            if c not in curr.next:
                break
            curr = curr.next[c]
            if curr.isWord:
                dp[k] = True
    return dp[-1]

print(solve("leetcode", ["leet", "code"]))

                


class TrieNode:
    def __init__(self, c):
        self.c = c
        self.isWord = False
        self.next = {}
    
    # add word, currently at index i (not added yet)
    def addWord(self, word, i):
        if i == len(word):
            # at end, so mark node as isword
            self.isWord = True
            return

        if word[i] not in self.next:
            self.next[word[i]] = TrieNode(word[i])
        
        self.next[word[i]].addWord(word, i + 1)

    def addWord(self, word):
        self.addWord(word, 0)

class NotFound(Exception):
    def __init__(self):
        pass

class Trie:
    def __init__(self, wordDict):
        self.root = TrieNode("root")

        for word in wordDict:
            self.root.addWord(word, 0)
    
    # generator. next(generate) yields next node that is valid, or none
    # def search(self, word):
    #     curr = self.root
    #     for c in word:
    #         # not found
    #         if c not in curr.next:
    #             yield None
    #             raise NotFound
    #         # else traverse
    #         curr = self.next[c]
    #         if curr.isWord:
    #             yield curr

def solve(s, wordDict):

    trie = Trie(wordDict)
    rootNode = trie.root

    cache = {}

    # searches for the next matched word in s, starting at idx
    # returns true or false, if s can be put into words
    def search(s, idx):
        nonlocal rootNode
        nonlocal cache

        if idx in cache:
            return cache[idx]

        if idx >= len(s): return True

        currNode = rootNode

        for i in range(idx, len(s)):
            c = s[i]
            if c not in currNode.next:
                cache[idx] = False
                return False
            currNode = currNode.next[c]
            if currNode.isWord: # is a word, do dfs on next
                if search(s, i + 1):
                    cache[idx] = True
                    return True
                # otherwise continue
        # if get here, then 
        cache[idx] = False
        return False
    
    return search(s, 0)
        
# print(solve("ileetcode", ["i", "leet","code"]))









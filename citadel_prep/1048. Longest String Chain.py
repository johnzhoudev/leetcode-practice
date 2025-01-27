"""

1048. Longest String Chain

Make graph and do dfs? from nodes with no indegrees

- How to make graph?

Maybe level by level
    - comparisons take O(m) time, just do bfs?

Not sure if a trie would help.
And doing level by level is a bit more efficient than a graph

Hold up. Need to also do dfs from other starts that are not. Need to start at all with no indegree
Maybe it is better to just make a graph?

Or actually dp!
- take each word, make sub words and hash, and see if encountered. then update longest chain with that word

O(n log n) to sort words
O(n ss) each word, make substring and check if in set and hash

Tactic:
DP. Sort words and make prev possibilities with concat. And check in set!

"""
from collections import defaultdict

def solve(words):
    words.sort(key = lambda x: len(x))
    wordChains = defaultdict(lambda : 0)

    for word in words:
        best = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in wordChains:
                best = max(best, wordChains[prev] + 1)
        wordChains[word] = best
    
    return max(wordChains.values())
        

# Works
# word = "abcdef"
# for i in range(len(word)):
#     prev = word[:i] + word[i+1:]

from collections import defaultdict

def solve(words):

    lengths = defaultdict(list)
    minlen = float('inf')
    for word in words:
        minlen = min(minlen, len(word))
        lengths[len(word)].append(word)
    
    def canChain(w1, w2):
        if len(w1) > len(w2): return canChain(w2, w1)
        if len(w1) + 1 != len(w2): return False

        skip = 0
        for i in range(len(w1)):
            if w1[i] == w2[i + skip]: continue
            if skip == 0: skip = 1
            else: return False
        return True

    # Now go thru
    l = minlen - 1
    length = 0
    curr = lengths[minlen]
    while curr:
        l += 1
        length += 1
        print("hi", curr, l)
        nextLvl = lengths[l + 1]
        newCurr = []
        for w1 in curr:
            for w2 in nextLvl:
                if canChain(w1, w2): newCurr.append(w2)
        curr = newCurr
    print(lengths)
    return length

print(solve(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))


    

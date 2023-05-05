"""

https://leetcode.com/problems/word-ladder/

- have dict of words
- step words one by one, each differs by single letter
- go from beginword to end word, beginword not in dictionary
- return min num transformations

Ideas:
- brute force, search alg to check every single possibility
- DP with memoization, state is at x, what is shortest way to get to y?
    - O(x, y), so O(n^2) states
- have to use seen array. can't do loops. DFS.

- maybe build graph in the beginning? check if a word differs in one position
    - O(max len * n) to check all chars
So O(max len * n) to check all chars and make a graph, then O(n^2) dp with memoization

- DP ground up? 
    - dp[x][y] = shortest path from x to y
    - start with same len, [x][x] = 0
    - then as len increases, pick middle and go 
    - O(n^2) * O(n) per each, since have to evaluate where in the path you depart

- Use djikstra's alg, get shortest path from one place to all places
- O(n) time? for graph?

Idea Final:
- make graph, check adjacency of each word
    - n num words, m max len per word
    - O(n^2 * m) to compare and check all pairs of words
- Make list of reachable, then do dijkstra's
    - to get min, just search manually
    - Every next thing, will take too much effort to reorganize if we have new adjacencies. so O(nm) anyway.
    So O(n^2 m) in total

- Not dijkstra's, but BFS basically since all edge weights are 1
    - O(n)

tip: Better to check adjacency by checking all possible departures from a word, and checking if it's in a set
    - basically less possibilities, rather than checking all pairs.
    - Or better yet, don't build the graph and just expand each step using the letter trick

tip2 (neetcode): use wildcard and default dict, but then have to store words during search

Tactic: BFS (dijkstra's in disguise). Tip, don't compare pairs of words to make adj list, but generate possible words (each differ by 1 letter) and check in set. OR, neetcode, use wildcard in word and create default dict (words with same wildcard, will be adj.)


"""
from collections import defaultdict

def solve(begin, end, words):
    if end not in words:
        return 0
    words.append(begin)
    adj = defaultdict(list)

    for word in words:
        for i in range(len(word)):
            nw = word[:i] + "*" + word[i+1:]
            adj[nw].append(word)
    
    # now do bfs
    state = [begin]
    visited = set()
    visited.add(begin)
    level = 1
    while state:
        dummy = []
        for word in state:
            if word == end:
                return level
            # add children
            for i in range(len(word)):
                nw = word[:i] + "*" + word[i+1:]
                for next in adj[nw]:
                    if next not in visited:
                        dummy.append(next)
                        visited.add(next)
        state = dummy
        level += 1
    return 0




def solve(begin, end, words):
    if end not in words:
        return 0

    words.append(begin)
    wordSet = set(words)

    state = [begin]
    visited = set()
    visited.add(begin)
    level = 0
    while state:
        dummy = []
        for word in state:
            if word == end:
                return level
            # else add children
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        dummy.append(newWord)
                        visited.add(newWord)
        state = dummy
        level += 1
    return 0


def solve(begin, end, words):

    if end not in words:
        return 0
    endIdx = words.index(end)

    # add word begin
    # otherwise get idx
    if begin not in words:
        words.append(begin)
        beginIdx = len(words) - 1
    else:
        beginIdx = words.index(begin)
    
    # 0 for match, 1 for only 1, -1 for more
    def diff(s1, s2):
        diffCount = 0
        for i, c in enumerate(s1):
            if c != s2[i]:
                diffCount += 1
            if diffCount > 1: return -1
        return diffCount
    
    # Building Graph V2
    adj = [[] for _ in range(len(words))]
    wordToIdx = {}
    for idx, word in enumerate(words):
        wordToIdx[word] = idx
    
    for idx, word in enumerate(words):
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordToIdx:
                    adj[idx].append(wordToIdx[newWord])

    # first, build graph
    # adj = [[False for _ in range(len(words))] for _ in range(len(words))]
    # also just enumerate using word idx instead of word for easy comparison
    # adj = [[] for _ in range(len(words))]
    # for idx1 in range(len(words)):
    #     for idx2 in range(idx1 + 1, len(words)):
    #         dif = diff(words[idx1], words[idx2])
    #         if dif == 0 or dif == 1:
    #             adj[idx1].append(idx2)
    #             adj[idx2].append(idx1)

    # Do bfs
    state = [beginIdx]
    visited = set()
    visited.add(beginIdx)
    steps = 1
    while state:
        dummyState = []

        for idx in state:
            if idx == endIdx:
                return steps
            # if not match, append children
            for childIdx in adj[idx]:
                if childIdx not in visited:
                    dummyState.append(childIdx)
                    visited.add(childIdx)
        state = dummyState
        steps += 1
    
    return 0
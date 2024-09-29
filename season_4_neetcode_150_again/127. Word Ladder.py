"""

Word ladder

- dictionary wordList
- beginword s1 s2 sk
- differ single letter

- return number of words in shortest transformation sequence, or 0 if DNE
- all words of same length

Idea:
- build a graph? 
- or don't build a graph, but start at beginword and just check each time?
- nah, better to build a graph otherwise repeating checks

Time: O(n) where n is number of words to do dfs + O(n^2) to make the adj list

Wildcard strat
Time: O(n) to make adj list!
Traversal, O(n) too? every word gets added once max

Tactic: Wildcard characters!!!
"""


def solve(beginWord, endWord, wordList):
    # make the wildcard adj lists
    adjList = defaultdict(list)

    # O(n)
    for word in wordList:
        for i in range(len(word)):
            wordKey = word[:i] + "*" + word[i+1:]
            adjList[wordKey] += [word]
    
    # now process
    curr = [beginWord]
    visited = set()
    level = 1
    while curr:
        next = []
        for word in curr:
            if word in visited: continue
            if word == endWord: return level

            visited.add(word)

            for i in range(len(word)):
                wordKey = word[:i] + "*" + word[i+1:]
                next += adjList[wordKey]
        curr = next
        level += 1
    
    return 0


from collections import defaultdict
def solve(beginWord, endWord, wordList):

    def compareWord(w1, w2):
        assert(len(w1) == len(w2))

        diffCount = 0
        for idx, c in enumerate(w1):
            if c != w2[idx]:
                diffCount += 1
            if diffCount > 1: return False
        return True

    # first make a graph
    adjList = defaultdict(list)

    for idx, word in enumerate(wordList):
        for word2 in wordList[idx+1:]:
            if compareWord(word, word2):
                adjList[word] += [word2]
                adjList[word2] += [word]
    
    # add from beginword
    for word in wordList:
        if compareWord(beginWord, word):
            adjList[beginWord] += [word]
    
    # Now do bfs
    state = [beginWord]
    visited = set()
    numIter = 1

    while state:
        next = []
        for word in state:
            if word in visited: continue
            if word == endWord: return numIter

            visited.add(word)
            for nextWord in adjList[word]:
                next.append(nextWord)
        
        numIter += 1
        state = next
    
    return 0






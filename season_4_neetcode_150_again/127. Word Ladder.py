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
"""

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
    
    # Now do dfs
    state = [beginWord]




# Results:
# Runtime: 1306ms 67.14%
# Memory Usage: 18.8MB 13.29%

"""

https://leetcode.com/problems/word-search-ii/

Idea: use prefix tree on words, and then must check every combo if is a word
    - can look up in a chain, 
- O(x * w) time to build prefix tree
- with n x m grid
- O(n * m^2)

n^2 * m
+ m^2 * n
O(n^2 m + m^2 n) * O(search)

- need to run a new search on each start, but we can save time on building strings

xx - Need to use a search algorithm to build all possible "paths" thru the thing
- then we can run our searching algs once we have a whole path
- how to avoid duplication

Maybe most straightforward is run the basic search with fixed start, and generate full paths
    - from each point

Or, use the trie to generate paths
    - start search at each letter, and use trie to check directions and see if a move is valid
    - some backtracking alg, storing visited and state and stuff
    - oh dang

Final idea:
- Build prefix trie for all words, to check existence
- Do a dfs from each starting location, and check if still in trie path, else off. 
- need to prune tree for fast

Tactic: Build Prefix Tree for words, do recursive search alg from all starts. Careful with visited, must pop when return. Prune tree after word found. tip, mark isWord = False when word found to avoid dupe
"""

class TrieNode:
    def __init__(self):
        self.letterTable = {}
        self.isWord = False
    
    def insert(self, word):
        currNode = self
        for c in word:
            if c not in currNode.letterTable:
                currNode.letterTable[c] = TrieNode()
            currNode = currNode.letterTable[c]
        currNode.isWord = True
    
    def pruneWord(self, word, idx = -1): # idx is of current node
        if idx <= len(word) - 3: # will add -2, but not -1
            self.letterTable[word[idx + 1]].pruneWord(word, idx + 1)
        
        child = self.letterTable[word[idx + 1]]
        if len(child.letterTable) == 0 and child.isWord == False:
            del self.letterTable[word[idx + 1]]

def buildPrefixTree(words):
    trie = TrieNode()
    for word in words:
        trie.insert(word)
    return trie

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solve(board, words):
    prefixTrie = buildPrefixTree(words)
    output = []

    def dfs(board, visited, node, row, col, word):
        nonlocal output
        if (row, col) in visited:
            return
        visited.add((row, col))

        if node.isWord:
            node.isWord = False
            output.append(word)
            prefixTrie.pruneWord(word)
        
        # Now dfs to next stuff
        for deltaRow, deltaCol in directions:
            newRow = deltaRow + row
            newCol = deltaCol + col
            if newRow < 0 or newRow >= len(board) or newCol < 0 or newCol >= len(board[0]):
                continue
            if board[newRow][newCol] in node.letterTable:
                dfs(board, visited, node.letterTable[board[newRow][newCol]], newRow, newCol, word + board[newRow][newCol])

        visited.remove((row, col))

    # now do dfs of all words, mark words as not word if found, and see
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] not in prefixTrie.letterTable:
                continue
            # Do a search alg for all paths
            visited = set()
            dfs(board, visited, prefixTrie.letterTable[board[row][col]], row, col, board[row][col])
    return output
                

def solveNotWorking(board, words):
    prefixTrie = buildPrefixTree(words)

    # now generate all combos of words, and reverse
    results = set()

    # for each row word
    for row in board:
        s = "".join(row)
        results.update(prefixTrie.findWordsCombo(s))
    
    for col in range(len(board[0])):
        s = ""
        for row in range(len(board)):
            s += board[row][col]
        results.update(prefixTrie.findWordsCombo(s))
    
    return list(results)

    





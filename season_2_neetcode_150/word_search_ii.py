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
"""

class TrieNode:
    def __init__(self):
        self.letterTable = {}
        self.isWord = False
        self.word = ""
    
    def insert(self, word):
        currNode = self
        for c in word:
            if c not in currNode.letterTable:
                currNode.letterTable[c] = TrieNode()
            currNode = currNode.letterTable[c]
        currNode.isWord = True
        currNode.word = word

    # def doesExist(self, word):
    #     currNode = self
    #     for c in word:
    #         if c not in currNode.letterTable:
    #             return False
    #         currNode = currNode.letterTable[c]
    #     return True

    def findWordsInWord(self, word):
        result = []
        currWord = ""
        currNode = self
        for c in word:
            if c not in currNode.letterTable:
                break
            currNode = currNode.letterTable[c]
            currWord += c
            if currNode.isWord:
                result += [currWord]
        return result

    def findWordsInWord(self, word, startIdx):
        result = []
        currWord = ""
        currNode = self
        idx = startIdx
        while idx < len(word):
            c = word[idx]
            if c not in currNode.letterTable:
                break
            currNode = currNode.letterTable[c]
            currWord += c
            if currNode.isWord:
                result += [currWord]
            idx += 1
        return result
    
    def findWordsCombo(self, word):
        result = []
        for startIdx in range(len(word)):
            result += self.findWordsInWord(word, startIdx)
        
        return result


def buildPrefixTree(words):
    trie = TrieNode()
    for word in words:
        trie.insert(word)
    return trie


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solve(board, words):
    prefixTrie = buildPrefixTree(words)
    output = []

    # now do dfs of all words, mark words as not word if found, and see
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] not in prefixTrie.letterTable:
                continue
            # Do a dfs / search alg for all paths
            visited = set()
            state = [prefixTrie.letterTable[board[row][col]]]
            visited.add(state[0])
            while state:
                node = state.pop()
                visited.add(node)
                if node.isWord:
                    node.isWord = False # prevent from being checked again
                    output.append(node.word)
                
                # advance
                for deltaRow, deltaCol in directions:
                    newRow = deltaRow + row
                    newCol = deltaCol + col
                    if newRow < 0 or newRow > len(board) or newCol < 0 or newCol > len(board[0]):
                        continue

                for next in node.letterTable.values():
                    if next not in visited:
                        state.append(next)
                





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

    





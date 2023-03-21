# Results:
# Runtime: 8462ms 79.70%
# Memory Usage: 78.1MB 35.54%

""""

https://leetcode.com/problems/design-add-and-search-words-data-structure/

- add words
- in search, dots can be matched with any letter

- use prefix trie, but on dot, search all letters?
- at most 3 dots in thing

- simplest, recursive search?
    - or do for loop. for each elt, do search - returns True / False

Tactic: trie, searchFromNode func that is called on each key if hit '.'

O(w) insert, O(w * num dots * maxSpread) search

"""

class TrieNode:
    def __init__(self):
        self.letterTable = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for c in word:
            if c not in currNode.letterTable:
                currNode.letterTable[c] = TrieNode()
            currNode = currNode.letterTable[c]
        currNode.isWord = True


    def search(self, word: str) -> bool:

        # returns true or false
        def searchFromNode(currNode, idx):
            
            while idx < len(word):

                if word[idx] == '.':
                    for nextc in currNode.letterTable:
                        if searchFromNode(currNode.letterTable[nextc], idx + 1):
                            return True
                    return False
                
                if word[idx] not in currNode.letterTable:
                    return False

                currNode = currNode.letterTable[word[idx]]
                idx += 1
            
            return currNode.isWord

        return searchFromNode(self.root, 0)

                


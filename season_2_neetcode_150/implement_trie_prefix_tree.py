# Results:
# Runtime: 173ms 63.56%
# Memory Usage: 31.6MB 48.9%

"""

https://leetcode.com/problems/implement-trie-prefix-tree/

- implement

Store root, with hash table of letter to next node

- insert follow along until not exist, then insert
- search, go until not exist or found
- startsWith, search

Better: insert, combine loops with clause, if not in, add dict entry
- for c in word works faster than idx while loop.

Tactic: hash tables to next letter. to insert, combine loops with clause, if not in, create new node.


"""

class TrieNode:
    def __init__(self, val, isWord = False):
        self.val = val
        self.isWord = isWord
        self.letterTable = {}

class Trie:

    def __init__(self):
        self.root = TrieNode('0')

    def insert(self, word: str) -> None:
        idx = 0
        currNode = self.root
        # First loop to insert word
        while idx < len(word):
            if word[idx] not in currNode.letterTable:
                currNode.letterTable[word[idx]] = TrieNode(word[idx])
            currNode = currNode.letterTable[word[idx]]
            idx += 1
        
        currNode.isWord = True
        
    def findNode(self, word: str) -> bool:
        currNode = self.root
        idx = 0
        while idx < len(word):
            if word[idx] in currNode.letterTable:
                currNode = currNode.letterTable[word[idx]]
                idx += 1
            else:
                return None
        return currNode

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node.isWord if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.findNode(prefix)
        return True if node else False

class Trie:

    def __init__(self):
        self.root = TrieNode('0')

    def insert(self, word: str) -> None:
        currNode = self.root
        # First loop to insert word
        for c in word:
            if c not in currNode.letterTable:
                currNode.letterTable[c] = TrieNode(c)
            currNode = currNode.letterTable[c]
        currNode.isWord = True
        
    def findNode(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            if c in currNode.letterTable:
                currNode = currNode.letterTable[c]
            else:
                return None
        return currNode

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node.isWord if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.findNode(prefix)
        return True if node else False

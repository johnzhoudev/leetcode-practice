"""

- given bag of roots
- replace all words in sentence with shortest root  

Ideas:
- make trie of all roots
- do word lookup for root and replace in string

O(n) where n is number of letters

Tactic: Use a Trie!

"""

class TrieNode:
  def __init__(self):
    self.isWord = False
    self.next = {}
  
  def makeWord(self):
    self.isWord = True
  
class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def addWord(self, word):
    currNode = self.root
    for c in word:
      if c in currNode.next:
        currNode = currNode.next[c]
      else:
        currNode.next[c] = TrieNode() # Make new node
        currNode = currNode.next[c]
    currNode.makeWord()
  
  def lookupPrefix(self, word):
    currNode = self.root
    prefix = ""
    for c in word:
      if c not in currNode.next: return word # Returns correct word as shortcut
      currNode = currNode.next[c]
      prefix += c
      if currNode.isWord: return prefix
    return word
    

def solve(roots, sentence):
  # Make trie
  words = Trie()
  for word in roots:
    words.addWord(word)
  
  output = ""
  for word in sentence.split(" "):
    output += words.lookupPrefix(word) + " "
  
  output = output.strip()
  return output

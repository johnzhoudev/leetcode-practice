"""
https://leetcode.com/problems/word-ladder/

begin-s1-s2-...-sk
adjacent words differ by single letter
each si is in wordList
begin does not need to be in wordlist
sk == endword
all words have same length

Return shortest transform sequence, or 0 if none exists

Ideas:
- Brute Force: Do a search alg, at each word, the next state is a word that has 1 letter different.
- search all possiblities, but break if len is over already or a loop
- watch for loops!

- How to find next states? Preprocessing?
- make an nxn array, or hash map to linked lists of what words will work...
- keep hash table of words already used, and undo?

Time: O(ns) to check for single letter diffs
- checking word diffs - put letter counts into hash table, and check equality between.
	- only need to check one side. If one letter differs, will see in both. either new letter, or letter with more.
	- O(ns) to make hashes, and O(ns) to check each word against other words = O(n^2 s)
- For actual search part, maintain stack of seen.
O()
"""
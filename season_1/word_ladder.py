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
	- O(ns) to make hashes, and O(n) to check each word against other words given hashes = O(n^2)
	- O(s) time to compare 2 individual words
- For actual search part, maintain stack / set of seen and do a search algorithm
- check if word goes to any of the words not already seen, and push that word onto the stack. and continue.
- each path max O(n) items, n! number of paths potentially.

Can we do better? can we do it without the adjacency table? how else to tell if valid move? no. 
Can we do better than a search algorithm for the search part? No, have to find shortest path. 
- maybe do BFS and return first find! so only go so deep, less redundancy.
- but still O(n!) worst case

Hold up - every adjacent word differs by single letter in SAME position - 
- GOC and COG differ in 2 places...
- so to establish equality, need to check both letter by letter - O(s) to check equality between 2
- O(n^2 s) for all
"""

def ladderlen1(beginWord, endWord, wordList):

	def isFingerprintEqual(f1, f2):
		if len(f1) != len(f2):
			return False
		
		# check all of f1. if you find there's 1 less or non-exist in f2, return false.
		for c in f1.keys():
			if c not in f2 or f1[c] != f2[c]:
				return False
		
		return True
	
	def isFingerprint1Away(f1, f2):
		if len(f1) != len(f2):
			return False
		
		# check all of f1. if you find there's 1 less or non-exist in f2, that's the most you can find.
		# difference - c is not in f2, and f1[c] has 1. OR, c is in f2, and f1 - f2 = 1
		# not worried about if f2 has the extra c, since if it does, since len is same, we will find ours is missing one somewhere.
		diffOne = False
		for c in f1.keys():
			if c in f2 and f1[c] == f2[c]: # matches
				continue
			elif (c not in f2 and f1[c] == 1) or (c in f2 and f1[c] - f2[c] == 1): # if c is less by 1 in f2
				# one missing
				if (diffOne): return False
				else: diffOne = True
			else:
				return False

		return diffOne

	def wordToFingerprint(word):
		fingerprint = {}
		for c in word:
			if c in fingerprint:
				fingerprint[c] += 1
			else:
				fingerprint[c] = 1
		return fingerprint

	# Setup state and get word fingerprints
	wordFingerprints = list(map(wordToFingerprint, wordList))

	# create adjacency hashtable to lists - hash the index of the word!
	adjTable = [[] for _ in range(len(wordList))]
	for index in range(len(wordList)):
		for index2 in range(len(wordList)):
			if (index == index2): continue
			elif (isFingerprint1Away(wordFingerprints[index], wordFingerprints[index2])):
				adjTable[index] += [index2]
			
	# now, adjacency table should be all good. can solve.
	print(adjTable)

ladderlen1("ab", "bc", ["ab", "ac", "dc", "de", "bc"])




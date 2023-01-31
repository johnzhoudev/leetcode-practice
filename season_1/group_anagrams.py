# Results:
# Runtime: 94ms 98.96%
# Memory Usage: 17.7MB 67.02%

"""
Array of strings strs
Group anagrams together - rearrangement of letters


Ideas:
- need to at least parse each letter of each word, and figure out which ones have same letters
- Can we do a set intersection?

Brute force:
- compare each word with every other word O(n^2) * comparison (can use hash table)

Better: 
- sort each word first -> O(n log n)
- use a dictionary to map hashes that are the same -> do a lookup for each word O(n) total, 
So O(n) total

Better? Can we do in O(n)?
- how to figure out which groups each one is in?
- how would you insert "eat" and "tea" into the same set?
- What's the best way to check two words are anagrams? Put letters and freq into hash table, then compare keys and vals.
	- O(n) to build fingerprints
- use these fingerprints as keys? O(n) lookup
	- can convert fingerprints to keys -> a2c3, or something in alphabetical order?
	- Not convinced that you can use dictionaries as keys in a hash table efficiently. Would need to have a way of ordering
		so you can go char by char, or equality checks / comparisons could take time too.
	- actually you can use dicts as keys, just need to be immutable. frozen set. can hash anything!

Tactic: Use sorted string as key, and hash.

"""

def groupAnagrams(strs):
	# 1. generate keys
	stringKeysAndValues = map(lambda string : (''.join(sorted(string)), string), strs)

	# 2. for each string, insert its thing into a dictionary, or if it exists already, append
	dictionary = {}

	for (key, string) in stringKeysAndValues:
		if (key in dictionary): dictionary[key].append(string)
		else: dictionary[key] = [string]
	
	return dictionary.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
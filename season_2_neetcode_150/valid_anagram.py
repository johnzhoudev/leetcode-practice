# Results:
# Runtime: 50ms 93.93%
# Memory Usage: 14.4MB 67.72%

"""
s, t, return true if t is an anagram of s, false otherwise

Ideas:
- O(n) time, create a hash table hashing character to num occurrences
- parse both, check if the same
	- dictionary equality checking
	- check len is same
	- for each item in one, check if matches other

Better: use one dictionary, and subtract values from t. if all 0 at end, all good.
- saves space

O(n) space

Tactic: Use 1 dict since if count is same, add / sub to 0. Also use early breaks for speed, ie check len first
"""

def generateFingerprint(str):
	fingerprint = dict()
	for c in str:
		if c in fingerprint:
			fingerprint[c] += 1
		else:
			fingerprint[c] = 1
	return fingerprint

def solve2(s, t):
	if (len(s) != len(t)):
		return False
	
	fingerprint = dict()
	for c in str:
		if c in fingerprint:
			fingerprint[c] += 1
		else:
			fingerprint[c] = 1

	for c in t:
		if c not in fingerprint:
			return False
		
		fingerprint[c] -= 1
		if (fingerprint[c] < 0):
			return False
	
	for count in fingerprint.values():
		if count != 0:
			return False

	return True

	

def solve(s, t):
	if (len(s) != len(t)):
		return False
	
	sFingerprint = generateFingerprint(s)
	tFingerprint = generateFingerprint(t)

	return sFingerprint == tFingerprint
	



"""

https://leetcode.com/problems/group-anagrams/


Idea:
- fingerprint for each anagram, as dict
- use a set of the fingerprints, find if same one
- add to list

- each fingerprint takes O(1) time to generate since fixed length
- equality check O(1), since fixed number of alphabet letters
- Runtime: O(n) - gen fingerprints, then check which are equal and group

Tactic: Either use sorted string as key, or frozen set fingerprint. can technically sort in O(n) n len of string.

"""

def groupAnagrams(strs):
    # create array of fingerprints

    fingerprints = []

    def toFingerprint(s):
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return d

    for s in strs:
        # store tuples
        fingerprints += [(frozenset(toFingerprint(s).items()), s)] # use fingerprints as keys, therefore must be immutable. freeze

    # for each fingerprint, add / check equality in set and group together
    fingerprintGroups = {}
    for f, s in fingerprints:
        if f in fingerprintGroups:
            fingerprintGroups[f] += [s]
        else:
            fingerprintGroups[f] = [s]
    
    result = []
    for val in fingerprintGroups.values():
        result += [val]

    return result

    




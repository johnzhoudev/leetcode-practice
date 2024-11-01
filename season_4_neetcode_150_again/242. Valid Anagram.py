"""

242. Valid Anagram

true if t is anangram of s

- just count letters. use dict

"""

from collections import defaultdict
def solve(s, t):
    sletters = defaultdict(lambda : 0)
    for x in s: sletters[x] += 1
    tletters = defaultdict(lambda : 0)
    for x in t: tletters[x] += 1

    if len(sletters) != len(tletters): return False
    
    for x in sletters:
        if sletters[x] != tletters[x]: return False
    
    return True
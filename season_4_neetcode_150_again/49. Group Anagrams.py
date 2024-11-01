"""

49. Group Anagrams

strs
group anagrams

Idea:
- parse all and turn to dictionaries of letter counts
- transform to strings, 
- or sort all strings and use as key to group?

O(nm log m) # sort
+ O(nm checking in hash set)

Tactic:
sort word and use sorted word as key in hashtable

"""

def solve(strs):

    groups = {}
    
    for s in strs:
        sorteds = ''.join(sorted(s))
        if sorteds in groups:
            groups[sorteds].append(s)
        else:
            groups[sorteds] = [s]
    
    return [groups[g] for g in groups]

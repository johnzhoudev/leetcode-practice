"""

49. Group Anagrams

make fingerprint with dict
dict compare equality
group!


O(n) time to generate fingerprint (count letters, sort O(26), join)

"""

from collections import defaultdict

def solve(strs):

    def gen_fingerprint(s):
        counts = defaultdict(lambda: 0)
        for c in s:
            counts[c] += 1
        val = ''.join([f"{x[0]}{x[1]}" for x in sorted(counts.items(), key=lambda x: x[0])])
        return val
    
    groups = defaultdict(list)

    for s in strs:
        fp = gen_fingerprint(s)
        groups[fp].append(s)
    
    return list(groups.values())


    

    
    
            


"""

916. Word Subsets


Idea:
- create master subset - max count of each letter
    - letters are individaul
- then for words, make fingerprint and check

O(m * n) time
O(n space)

"""

from collections import defaultdict

def solve(words1, words2):

    def get_fingerprint(word):
        fingerprint = defaultdict(lambda : 0)
        for c in word:
            fingerprint[c] += 1
        return fingerprint

    master_fingerprint = defaultdict(lambda : 0)
    for word in words2:
        fingerprint = get_fingerprint(word)
        for c, count in fingerprint.items():
            master_fingerprint[c] = max(master_fingerprint[c], count)
    
    # now check words
    output = []
    for word in words1:

        fingerprint = get_fingerprint(word)
        no_match = False

        for c, count in master_fingerprint.items():
            if count > fingerprint[c]:
                no_match = True
                break
        
        if no_match: continue
        else: output.append(word)
    
    return output


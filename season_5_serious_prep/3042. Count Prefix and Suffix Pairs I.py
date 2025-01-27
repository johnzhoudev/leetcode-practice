"""

3042. Count Prefix and Suffix Pairs I


- number of pairs that are prefix suffixes of each otehr, i < j 

Idea:
isPrefixSuffix - O(str 1)

for pairs -> just do for each

"""

def solve(words):

    def isPrefixSuffix(w1, w2):
        if len(w2) < len(w1): return False
        # is prefix?
        for i in range(len(w1)):
            if w1[i] != w2[i]: return False
        # is suffix?
        for i in range(len(w1)):
            if w1[len(w1) - i - 1] != w2[len(w2) - i - 1]: return False
        return True
    
    count = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if isPrefixSuffix(words[i], words[j]):
                count += 1

    return count

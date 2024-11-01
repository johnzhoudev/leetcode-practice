"""

763. Partition Labels

partition s so each letter appears in at most 1 part
- concat all so resulting string must be s
- want as many parts posssible

- return list of ints representing size of parts

Ideas:
- partition all into single characters, and join them together until chars not in 2 parts
- union find problem?

Brute force way:
- for each character, extend the window until the last character

First pass, map char to last index in string 
- keep expanding a rolling window s.t. all characters in window are contained
O(n) time!

Tactic:
Greedy, map char to last idx in string and keep expanding rolling window.

"""

def solve(s):
    # get last index of each character
    lastIdx = {}
    for idx, c in enumerate(s):
        lastIdx[c] = idx
    
    # Now go thru and keep sizes 
    size = 0
    currIdx = 0
    endIdx = 0

    output = []

    # assumes currIdx not added yet
    while currIdx < len(s):
        endIdx = max(endIdx, lastIdx[s[currIdx]]) # update endIdx
        size += 1

        # hit end of section
        if currIdx == endIdx:
            output.append(size)
            size = 0

        # otherwise, continue 
        currIdx += 1
    
    return output



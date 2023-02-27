# Results:
# Runtime: 154ms 56.86%
# Memory Usage: 14.7MB 76.14%

"""

https://leetcode.com/problems/minimum-window-substring/description/

s, t
- min window substr of s s.t. all chars of t included in s

Idea:
- problem is you can have random chars inside now

Naive: O(n^2) test all substrings

- Extend window until all chars are inside
- then shrink until one char is not - then keep growing
Correctness: guaranteed to get all chars, then shrinking will get min.
O(n) time, O(t) space? 

Tactic: Sliding window, expand until have all chars, then try shrinking. use numContained to easily check equality - num chars with correct quantity or MORE
"""

def solve(s, t):
    # create t fingerprint
    tMap = {}

    for c in t:
        if c in tMap:
            tMap[c] += 1
        else:
            tMap[c] = 1
    
    # sliding window
    left = 0
    right = 0 # exclusive

    numMatches = 0 # for checking if characters match, or exceed
    sMap = {}

    bestLeft = 0
    bestRight = len(s) + 1

    while right <= len(s):

        # if not all characters contained, keep growing window
        if numMatches != len(tMap): # not all keys match
            if (right == len(s)): break
            c = s[right]
            # If adding a char that's valid
            if c in tMap:

                if c in sMap:
                    sMap[c] += 1
                else:
                    sMap[c] = 1

                if sMap[c] == tMap[c]: # become equal after adding
                    numMatches += 1

            # else, do nothing
            right += 1
        else: # all keys match

            if (right - left < bestRight - bestLeft):
                bestLeft = left
                bestRight = right

            # try shrinking
            c = s[left]
            if c in tMap: # then must be matching
                sMap[c] -= 1
                if (sMap[c] < tMap[c]):
                    numMatches -= 1
            # else dropped a useless char
            left += 1
    
    if (bestRight - bestLeft == len(s) + 1): return "" # none found
    return s[bestLeft:bestRight]





            

            





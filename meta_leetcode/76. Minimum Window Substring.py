"""

76. Minimum Window Substring

s and t
len m and n
- return min window substring of s s.t. each char of t is included, including duplicates

- or "" if none

Brute force: check all substrings, O(n^2 m)

Sliding window? Keep counts of each letter in t
- left, keep shrinking until shrink would decrement a key value
- each time you expand the window, if the left side equals the new expanded and is extra, can decrement

- numchars added / removed counter to verify

O(n) time
O(n) space for map of char counts

Tactic:
Store counts for characters in hashmap. Expand window, and after expanding, shrink if possible.

"""

def solve(s, t):
    # make map count of t's chars
    tmap = {}
    for c in t:
        if c in tmap:
            tmap[c] += 1
        else:
            tmap[c] = 1
    
    # now sliding window thru s
    count = 0
    left = 0
    right = 0 # exclusive

    bestLeft = -1
    bestRight = float('inf')

    while right < len(s):

        # add right
        c = s[right]

        # if it's a character
        if c in tmap:
            # necessary character
            if tmap[c] > 0:
                count += 1

            tmap[c] -= 1

        right += 1
        # added right
        
        # now shrink left as much as possible
        while left < right:
            # irrelevant character, shrink
            if s[left] not in tmap:
                left += 1
            elif tmap[s[left]] < 0:
                # remove extraneous characters
                tmap[s[left]] += 1
                left += 1
            else:   # tmap >= 0
                break # cannot remove left

        if count == len(t):
            if (bestRight - bestLeft + 1 > right - left + 1):
                bestLeft = left
                bestRight = right

    if bestLeft == -1:
        return ""
    return s[bestLeft:bestRight]


print(solve("ab", "a"))

        
            


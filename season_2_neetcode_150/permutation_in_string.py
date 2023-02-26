# Results:
# Runtime: 63ms 88.58%
# Memory Usage: 14MB 23.69%

"""

https://leetcode.com/problems/permutation-in-string/

Idea:
- make hash map of s1
- sliding window, add characters if in s1. if over, start dropping
    - if you've added x characters, and last char is equal, must be true.
    - if you get over, drop chars until safe again

Tactic: sliding window var. sized only add if in s1. if len == s1, True.
"""

def solve(s1, s2):
    # state
    s1Count = {}
    s2Count = {}

    # Build s1count
    for c in s1:
        if c in s1Count:
            s1Count[c] += 1
        else:
            s1Count[c] = 1
    
    # sliding window on s2
    left = 0
    right = 0 # exclusive

    while left <= right and right <= len(s2):
        # if we manage to add all chars, must be true
        if right - left == len(s1):
            return True
        
        if right == len(s2): break
        c = s2[right]
        
        # Try adding a character 
        if c not in s1Count: # not a valid character, must restart
            right += 1
            left = right
            s2Count.clear()
            continue
        elif c not in s2Count:
            s2Count[c] = 1
            right += 1
        else:
            s2Count[c] += 1
            right += 1
        
        # if s2Count now invalid, keep dropping until we are okay again
        while s2Count[c] > s1Count[c]:
            s2Count[s2[left]] -= 1
            left += 1
    
    return False
        
            
            


        




# Results:
# Runtime: 86ms 38.34%
# Memory Usage: 14MB 90.14%

"""

https://leetcode.com/problems/longest-substring-without-repeating-characters/

s, string, longest substring no rpt characters

Idea:
- use a set, keep adding to window, then if rpt, drop
Time O(n). memory O(n) but you have to be that anyway since how else will you know of rpts

Tactic: Set and sliding window.

"""

def solve(s):
    left = 0
    right = 0 # non inclusive
    chars = set()
    maxSize = 0

    while left < len(s) and right < len(s):
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            maxSize = max(maxSize, len(chars))
        else:
            chars.remove(s[left])
            left += 1
    
    return maxSize



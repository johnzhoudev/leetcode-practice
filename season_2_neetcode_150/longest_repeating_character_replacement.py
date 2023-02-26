# Results:
# Runtime: 120ms 78.20%
# Memory Usage: 14MB 51.35%

"""

https://leetcode.com/problems/longest-repeating-character-replacement/

Ideas:
sliding window, keep count of how many of each character there are.
- hash table?
- for each, count number of max characters changed? technically O(1) since fixed number of english chars
- keep adding to window if num of changeable chars <= k

- max chars and total chars, keep track
- use heap? to keep track of min and max chars? or O(1) it with alphabet

s only has uppercase english letters

Idea 2:
- Trick here, we do the same thing, but we never decrement the "maxFreq" 
- Length of the sliding window will never get larger unless you get a higher real max freq!
- Try an example, aaabcdefgaaa. Then it'll make sense

Tactic: sliding window, hashmap to track freq. pro tip, keep maxFreq and don't correct when removing. valid == right - left - maxFreq <= k

"""

def solve2(s, k):
    chars = {}
    left = 0
    right = 0 # exclusive
    maxFreq = 0
    longestSubstring = 0

    while True:
        # validate first
        if right - left - maxFreq <= k: # valid
            longestSubstring = max(longestSubstring, right-left)
            # increment right
            if right == len(s): break
            if s[right] in chars:
                chars[s[right]] += 1
            else:
                chars[s[right]] = 1
            maxFreq = max(maxFreq, chars[s[right]])
            right += 1
        else: # invalid
            chars[s[left]] -= 1
            left += 1
    
    return longestSubstring









# too slow
def solve(s, k):
    # setup state
    chars = {}
    left = 0
    right = 0 # exclusive

    def validate(chars):
        maxSingleChar = 0
        numChars = 0
        for ch in chars:
            maxSingleChar = max(maxSingleChar, chars[ch])
            numChars += chars[ch]
        return (numChars - maxSingleChar) <= k

    longestSubstring = 0
    while left < len(s) and right <= len(s):
        
        if validate(chars):
            longestSubstring = max(longestSubstring, right - left)
            if right == len(s): break
            # advance right
            if s[right] in chars:
                chars[s[right]] += 1
            else:
                chars[s[right]] = 1
            right += 1

        else: # invlaid, so have to drop chars
            chars[s[left]] -= 1
            left += 1
    
    return longestSubstring








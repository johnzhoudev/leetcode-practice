"""

Return num of palindromic substrings
feels like DP

- ababa
- each letter
- Palindrome if inner range is palindrome and 2 letters outside are the same
- DP soln, O(n^2)? for each length, 
    - for each start position, add letters on each side until palindrome ends

n start positions at the letters + n-1 start positions inbetween

Tactic: Expand from middle, or DP. O(n^2) time, O(1) space for expand middle
"""

def solve(s):
    numPalindromes = 0

    # first check at each letter
    for startIdx in range(len(s)):
        start = startIdx
        end = startIdx
        while start >= 0 and end < len(s) and s[start] == s[end]:
            numPalindromes += 1
            start -= 1
            end += 1
    
    # Now check at each space
    for startIdx in range(len(s) - 1): # reprsents char left of space
        start = startIdx
        end = startIdx + 1
        while start >= 0 and end < len(s) and s[start] == s[end]:
            numPalindromes += 1
            start -= 1
            end += 1

    return numPalindromes





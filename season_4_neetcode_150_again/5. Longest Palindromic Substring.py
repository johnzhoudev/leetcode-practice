"""

longest palindromic substring

Ideas:
- dp[start][end] = is palindrome?
- dp[i][i] = true
- dp[i][j] = dp[i+1][j-1] and i == j

O(n^2) space
O(n^2) time

Don't even need dp? start from middle and go outwards?
O(1) space?
Better: Helper func for each part (eval(startidx, endIdx))

Tactic:
eval(startIdx, endIdx) helper func to grow outwards checking palindrome. Check single letter start and double letter!

"""

def solve(s):
    longestLen = 1
    startIdx = 0
    endIdx = 0

    def eval(sIdx, eIdx):
        nonlocal longestLen
        nonlocal startIdx
        nonlocal endIdx

        while s[sIdx] == s[eIdx]:
            if eIdx - sIdx + 1 > longestLen:
                longestLen = eIdx - sIdx + 1
                startIdx = sIdx
                endIdx = eIdx
            sIdx -= 1
            eIdx += 1
            if sIdx < 0 or eIdx >= len(s):
                break
    
    for x in range(len(s)):
        eval(x, x)
        if x+1 < len(s):
            eval(x, x+1)
    return s[startIdx:endIdx+1]


    
    # For each start index in the middle
    for i in range(len(s)):
        for size in range(0, len(s)): # will break
            start = i - size 
            end = i + size
            if start < 0 or end >= len(s):
                break # stop checking
            
            # for each size, increasing
            if s[start] != s[end]:
                break # Can't continue, not a palindrome
            
            # else palindrome
            if longestLen < end-start + 1:
                longestLen = end-start+1
                startIdx = start
                endIdx = end
    
    # Also do passes for if adj are palindromes
    for i in range(len(s)): # left
        for size in range(0, len(s)): # will break
            start = i - size 
            end = (i + 1) + size
            if start < 0 or end >= len(s):
                break # stop checking
            
            # for each size, increasing
            if s[start] != s[end]:
                break # Can't continue, not a palindrome
            
            # else palindrome
            if longestLen < end-start + 1:
                longestLen = end-start+1
                startIdx = start
                endIdx = end
            
    return s[startIdx:endIdx + 1]

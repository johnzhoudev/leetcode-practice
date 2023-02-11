# Results:
# Runtime: 56ms 45.58%
# Memory Usage: 14.5MB 96.50%

"""
https://leetcode.com/problems/valid-palindrome/

all uppercase to lowercase
remove non alpha

tactic: remove and count half. do smart indexing math
"""

def solve(s):

    def isalpha(c):
        return 'a' <= c and 'z' >= c or '0' <= c and '9' >= c

    newS = ""

    for ch in s.lower():
        if isalpha(ch):
            newS += ch
    
    # 12345
    # len = 5
    # check 0, 1 vs 4, 5
    for i in range(len(newS) // 2):
        if newS[i] != newS[len(newS) - i - 1]:
            return False
    
    return True

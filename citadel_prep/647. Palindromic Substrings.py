"""

647. Palindromic Substrings

number of palindromic substrings

dp
- all individual chars are palindromes
- all rpt chars are palindromes too
- from each one, try growing out

O(n^2) to check all substrings

Tactic:
Just check from each center!

"""

def solve(s):
    # cache = {} # (start, end) -> isPalindrome

    # base cases
    # for i in range(len(s)):
    #     cache[(i, i)] = True 

    # start from each character
    cnt = 0

    def getCounts(i, j):
        nonlocal cnt
        while 0 <= i and j < len(s):
            if s[i] == s[j]: 
                cnt += 1
                i -= 1
                j += 1
            else:
                break

    for center in range(len(s)):
        getCounts(center, center)
        getCounts(center, center + 1)
    return cnt

        
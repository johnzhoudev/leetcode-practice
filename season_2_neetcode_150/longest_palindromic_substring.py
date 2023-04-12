"""

https://leetcode.com/problems/longest-palindromic-substring/

- palindromic substr

Idea:
- brute force O(n^3), each substr, check pali O(n)

- Better: DP, O(n^2)
- S(i, k) = is palindrome with start at i, and end at i + k (inclusive)

S(i, 0) = True (1 letter always)
S(i, 1) = True if s[i] == s[i+1]
S(i, k) = S(i+1, k-2) and s[i] == s[i+k]

P(i, k) = is pali, start i, end k
P(i, k) = P(i+1, k-1) and ends equal
P(x, x) = True

- Iterate from each x, start at P(x, x) and iterate outwards until x < 0 or x >

- Slow becase we still eval false and continue even if previous is false


Idea2: Go from center, and eval going outwards. Break if not palindrome
- centers at each node, or inbetween. Exception is very last one

Tactic: From centre, eval outwards. O(n^2). Remeber center odd or even.

"""

def solve(s):
    if not s:
        return ""

    longestLen = 1
    ls = 0
    le = 0

    # to accomodate for double
    # assumes start to end already a palindrome
    def eval(startIdx, endIdx):
        nonlocal longestLen
        nonlocal ls
        nonlocal le

        while startIdx >= 0 and endIdx < len(s):
            if s[startIdx] != s[endIdx]:
                break
            if endIdx - startIdx + 1 > longestLen:
                longestLen = endIdx - startIdx + 1
                ls = startIdx
                le = endIdx
            startIdx -= 1
            endIdx += 1

    for x in range(len(s)):
        eval(x, x)
        if x+1 < len(s):
            eval(x, x+1)
    return s[ls:le+1]
           

# edge cases: empty str, 1 letter, 2 letters
def solve(s):
    # edge cases
    if len(s) == 0:
        return ""

    state = [[False for _ in range(len(s))] for _ in range(len(s))]

    # base conditions
    longestLen = 1
    lStart = 0
    lEnd = 0

    for i in range(len(s)):
        state[i][0] = True
        if i+1 < len(s) and s[i] == s[i+1]:
            longestLen = 2
            lStart = i
            lEnd = i+1
            state[i][1] = True
    
    # fill out going backwards
    for k in range(2, len(s)):
        for i in range(len(s)-1-k, -1, -1):
            state[i][k] = state[i+1][k-2] and s[i] == s[i+k]
            if state[i][k] and k + 1 > longestLen:
                lStart = i
                lEnd = i+k
                longestLen = k+1
    
    return s[lStart:lEnd+1]

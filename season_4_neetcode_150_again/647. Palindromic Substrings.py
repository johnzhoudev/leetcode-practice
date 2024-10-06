"""

s string - number of palindromic substrings?

Idea:
O(n^2) just build all substrings and count

Do it dp? - hard, don't even need it

Tactic:
Eval function from middle of word, growing outwards. On single letters and matching pairs!!

"""

def solve(s):
    numPalSubstr = 0

    def eval(startIdx, endIdx):
        nonlocal numPalSubstr
        while s[startIdx] == s[endIdx]:
            numPalSubstr += 1
            startIdx -= 1
            endIdx += 1
            if startIdx < 0 or endIdx >= len(s): return
    
    for i in range(len(s)):
        eval(i, i)
        if i+1 < len(s):
            eval(i, i+1)
    
    return numPalSubstr
        





# def solve(s):

#     dp = [[False for _ in range(len(s))] for _ in range(len(s))]

#     # base cases
#     for i in range(len(s)):
#         dp[i][i] = True
    
#     # pairs base cases
#     for i in range(len(s) - 1):
#         if s[i] == s[i+1]:
#             dp[i][i+1] = True
    
#     # Now build all substrings
#     for i in range()
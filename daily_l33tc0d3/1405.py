"""

https://leetcode.com/problems/longest-happy-string/

only a b c
no triple abc as substr
at most a b c occurrences

- given a b c integers, return longest possible happy string

Ideas:
- recursive dp problem? 
- Math solution? 

aabaabaab
aabbcaabbc

ababbaabbcbb
aab
abaaba

a
8a3b1c
aacaabaababa

- only an issue when you have way more of one than another that you are forced to put 3 a's in a row
and can't space anything out
- ordering arbitrary, sort descending
- DP? dp[a][b][c] = longest with a b c, ending with (a, b, c)
= max(dp[a][b][c-1]

Idea 2:
- Greedy, use largest letter that is not invalid.

Tactic: Greedy, use AA from largest pile spaced with B from medium pile.

"""

def solve(a, b, c):
    letters = [(a, 'a'), (b, 'b'), (c, 'c')]
    s = "XX"

    while True:
        letters.sort(key=lambda x : x[0], reverse=True)

        # Greedy add valid letters
        added = False
        for i in range(len(letters)):
            count = letters[i][0]
            letter = letters[i][1]

            if count == 0 or (s[-1] == letter and s[-2] == letter): # cannot add
                continue
            else:
                # can add
                s += letter
                letters[i] = (count - 1, letter)
                added = True
                break
        
        if not added:
            break

    return s[2:]





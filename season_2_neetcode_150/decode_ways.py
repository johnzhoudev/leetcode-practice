"""

https://leetcode.com/problems/decode-ways/

- ints mapped from 1 to 26, A-Z
- how many ways to decode ints?

Idea:
- search alg, either decode one way or the other.
    - take either next digit, or next 2 digits. But if next is 0 or starts with 0, return.
    - end if reach end.
- O(num solns)

Faster, DP:
- s[i] = num ways to decode up to and including i
- either from prev, add 1 char (provided it's not 0) 1-9
- or from 2 prev, add 2 char, provided it's from 10 to 26.
- s[i] = s[i-1](i is 1-9) + s[i-2](if 10-26)
    - (0)[1-9]
    - (?)(10-26)
        - (1-9)[0]
O(n) time
O(n) space
- base case, 1, 2 letters

- Edge case: leading 0
- Edge case: 2 consecutive 0's

Tactic: Tricky, d[i]=num ways decode up to i. d[i]=d[i-1](if i 1-9) + d[i-2](if 10-26). Careful with d[1] base case. (either 1 digit (not0) and rest separate, or 10-26 and prev sep)
"""

def solve(s):
    if s[0] == '0':
        return 0

    # generate state[1]
    state = [0 for _ in range(len(s))]
    state[0] = 1

    if len(s) >= 2:
        if int(s[1]) > 0:
            state[1] += 1
        if int(s[0:2]) >= 10 and int(s[0:2]) <= 26:
            state[1] += 1

    for x in range(2, len(s)):
        if int(s[x]) > 0:
            state[x] += state[x-1]
        di = int(s[x-1:x+1])
        if di >= 10 and di <= 26:
            state[x] += state[x-2]

    return state[-1]








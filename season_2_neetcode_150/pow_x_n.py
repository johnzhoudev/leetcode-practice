"""

https://leetcode.com/problems/powx-n/

Subproblems, go as big as you can and then asdf
- use n binary representation, bitshift
- get 2^i ones, and if n has a 1, mult by it

Tactic: use binary rep, if 1, mult x by currx.

"""

def solve(x, n):

    if n < 0: return 1 / solve(x, -n)

    acc = 1

    while n > 0:
        if n & 1 == 1:
            acc *= x
        x *= x
        n = n >> 1
    
    return acc

            

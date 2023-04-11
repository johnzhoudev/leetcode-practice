"""

https://leetcode.com/problems/climbing-stairs/

- n steps
- either climb 1 or 2 steps
- how many distinct ways to reach top?

Idea:
- Search alg? either climb 1 or 2 steps. But this iterates thru all possibilities. 

- DP: s[i] = num ways to reach step i
- s[i] = s[i-1] + s[i-2] # step 1 from i-1, or 2 from i-2
- base = s[0] = 1, s[1] = 1
TimeL O(n), space = O(n)
Space: O(1), only need last 2

Tactic: DP s[i] = num ways to reach step i. si = si-1 + si-2

"""

def solve(n):
    s0 = 1
    s1 = 1

    for x in range(2, n+1):
        tmp = s1 + s0
        s0 = s1
        s1 = tmp

    return s1



def solve(n):
    state = [0 for _ in range(n+1)]
    state[0] = 1
    state[1] = 1

    for x in range(2, n+1):
        state[x] = state[x-1] + state[x-2]
    
    return state[n]



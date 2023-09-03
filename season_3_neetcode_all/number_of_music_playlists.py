"""

https://leetcode.com/problems/number-of-music-playlists/

n different songs, listen to goal songs
playlist st each song played at least once
song played again only if k other songs have been played

return num possible playlists mod 10^9 + 7

Combinatorics problem?

whatever song you play at a certain point, can only play it again after k songs...
closed solution?
maintain a pool of possible songs to choose from
then num ways is multiplying choices
doesn't matter which you choose, since once a song is valid, can't play for another k


But must listen to all songs at least once - how to enforce?
eliminate possiblities? search alg?
subtract the number of ways to choose just x < n? 
n choose 1 (1 to eliminate) * regular alg for n-1 things

n * n-1 * ... * n-k * n-k-1+1 * ...
n-k ** (goal - k) + n * n-1 * ...
pool size

Not bad! 

No, I'm double counting
num ways to pick but omit one
Search alg? slow

f(4) counts ways for 3, 2, 1 item only too
-4 * f(3) counts all ways for only 3 items, plus 2 and 1 items. 
- each one has 3 items, 
- if we consider one way of doing 2 items, that would be counted twice
- so all are counted twice and were subtracted
- Additionally, all the 1 songs have been subtracted 3 times
- then add back the f(2) songs once, gives correct 2
- but f(2) adds back ways for just 1 song once. so now still subtracted 1 time over
- so add back f(1)

So in general, f(4) - 4f(3) + 4 choose 2 f(2) + ...

choice between picking unpicked and picked already, affects pool later...

# New idea: DP

state[i][j] = num ways to play i songs in j slots (guaranteed all played)
state[i][j] = state[i][j-1] * (i-k) // j-1 slots, play all songs + a random song from pool
+ state[i-1][j-1] * i * 1 // last song hasn't been played yet, so previous is 
pick 1 song missing (i) * ways. all unique since unique combos, since guaranteed to play all songs

base
state[1][j] = 1
state[k][k] = k!

Tactic: dp[i][j] = num ways to play i songs in j slots, guaranteed all played. Careful, i-k case, could be neg so max(0, i-k)
Careful: in i-k case, could be negative. don't assume this is valid. in which case, take max with 0
"""

# DP Solution
mod = 10**9 + 7
def fact(n):
    if n == 1 or n == 0: return 1
    return (n * fact(n-1)) % mod

def solve(n, goal, k):
    # init base cases
    state = [[0 for _ in range(goal+1)] for _ in range(n+1)]
    for j in range(goal+1):
        state[1][j] = 1 if k == 0 or j == 1 else 0
    for i in range(n+1):
        state[i][i] = fact(i) % mod
    
    # solve
    for i in range(2, n+1):
        for j in range(i+1, goal+1):
            state[i][j] = (state[i][j-1] * max(i-k, 0) + state[i-1][j-1] * i) % mod
    return state[n][goal]

    


# X doesn't work
def solve(n, goal, k):
    mod = 10**9 + 7
    
    def numWays(n, goal, k):
        combos = 1
        x = n
        for _ in range(k):
            combos *= x
            x -= 1
            combos %= mod
        # n * n-1 * ... * n-k+1
        for _ in range(goal-k):
            combos *= x
            combos %= mod
        return combos
    
    print(numWays(n, goal, k))
    print(numWays(n-1, goal, k) * n)
    return numWays(n, goal, k) - (n * numWays(n-1, goal, k))

# solve(2, 3, 0)
# solve(3, 3, 1)
solve(3, 3, 0)







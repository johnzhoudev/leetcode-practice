"""

https://leetcode.com/problems/stone-game-ii/

each pile has positive int of stones

M=1 initially
on each turn, take all stones in first X remaining piles, 1 <= X <= 2M
then M = max(M, X)


return max number of stones alice can get

Ideas:
- search alg, each time pick X <= 2M
- choices double each time, so it's like exponential growth in complexity

state[M][idx of remaining] => what you can get
- M must be <= half, else pointless, can just take everything
so still O(n^2)

state[m][idx] = 

- could have cases where you play any possible m, so could be anything
- different m changes the whole game

"""
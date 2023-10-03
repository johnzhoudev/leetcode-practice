"""

https://leetcode.com/problems/stone-game/

even number of piles in a row
eacvh pile has positive int piles[i]
total stones across all piles is odd
objective is to end with most stones

turns to take stones from beginning or end of row
continue until no stones left

Assume optimal play, return who wins

Ideas

- search alg for all different possible combos of taking stones, binary, so O(2^n) possible
- improve with memoization / dp?

state[num on left][num on right] => highest possible return for person to play

state[x][y] = max(x + state[x+1][y], y + state[x][y-1])
base case if no rocks, 0

- want to solve in increasing length


O(n^2)


"""

def solve(piles):
    n = len(piles)
    state = [[0 for _ in range(n)] for _ in range(n)] # base cases are 0, for y < x (no items)

    total = sum(piles)

    for l in range(n): # different interval lengths
        for start in range(n):
            # check if valid range
            if start + l >= n: break

            best = 0

            if (start+1 <= start + l):
                best = max(best, piles[start] + state[start+1][start + l])
            if (start+l-1 >= start):
                best = max(best, piles[start+l] + state[start][start + l -1])

            state[start][start+l] = best
    
    return state[0][n-1] > total - state[0][n-1]



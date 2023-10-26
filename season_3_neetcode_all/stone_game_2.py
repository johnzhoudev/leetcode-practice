"""

https://leetcode.com/problems/stone-game-ii/

each pile has positive int of stones

M=1 initially
on each turn, take all stones in first X remaining piles, 1 <= X <= 2M
then M = max(M, X)


return max number of stones alice can get

Ideas 2:
- start from back, at each position, given an M value, how many stones could you take to get highest amount?
- dp[x][m] = max sum of piles + dp[x+k][new m] for 1 <= k <= 2M
- O(n^3)?
- x inc, m inc

- Refactor, dp[x][m] = number of stones more that you could get vs your opponent
- so dp[x][m] = max sum of piles - dp[x+k][new m]
- then total is how much you could get more, so total - x / 2 + asdf

Works, but slow. Can we do faster?

"""

def solve(piles):

    total = sum(piles)
    n = len(piles)
    dp = [[float('-inf') for _ in range(n + 1)] for _ in range(n+1)]

    # base cases, if 1 elt left, take for any M
    for m in range(1, n+1):
        dp[n-1][m] = piles[-1]
        dp[n][m] = 0 # out of bounds
    
    # now do dp
    for m in range(n, 0, -1):
        for x in range(n-1, -1, -1):
            rollingSum = 0
            for k in range(0, 2 * m): # take stones from x to x + k inclusive
                if x + k >= n: break
                rollingSum += piles[x + k]
                dp[x][m] = max(dp[x][m], rollingSum - dp[x + k + 1][max(k+1, m)]) # careful with iteration direction and little numbers! what is k? def needs to be clear
    
    return ((total - dp[0][1]) // 2) + dp[0][1]



"""
Ideas

- m is either same, so less than m taken before, or X.
- alice plays optimally, would have played turn before with best value of state[m][idx] for prev
- always best to play with minimal M, since with larger M bob could just choose to take less?

- go backwards?
- no, m could grow exponentially

-> choose 1 <= x <= 2M
state[m][idx] = best score

brute force, store m and idx left and do search alg
- m could grow exponentially, so need smarter soln than dp
- but m is bounded by n, since can't take more

-> can take 1 to 2m items, or less than n
dp[m][idx] = sum of taken + dp[new m][idx + num taken]
- new m is min(m, X)

O(n^3), On2 dp's plus on to solve each

"""
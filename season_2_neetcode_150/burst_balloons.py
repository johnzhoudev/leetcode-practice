"""

https://leetcode.com/problems/burst-balloons/

- n balloons
- each has a number on it

- burst i, then you get i-1 * i * i+1 coins. if out of bounds, treat as 1

- have to burst all balloons. What order?
- could do search alg, but then all permutations. n!

- search alg with memoization, just set of items left. O(2^n)

Smaller cases:
- [3, 5] - which to burst first?
    - 3, then 5 shows up twice

- [1, 3, 5] - 3, 15, 15
- [3, 5] - 15, 15 - lost no potential value
- vs [1, 5] - +15, now 5, 5 (lost 20 potential value)

- [3,1,5,8] - 3, 15, 40, 40
- if remove 3, 1,5,8 - +3, 5,40,40  - 10 potential value
- if remove 1, 3,5,8 - +15, 15, 120, 40 - gained potential value

Idea:
- dp[x][y] = best value bursting balloons s[x:y+1]
- needs to have -1 and len vals
- dp[x][y] = max(each inbetween * right outside + the best value for all subsets)
- O(n^2) * O(n) = O(n^3)

Tactic: Tricky DP, dp[x][y] = best val bursting nums[x:y+1], = max(z from x to y * right outside + best val of divided parts). Careful to iterate from smaller to larger parts

"""

def solve(nums):
    dp = [[0 for _ in range(len(nums) + 2)] for _ in range(len(nums) + 2)] # have dummy's on each side

    # base case, for each elt, value is 1
    # rest is 0
    for idx, num in enumerate(nums):
        dp[idx][idx] = num
    
    # do dp
    for l in range(0, len(nums)):
        for start in range(len(nums)):
            end = start + l
            if end >= len(nums):
                break

            maxVal = 0
            left = nums[start-1] if start-1 >= 0 else 1
            right = nums[end+1] if end+1 < len(nums) else 1
            for last in range(start, end+1):
                maxVal = max(maxVal, nums[last] * left * right + dp[start][last-1] + dp[last+1][end])
            dp[start][end] = maxVal

    return dp[0][len(nums) - 1]







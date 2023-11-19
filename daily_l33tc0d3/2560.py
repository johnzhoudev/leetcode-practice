"""
https://leetcode.com/problems/house-robber-iv/

cannot steal from adjacent homes

capability = max money he steals from one house
nums
k = min number of houses to steal from

return min capability of all possible ways to steal at least k houses

Ideas
- only consider stealing k houses, if steal more, just don't
- ways to steal from k houses, minimizing the largest amount of money stolen

Naive: get all k combos and get min. could do search alg, for all cases either use or not, break if more than k
O(2^n)

dp? dp[i][k] = from houses 0 to i, robbing k houses, what is capability?
dp[i][k] = min(dp[i-1][k] -> not exist for edge, just take max, max(nums[i], dp[i-1][k-1]))
O(n^2)
Base cases, k = 0 means 0, and solve diagonally starting at k = i


shoot, can't do adjacent ones
dp[i][k] = min(dp[i-1][k] (don't take), max(nums[i], dp[i-2][k-1]))
But base cases are a bit crazy, need to take given i elts, max k would be all the odds, separated
    - ie at a given k, the min i needed would be 2k - 1 with value ...

FAIL: TLE, need to do faster...


TODO: Binary search on sorted values, and verify at least k of the indices below are not adjacent
- put all indices into set, and go thru (max n possible indices) and could adjacent / 2

Tactic: Koko eating bananas! binary search on value, and just check if all below has enough for k!
"""

def solve(nums, k):

    def validate(indices, k):
        largest = max(indices)
        indices = set(indices)

        i = 0
        num_houses = 0
        while i <= largest:
            if i in indices:
                num_houses += 1
                i += 1 # skip next
            i += 1
        return num_houses >= k
    
    nums = sorted([(nums[i], i) for i in range(len(nums))])
    indices = [num[1] for num in nums]

    # do binary search, inclusive
    left = 0
    right = len(nums) - 1

    while left < right:
        pivot = left + (right - left) // 2 # bias left

        # if possible, could be smaller, so go left
        if validate(indices[:pivot + 1], k):
            right = pivot # still valid
        else:
            left = pivot + 1
        
    # at end, left = right
    return nums[left][0]


def solvedp(nums, k):
    n = len(nums)
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # base cases diagonal
    largestOdd = 0
    for i in range(1, k+1):
        largestOdd = max(nums[i*2 - 1 - 1], largestOdd)
        dp[(i * 2) - 1][i] = largestOdd
    
    # dp
    for j in range(1, k+1):
        for i in range(j * 2, n+1):
            dp[i][j] = min(dp[i-1][j], max(nums[i-1], dp[i-2][j-1]))

    return dp[n][k]



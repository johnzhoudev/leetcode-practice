
"""

subarray with largest product
return product

brute force: O(n^2) try all combos

Store max and min

dp[i] = (max, min) product ending in i
dp[i] = max(i, i * dp[i-1][0]), min(i, i * dp[i-1][1])
O(n)

Tactic:
dp[i] = (max, min) product ending at nums[i]. dp[i] = max(i, i*dp[i-1][0], i*dp[i-1][1])

"""

def solve(nums):
    dp = [(0, 0) for _ in range(len(nums))]
    dp[0] = (nums[0], nums[0])
    actualMax = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]
        maxNum = max(n, n * dp[i-1][0], n * dp[i-1][1])
        minNum = min(n, n * dp[i-1][0], n * dp[i-1][1])
        dp[i] = (maxNum, minNum)
        actualMax = max(maxNum, actualMax)
    
    return actualMax
    

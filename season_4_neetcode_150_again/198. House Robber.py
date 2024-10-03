"""

198. House Robber

2 adj houses, security contacted

nums

max amt to rob without alerting police

dp[i] = max money robbed up to this house
dp[i] = max(nums[i] + dp[i-2], dp[i-1] # don't rob house)

"""

def solve(nums):
    if len(nums) == 1: return nums[0]
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]
"""

213. House Robber II

circle street
adj houses => police

max money?

do 2 dp's: first house removed and last added, and first added last removed.
take max.

"""

def solve(nums):
    if len(nums) == 1: return nums[0]

    def dp(values):
        if len(values) == 1: return values[0]
        dp = [0 for _ in range(len(values))]
        dp[0] = values[0]
        dp[1] = max(values[0], values[1])

        for i in range(2, len(values)):
            dp[i] = max(dp[i-1], dp[i-2] + values[i])
        return dp[-1]
    
    return max(dp(nums[1:]), dp(nums[:-1]))

        
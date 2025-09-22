"""

213. House Robber II

houses arranged in a circle
cannot rob 2 adjacent houses in the same night

Find max amount of money you can rob without alerting police?

dp[i] = max money you can get up to house i
dp[i] = max(dp[i-1], dp[i-2] + val[i])

Do 2 runs, 1 with first house and without last house, one with last house no first house

O(n) time

"""

def solve(nums):
    if len(nums) == 1:
        return nums[0]

    def helper(nums):
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # dp step
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
    
    return max(helper(nums[:len(nums) - 1]), helper(nums[1:]))
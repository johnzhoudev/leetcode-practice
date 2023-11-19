"""
https://leetcode.com/problems/house-robber-ii/
house robber 2

- idea, rob [1:] and [:-1] since either can use 1st (then can't use last) or can use last but can't use first


regular

dp[i] = best from using 0 to i
dp[i] = max(dp[i-1], i + dp[i-2])
"""

def solve(nums):

    if len(nums) == 1:
        return nums[0]

    def helper(nums):
        # regular solve
        dp = [nums[0]]

        if len(nums) == 1:
            return dp[-1]
        
        dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            dp += [max(dp[i-1], nums[i] + dp[i-2])]
        
        return dp[-1]
    
    return max(helper(nums[1:]), helper(nums[:-1]))

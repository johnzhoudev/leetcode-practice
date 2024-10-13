"""

312. Burst Balloons

- ballons with numnbers on them
- bursting a balloon gives value n-1 * value n * value n + 1 on it
- can burst all the balloons
- if goes out of bounds, pretend it's a balloon with value 1 - doesn't contribute to multiplication
- max coins?

brute force:
- try bursting random balloons at a time
    - O(n!) => permutations of the balloons
- are you doing duplicate work?

- greedy?
- dp subproblems?

- dp[i][k] = best way to pop sections [i:k]
- dp[i][k] = for each popping point, add + best ways to pop sides
- dp[i][k] with len 0 is just that.

GENIUS!

- problem: you merge the two sides...the sides affect the outcome.
- Soln: treat as last thing you pop => sides known!

O(n^3)

Tactic:
dp[i][k] = best sum when popping from [i..k], taking into account left and right edges.
dp[i][k] = max(left * right * nums[pivot] + dp[i][pivot-1] + dp[pivot+1][k])
- treat pivot as LAST ITEM to be popped. Then subproblems, the edges are defined!
"""

def solve(nums):
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))] # value popping these last

    # base cases
    # for each section of length 1, just 1 number
    # WRONGN! Need to be the num * left * right
    for i in range(len(nums)):
        dp[i][i] = (nums[i-1] if i-1 >= 0 else 1) * nums[i] * (nums[i+1] if i+1 < len(nums) else 1)

    def getPoppingValue(dp, start, end, popIdx, left, right):
        if end - start + 1 == 1: return nums[start] * left * right # only 1 in list

        if popIdx == start: return (left * nums[start] * right) + dp[start + 1][end] # left end
        if popIdx == end: return (right * nums[end] * left) + dp[start][end - 1] # right end
        else: return (nums[popIdx] * left * right) + dp[start][popIdx - 1] + dp[popIdx + 1][end]

    # dp step - need to increase in size
    for size in range(2, len(nums) + 1):
        for start in range(len(nums)):
            end = start + size - 1 # inclusive
            # bounds check
            if end >= len(nums): break # only going to get bigger
            bestValue = 0
            left = nums[start-1] if start-1 >= 0 else 1
            right = nums[end+1] if end + 1 < len(nums) else 1

            for pop in range(start, end + 1):
                print(start, end, pop, getPoppingValue(dp, start, end, pop, left, right))
                bestValue = max(bestValue, getPoppingValue(dp, start, end, pop, left, right))
            dp[start][end] = bestValue

    return dp[0][len(nums)-1]





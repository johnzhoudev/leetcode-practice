"""

https://leetcode.com/problems/longest-increasing-subsequence/

- longest increasing subsequence - delete some or none of elts, but maintain order
- 2^n subsequences / sets

Ideas
- O(n^2) time,
- d[x] = length of longest subsequence ending at x
- just need to check all elts before it, and look.
- tricky scenario - all elts increasing, then huge outlier increase, then rest good. how to do in O(n) time?

Ideas contd: O(n) time? O(n log n)?

Tactic: DP, dx = len of longest subseq ending at x. must search all before it.

WHY THIS IS NOT MARKED AS DONE: Traditional dp uses O(n^2), but there exists a non-triv O(n log n) soln.

"""

def solve(nums):
    state = [1 for _ in range(len(nums))]
    longest = 1

    for idx, num in enumerate(nums):
        largestLessThan = 0 # len of largest subsequence still less than num, before num
        for k in range(idx):
            if nums[k] < num:
                largestLessThan = max(largestLessThan, state[k])
        state[idx] = largestLessThan + 1
        longest = max(longest, state[idx])
    return longest
    




"""
Try 2

- len of longest strictly inc subsequence

dp[i] = longest inc subs ending at nums[i]
dp[i] = max dp[k] for k in 1 to i

O(n^2)

"""

def solve(nums):
    dp = [0 for _ in range(len(nums))]

    for idx, num in enumerate(nums):
        best = 1
        for k in range(0, idx):
            if nums[k] < num:
                best = max(best, dp[k] + 1)
        dp[idx] = best
    return max(dp)
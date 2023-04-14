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

WIP

Tactic: DP, dx = len of longest subseq ending at x. must search all before it.

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
    




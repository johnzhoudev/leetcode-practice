"""

https://leetcode.com/problems/maximum-subarray/

- find subarray with largest sum and return
    - subarray = contiguous segment

Ideas:
- greedy, when consider num i, either use previous sum or just num, depending on what's bigger.
    - proof: if previous sum + num bigger than just num, better to start from prev.
    - else, better to start anew

Tactic: at each num, either use prev sum if prev + num > just num. Else start anew.


"""

def solve(nums):
    best = nums[0]
    curr = nums[0]
    for idx, num in enumerate(nums):
        if idx == 0: continue
        if curr + num > num:
            curr += num
        else:
            curr = num
        best = max(curr, best)
    return best
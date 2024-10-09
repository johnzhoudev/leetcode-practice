"""

300. Longest Increasing Subsequence

given int arr nums
len of longest strictly increasing subsequence - not contiguous?

brute force:
- check all subsequences, 2^n * n

dp[i] = what's longest subsequence length ending at i?
O(n^2)

tails approach:

tails[i] = min final element of all tails of length i. 
- for each elt, binary search on tails[i]. find one that's less than nums[i], and so you can add to it.
- tails[i-1] < x <= tails[i], update tails[i] to be min(num[i], tails[i]). or append new.

Tactic:
dp[i] = longest subsequence ending at i? dp[i] = max(dp[j] + 1 for all j under i, given nums[j] < nums[i])
Better O(n log n): tails array, tails[i] = min final elt of all tails of len i. Binary search on tails to find
tail[i-1] < x <= tails[i], and update tails[i] = min(nums[i], tails[i]) and ret len(tails)
"""

def solve(nums):
    if len(nums) == 0: return 0
    tails = [nums[0]]

    # finds i s.t. tails[i] < num, max(tails[i])
    def binary_search(tails, num):
        left = 0
        right = len(tails) - 1 # inc
        while left < right:
            pivot = left + (right - left + 1) // 2 # bias right

            if tails[pivot] < num:
                left = pivot # Pivot still valid
            else:
                right = pivot - 1
        
        if left == right and tails[left] < num: return left
        return -1 # Not found

    for num in nums[1:]:
        i = binary_search(tails, num)
        if i == -1: # couldn't find anything less than num
            tails[0] = min(tails[0], num)
        if i == len(tails) - 1:
            tails.append(num) # larger than all
        else:
            tails[i+1] = min(tails[i+1], num)
    
    return len(tails)




def solve(nums):
    dp = [1 for _ in range(len(nums))] # base case, each has len 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    
    return max(dp)

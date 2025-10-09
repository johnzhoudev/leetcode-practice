"""

560. Subarray Sum Equals K

Rolling window? not really because could be negative.
Try all subarrays then
dynamic programming, lengths

or, carry forward set of all subarray lengths ending in the previous one?
O(n)?
When you move forward, have to update all sums + k
O(n^2) eventually

TLE!

OMG fail

store rolling sums.
Then at each position, 
value = dp[0,j] - dp[0,i] + num[i] 
given j, need to know if k - dp[0, j] = num[i] - dp[0, i]
So keep a set?

value = sum(0, j) - sum(0, i) or 0, and need an i that makes value = k
-(k - sum(0, j)) must be in sum list

smart!!!

Tactic: HARD. O(n). k = sum(0,j) - sum(0,i)(or 0, sub nothing) for some i < j. 
So keep rolling sums and if sum(0,j) - k in the rolling sums = sum(0,i) or 0, then soln. Count sums since could be more than 1!


"""

from collections import defaultdict

def solve(nums, k):
    dp = defaultdict(lambda: 0) # set of sums
    dp[0] += 1
    total = 0
    count = 0

    for num in nums:
        total += num
        # total is now sum(0, j)
        value = total - k
        if value in dp:
            count += dp[value]
        dp[total] += 1
    
    return count

print(solve([1, 1, 1], 2))


def solve(nums, k):
    total = 0

    # Base cases
    for num in nums:
        if num == k:
            total += 1
    dp = nums[:] # len 1

    for length in range(2, len(nums) + 1):
        new_dp = [0 for _ in range(len(nums))]
        for start in range(len(nums) - length + 1):
            end = start + length - 1 # inclusive

            total_sum = dp[end-1] + nums[end]
            # print(length, start, end, total_sum)
            if total_sum == k:
                total += 1
            new_dp[end] = total_sum
        dp = new_dp
    
    return total

print(solve([1, 1, 1], 2))
        



        
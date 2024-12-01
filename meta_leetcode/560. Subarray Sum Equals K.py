"""

560. Subarray Sum Equals K

nums
k
subarrays with sum equal to k?
- contiguous non-empty sequence

Ideas:

Rolling window?
- if too big, decrease left
- if too small, increase right

Nums could be negative, so further increasing might get better

O(n^2) brute force, check every subarray

Better way?

dp[i] = sum of values from i to end

let me just try now
TLE

How to elmiminate cases?

Must be rolling window?

[1, 2, 1, -2, -1, -3] = 1

maybe store deltas at each idx?

O(n) time?

Tactic:
Can go forwards or backwards. if dp[i] = sum of elts up to including i, add that new sum to a hash map counter.
Every time you get a sum, if sum - k has been reached before, then there exists a new subarray containing k

"""

from collections import defaultdict

def solve(nums, k):
    deltas = defaultdict(lambda : 0)

    totalWays = 0
    total = sum(nums)
    for i in range(len(nums) - 1, -1, -1):
        deltas[total] += 1
        total -= nums[i]
        # total(prev) + k = deltatotal
        if total + k in deltas:
            totalWays += deltas[total + k]
    
    return totalWays
        



from collections import defaultdict

def solve(nums, k):
    deltas = defaultdict(list)

    total = 0
    for idx, num in enumerate(nums):
        total += num
        deltas[total].append(idx)
        # deltas[total] existing means the sum from 0 to idx is total
        # can help because say you're at idx 1. you know the previous before was 3 = prevweight
        # need total - prevweight = k. so want to know if there's a total = k + prevweight with idx >= curr.
        # could do binary search on list for even faster
    
    totalWays = 0
    prevTotal = 0
    for idx, num in enumerate(nums):
        if k + prevTotal in deltas:
            idxList = deltas[k + prevTotal]
            for i2 in idxList:
                if i2 >= idx:
                    totalWays += 1
        prevTotal += num
    return totalWays



def solve(nums, k):
    totalWays = 0
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            if total == k:
                totalWays += 1
    
    return totalWays


"""
https://leetcode.com/problems/delete-and-earn/

int array nums
- max number of points by performing an operation any number of times
- pick nums[i] and delete it to earn nums[i] points
- then, must delete every element equal to nums[i] -1 and every element equal to nums[i] + 1
- but doesn't delete the num

- value of each point is itself minus the value of the surrounding if deleted. but all dependent

1,2,3,4,5

- get counts of all elts
- can check counts of related elts
- dp? what is max number of points with those elts left?grpah

just 1, 1
just 1 and 2, either delete 2 or 1
1,2,3, del 3, then value of 1. else del 2, then it
1,2,3,4 del 4, then value of 1,2. del 3, val of 1

dp[x] = best you can do using nums up to x, either keep or get deleted
dp[x] = max(if used, left bound. or if immediate left exists, immediate left (skipped))

O(n log n)

can you do it without the sort?

"""

from collections import defaultdict

def solve(nums):
    # first get frequencies and also sort unique nums
    numSet = set()
    totals = defaultdict(lambda : 0)
    for num in nums:
        totals[num] += num
        numSet.add(num)
    
    sortedNums = sorted(numSet)

    # now do dp with each num
    dp = {}

    for idx, num in enumerate(sortedNums):
        # if previous not in, cannot be erased, so just add
        if (num-1 not in dp):
            lastTotal = dp[sortedNums[idx-1]] if idx-1 >= 0 else 0
            dp[num] = totals[num] + lastTotal
        else:
            lastLastTotal = dp[sortedNums[idx-2]] if idx-2 >= 0 else 0
            # previous in, so could be erased.
            dp[num] = max(dp[num-1], totals[num] + lastLastTotal)
    
    return dp[sortedNums[-1]]






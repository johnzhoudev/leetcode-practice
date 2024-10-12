"""

nums
target
- make an expression using + and -

number of different expressions, evaluating to target?

Brute force, search algorithm?
- each one, add or subtract
- O(2^n)

- states[x] = num of ways to reach sum x 
for each number - add the ways
O(n * total) time?
O(total) space

states[numidx][amt] = num ways to get to amt using numbers 0 to numidx
# either add number or subtract number
dp[i][amt] = dp[i-1][amt - nums[i]] + dp[i-1][amt + nums[i]]

- can't use 1d array since updates come from both directions

Tactic:
Knapsack. Easier with dfs(numidx, currSum) + memoization. 
- better memory wise since you only reach sums you reach.

"""

def solve(nums, target):
    cache = {}

    def dfs(total, numIdx):
        # check end condition
        if numIdx == len(nums):
            if total == target:
                return 1
            return 0 # not a solution
        
        # check cache
        if (total, numIdx) in cache: return cache[(total, numIdx)]

        # do work
        totalWays = dfs(total - nums[numIdx], numIdx + 1) + dfs(total + nums[numIdx], numIdx + 1)
        cache[(total, numIdx)] = totalWays
        return totalWays
    
    return dfs(0, 0)
        

def solve(nums, target):
    total = sum(nums)
    # range from -total to 0 to total
    totals = [0 for _ in range(total + 1 + total)] # use negatives to access

    def getIdx(amt):
        return amt + total
    
    def isInRange(idx):
        return 0 <= idx and idx < len(totals)

    # Base case
    totals[getIdx(0)] = 1

    for numIdx in range(len(nums)):
        newTotals = [0 for _ in range(total + 1 + total)]
        for amt in range(-total, total + 1):
            num = nums[numIdx]
            newTotals[getIdx(amt)] = totals[getIdx(amt - num)] if isInRange(getIdx(amt - num)) else 0# if you add
            newTotals[getIdx(amt)] += totals[getIdx(amt + num)] if isInRange(getIdx(amt + num)) else 0# Sub
        totals = newTotals
    
    return totals[getIdx(target)] if isInRange(getIdx(target)) else 0





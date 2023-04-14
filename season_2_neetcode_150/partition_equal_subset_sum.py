"""

https://leetcode.com/problems/partition-equal-subset-sum/

- partition array into 2 subsets such that sum is equal
- t / f

Brute Force: O(2^n) * n all subsets test and check
- can write a search alg and dfs on this

subproblem?

- Don't think there's a way to do it without checking each subset. ie you could 

Idea:
- search alg to find subsets, but use memoization to cache results
    - do dfs, lets say, just for example
    - 
- only need to find target = half of regular

Idea:
- basically 0/1 knapsack problem. 
- d[i][k] = using elts 0 to i, can we make combo of k weight?
- d[i+1][k] = d[i][k] or d[i][k-w[i]] # use or don't use

- target = total / 2
- fail if not even
- can we make a subset equaling target? 
- dp[i][s] = can i make sum s using elts 0-i?
- dp[i][s] = dp[i-1][s] or dp[i-1][s-x[i]] # use i or not

- base case, dp[-1][0] = False

Faster Idea:
- For dp, we store index. But if we go thru in order, we don't care. just add total to available sums
- Maintain set of reachable sums for each number. O(n * target) time, just check if target in there.

Tactic: Target = sum(nums) / 2. Fastest, maintain set of reachable sums for each number, and expand. Also Knapsack DP works. Also dfs with memoization, but TLE.

"""

def solve(nums):
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums) // 2
    candidates = set()
    candidates.add(0)

    for num in nums:
        candidateCopy = candidates.copy()
        for c in candidates:
            if c + num == target:
                return True
            if c + num < target:
                candidateCopy.add(c + num)
        candidates = candidateCopy
    return False

def solve(nums):
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums) // 2
    dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    # base cases
    for x in range(target + 1):
        dp[-1][x] = False
    dp[-1][0] = True
    
    for x in range(0, len(nums)):
        for s in range(target + 1):
            if s - nums[x] < 0:
                dp[x][s] = dp[x-1][s]
            else:
                dp[x][s] = dp[x-1][s] or dp[x-1][s - nums[x]]
    
    return dp[len(nums)-1][target]



    

x =[[True, True, False, False, False, False, False, False, False, False, False, False], [True, True, False, False, False, True, True, False, False, False, False, False], [True, True, False, False, True, True, True, False, False, False, False, True], [True, True, False, False, True, True, True, False, False, True, True, True], [True, False, False, False, False, False, False, False, False, False, False, False]]
for row in x:
    print(row)





# TLE
def solve(nums):
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums) / 2
    nums.sort(reverse=True)

    def dfs(idx, currSum, visited):
        if (idx, currSum) in visited:
            return False
        
        visited.add((idx, currSum))

        if currSum == target:
            return True # found
        
        for x in range(idx, len(nums)): 
            if currSum + nums[x] <= target:
                if dfs(x+1, currSum + nums[x], visited):
                    return True
        return False
    
    return dfs(0, 0, set())
    

# TLE
def solve(nums):
    # get target
    target = sum(nums) / 2

    # state = deque()
    # state.append((0, 0)) # idx, currSum
    state = [(0, 0)]
    visited = set() # idx + currSum to check if already visited

    while state:
        idx, currSum = state.pop()
        if (idx, currSum) in visited:
            continue
        visited.add((idx, currSum))
        if currSum == target:
            return True
        # otherwise add all subproblems
        # either use idx, or not

        for x in range(idx, len(nums)):
            if currSum + nums[x] <= target:
                state.append((x+1, currSum + nums[x]))

    return False




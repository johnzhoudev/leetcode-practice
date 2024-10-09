"""

416. Partition Equal Subset Sum

nums - ints
partition in 2
sum of both subsets equal
or false otherwise

Ideas:
- sorting might help?

Brute force alg:
- all subsets, do sum, and then check against rest
    - O(2^n)

Idea:
- generate all subsets as a set, and add to them
- O(n * size of sum set)

- Reduces to seeing if you can find a set of numbers summing to target = sum / 2
- 01 knapsack? 
dp[i][w] = can you sum using 0toi to weight w

Tactic:
But faster, do iterative set of sums and expand per number. if reach target, done.
Reduces to 01 knapsack, sum to target = sum(nums) // 2. dp[i][w] = dp[i-1][w] or dp[i-1][w-num]
"""

def solve(nums):
    if sum(nums) % 2 == 1: return False
    target = sum(nums) // 2
    # Setup state
    dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
    # dp[i][w] = can we, using nums[0:i-1], make a sum of weight w

    # base cases
    for i in range(len(nums) + 1):
        dp[i][0] = True
    
    # magic step of dp
    for i in range(1, len(nums) + 1): # Start at 1?
        for w in range(target + 1):
            num = nums[i - 1]
            if w - num < 0:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w] or dp[i-1][w-num]
            
            if w == target and dp[i][w]: return True
    
    return dp[-1][target]


# def solve(nums):

#     # edge case, odd sum
#     if sum(nums) % 2 == 1: return False # can't split in 2
#     target = sum(nums) // 2

#     # make the state set
#     sums = set() # sums seen so far
#     sums.add(0) # base case, we have 0

#     for num in nums:
#         newSums = set(sums)
#         for total in sums:
#             newSum = total + num
#             if newSum > target: continue
#             if newSum == target: return True
#             newSums.add(newSum)
#         sums = newSums
    

#     return False


def validate(nums, expected):
    res = solve(nums)
    if res == expected:
        # print("Passed test!", nums, "Expected:", expected)
        pass
    else:
        print("FAILED TEST", nums)
        print("Result:", res, "Expected:", expected)

validate([1, 2, 5, 6], True)
validate([1, 2, 5, 5], False)
# validate([], True)
validate([1], False)
validate([1, 1], True)
validate([6, 5, 2, 1], True)

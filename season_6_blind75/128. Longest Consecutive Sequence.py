"""

128. Longest Consecutive Sequence

longest consecutive elements sequence

doesn't have to be in order

dict num to consecutive
if in dict already, return
store max
store nums

Key idea: If x-1 is not in set, it's the start of the streak

Tactic: Turn to set. Then walk up from each number, using dfs cache. OR, check number is start (num-1 not in set) and walk up.

"""
from collections import defaultdict

def solve(nums):
    num_set = set(nums)
    best = 0
    for num in nums:
        if (num - 1) in num_set:
            continue
        y = num + 1
        while y in num_set:
            y += 1
        best = max(best, y - num)
    
    return best



from collections import defaultdict

def solve(nums):
    num_set = set(nums)
    best = 0
    for num in nums:
        if (num - 1) in num_set:
            continue
        count = 0
        while num in num_set:
            num += 1
            count += 1
        best = max(best, count)
    
    return best

print(solve([1, 2, 3, 4]))

def solve2(nums):
    num_set = set(nums)
    counts = defaultdict(lambda: 0) # doubles as cache

    def dfs(num):
        # If cached
        if num in counts:
            return counts[num]

        count = 1
        next_num = num + 1

        if next_num in num_set:
            count += dfs(next_num)

        counts[num] = count
        return count

                
    best = 0
    for num in nums:
        best = max(dfs(num), best)
    
    return best



    

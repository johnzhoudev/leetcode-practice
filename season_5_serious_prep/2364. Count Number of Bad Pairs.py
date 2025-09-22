"""

2364. Count Number of Bad Pairs

nums[j] - nums[i] == j - i
implies nums[j] - j == nums[i] - i

So count all sums and figure out

Tactic: Trick! nums[j] - nums[i] == j - i => nums[j] - j == nums[i] - i

"""
from collections import Counter, defaultdict

def solve(nums):
    n = len(nums)

    counts = defaultdict(lambda : 0)
    for i in range(n):
        counts[nums[i] - i] += 1
    total = 0
    for c in counts.values():
        total += (c * (c - 1)) // 2 # number of valid pairs
    
    return ((n * (n - 1)) // 2) - total

def solve(nums):
    n = len(nums)
    counts = Counter([num - i for i, num in enumerate(nums)])
    total = sum([(c * (c-1)) // 2 for c in counts.values()])
    return ((n * (n - 1)) // 2) - total

    







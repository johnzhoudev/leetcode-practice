"""

268. Missing Number


Idea:
- add up, subtract, boom

"""

def solve(nums):
    total = sum(nums)
    n = len(nums)
    return int((n + 1) * (n / 2)) - total
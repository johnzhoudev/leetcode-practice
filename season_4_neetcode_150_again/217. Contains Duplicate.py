""""

https://leetcode.com/problems/contains-duplicate/description/

int array nums
true if any val appears twice
else false

"""

def solve(nums):
    seen = set()
    for num in nums:
        if num in seen: return True
        seen.add(num)
    return False
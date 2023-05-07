"""

https://leetcode.com/problems/jump-game/

nums, each elt is max jump length at  that position
- true if can reach last index, else false

Ideas
- search alg? or DP, record best jump to be reached?

- Or just go thru, for each number update max capable of being reached
O(n) time, const space

Tactic: go thru, best you can reach is max of best, and i + nums[i]. Either reach end, or stop short.

"""

def solve(nums):
    best = 0 # can only reach 0
    i = 0
    while i <= best:
        if i == len(nums) - 1:
            return True
        best = max(best, i + nums[i])
        i += 1
    return False
    
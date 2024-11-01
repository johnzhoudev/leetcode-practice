"""

55. Jump Game

array 1
max jump length at position

can u reach last idx, or false?

Ideas:
- each time you jump, new available. Go thru and keep increasing max until reached
O(n)

Tactic:
Greedy, for each number increase highest reached. Go thru until can't.

"""

def solve(nums):
    highest = 0
    curr = 0

    while curr <= highest:
        highest = max(highest, nums[curr] + curr)
        if highest >= len(nums) - 1: return True
        curr += 1
    
    return False





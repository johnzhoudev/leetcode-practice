"""

45. Jump Game II

min number of jumps?

Ideas:
- go in waves, count number of loops to get to new reachables
O(n) time

Tactic:
greedy, go in waves to reach newhighest. Each wave, update numJumps. Check for no jump trivial case.

"""


def solve(nums):
    if len(nums) == 1: return 0

    highest = 0
    curr = 0
    numJumps = 0
    # enter the loop => make a jump
    while True:
        newHighest = highest
        numJumps += 1 # make first jump

        while curr <= highest:
            newHighest = max(newHighest, curr + nums[curr])
            if newHighest >= len(nums) - 1: return numJumps
            curr += 1
        
        # end condition
        if highest == newHighest: break # hit ceiling
        highest = newHighest
    
    return -1 # unreachable
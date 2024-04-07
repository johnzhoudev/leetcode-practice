"""

https://leetcode.com/problems/jump-game-ii/description/

nums[i] = max number of jumps forward
start at nums[0]
Min number of jumps to reach nums[n-1]?

Ideas:
Brute force, search algorithm, O(2^n) or something like that.

DP? Search alg with memoization? 

dp[i] = min number of jumps to reach i
dp[i] = just fill in, going in order. take min.  
O(n^2) - best already

Go backwards? can you look up? or binary search somehow? x
dp[i] = num jumps to get to end
dp[i] = 

def can do faster, O(n)?

Alt soln: from 0, jump to best. then work backwards, find max next distance. 
then jump and repeat, until get to end. O(n)

Tactic: 2 pointer ranges thing. Just go from start and count backwards to extend reach.
"""

def solve(nums):
    n = len(nums)
    if n == 1: return 0
    numJumps = 1
    right = nums[0]
    left = 0


    while right < n-1: # Not reachable end
        bestJump = -1
        for i in range(left, right + 1):
            bestJump = max(bestJump, i + nums[i])

        left = right + 1 
        right = bestJump
        numJumps += 1
    
    return numJumps



def solve(nums):
    # First, make state
    n = len(nums)
    state = [float('inf') for i in range(n)]
    state[0] = 0

    for (idx, num) in enumerate(nums):
        for dest in range(idx + 1, min(idx + num + 1, n)):
            state[dest] = min(state[dest], state[idx] + 1)
    
    return state[-1]



"""

https://leetcode.com/problems/jump-game-ii/

- nums
- max len forward jump
- return min number of jumps to reach nums[n-1]

Ideas
- brute force, do search alg and consider every possibliity - slow
- DP / memoization? - going to be min of each thing, not that much better
    - dp + memoization might be best bet, how to know when to backtrack?
    - unless there exists a greedy solution, but don't think there is. can't tell which one is best

- So let's do search alg + memoization
dp[i] = smallest jump to get to end from index i
- for each i, need to calc for all smaller ones and min the ones of the reachable.
- break early if already reached point with more than best?

O(n^2) time, O(n) space

Idea2: Iterate forwards, but store min num jumps to get to a number (as you go)
- originalyl all infinity
- then if reachable, best = min(curr + 1, best)
- then reach end
- No, still O(n^2)

Idea 3: Greedy, O(1) space?
- can't do it going forward because then you'd have to know which one to pick. But impossible to know
- Backwards?
    - doesn't necessarily work either, can't tell what's the best jump going backwards in O(1) time

Idea 4: 
- jump to the next index that has the greatest reach
- tip, don't have to recompute at each index, since you know when you jump that that num was the largest

Idea5: iterate thru, and update currFarthest. Then, only update numJumps if you get to currEnd, and on next, set currEnd = currFarthest (requires a jump)
- keep track of current end and next end. increment num jumps when you PASS current end (means you jumped), or you reach the end
- There must be a cleaner way of doing this.
- 

Invariant: when you are handling a row, you haven't jumped to any of them yet. So start at -1
- Then, when you reach the end, on last one, signifies you've jumped to one of them
- Also currEnd = min(nextEnd, len(nums))

Tactic: Greedy, jump to next in range that gives largest reachable. Fancy way, keep currEnd and nextEnd. always expand nextEnd, and if reach currEnd, numJumps += 1. invar, while processing, haven't jumped to elt in [start, currEnd]. currEnd = min n-1, nextEnd for last jump. start numJumps -1
"""

def solve(nums):
    numJumps = -1
    currEnd = 0 # so will add a jump to 0
    nextEnd = 0

    for i in range(len(nums)):
        # first update next end, since if we add the jump, still could technically be larger
        nextEnd = max(nextEnd, i + nums[i])

        if i == currEnd:
            currEnd = min(nextEnd, len(nums) - 1)
            numJumps += 1
        
        if i > currEnd:
            return -1
        
    return numJumps


def solve(nums):
    numJumps = 0
    lastComputed = 0
    currIdx = 0

    while currIdx != len(nums) - 1:
        # try to jump to another idx
        bestReachable = currIdx
        jumpToIdx = currIdx
        while lastComputed < currIdx + nums[currIdx]:
            lastComputed += 1
            if lastComputed == len(nums) - 1: return numJumps + 1
            if bestReachable < lastComputed + nums[lastComputed]:
                bestReachable = lastComputed + nums[lastComputed]
                jumpToIdx = lastComputed
        if jumpToIdx == currIdx: return -1
        currIdx = jumpToIdx
        numJumps += 1
        
        # now bestReachable is 
    return numJumps



        
        



def solve(nums):
    dp = [-1 for _ in range(len(nums))]
    # state = [0] # start at index 0

    def dfs(currIdx):
        if currIdx == len(nums) - 1:
            return 0 # need 0 jumps
        
        if dp[currIdx] != -1:
            return dp[currIdx]

        # else, try jumping to anything in range
        best = float("inf")
        for next in range(currIdx+1, min(len(nums), currIdx + nums[currIdx] + 1)):
            best = min(best, 1 + dfs(next)) # take 1 jump
        dp[currIdx] = best
        return best
    
    return dfs(0)



        

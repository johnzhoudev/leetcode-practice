# Results:
# Runtime: 40ms 71.69%
# Memory Usage: 14.1MB 49.83%

"""

https://leetcode.com/problems/permutations/

- Given nums, return all possible permutations
- nums are distinct

Idea:
- backtracking alg, which to choose on ith one.
O(n!) time, to get permutations, copy over, etc

- recursive

Tactic: Backtrack on choosing num to add, since all unique. Use set. Careful in for loops, modifying set.

If had to do for non-unique characters, do same but do checks
    - or could choose position of repeated characters first, then rest.

"""

def solve(nums):

    original = set(nums)
    state = []
    solns = []

    def backtrack(state, leftSet):
        if len(leftSet) == 0:
            solns.append(state.copy())
        else:
            for num in leftSet.copy():
                state.append(num)
                leftSet.remove(num)
                backtrack(state, leftSet)
                leftSet.add(state.pop())
    
    backtrack(state, original)

    return solns





# Results:
# Runtime: 56ms 86.12%
# Memory Usage: 14MB 60.6%

"""

https://leetcode.com/problems/combination-sum/


candidates, taret int target
- all unique combos of candidates summing to target
- return combinations in any order
- can choose from candidates unlimited times
- unique combos < 150

Ideas:
- Can do a search algorithm looking at all combos - fail when sum is greater. 
- O(n^n) combinations, pretty much, to check - but may be okay if 
- Total number combos? hard to calculate, each permutation will have own combos
- Is there a smarter way than checking all combinations? Otherwise no. 
    - can store solutions - make a hash map of combos as you go - then you have existing solutions
    - Or dp? 
- how to know you've saturated all combos unless you go thru them all? - yeah don't think memory will help here

Idea:
- Going to do a search algorithm / backtracking, adding numbers to a set in order. Once over target, return. if equal, continue.
    - will sorting help? nah, considering all possiblities anyway

Max recursion depth exceeded

Alternate ideas? Could do a heap based thing
1. add og combo to stack
pop
check sum
add childs
- can get unique if iterate in order, never add from behind

Tactic: Classic backtracking. Either do recursive or iterative. To avoid repeats, only add from idx


--- Trying Again

Tactic: Classic backtrack. What is the ith item to add, in order. Avoid repeats, only add idx.

"""



def solveIterative(candidates, target):

    state = [([], 0, 0)]
    output = []

    while state:
        currSoln, rollingSum, fromIdx = state.pop()
        if rollingSum > target:
            continue
        elif rollingSum == target:
            output += [currSoln[:]]
            continue
        else:
            for i in range(fromIdx, len(candidates)):
                state.append((currSoln + [candidates[i]], rollingSum + candidates[i], i))
    
    return output



def solve(candidates, target):

    # init state
    output = []

    def backtrack(currentCombo, rollingSum, fromIdx):
        nonlocal candidates
        nonlocal output
        if rollingSum > target:
            return
        elif rollingSum == target:
            output += [currentCombo.copy()]
            return
        else: # rolling sum < target
            for i in range(fromIdx, len(candidates)): # can add any number of times
                currentCombo += [candidates[i]]
                backtrack(currentCombo, rollingSum + candidates[i], i)
                currentCombo.pop() # remove

    backtrack([], 0, 0)

    return output

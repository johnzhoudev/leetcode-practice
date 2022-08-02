# Recursion backtracking
# Results:
# Runtime: 75ms 93.73%
# Memory Usage: 13.9MB 92.52%

# Hash map solution
# Results:
# Runtime: 89ms 86.10%
# Memory Usage: 15.3MB 6.02%

"""
Combination Sum

Backtracking:
- idea is to just iterate thru all possible combinations
- O(n * num partial combinations) runtime
- O(longest combo) space, not counting solution


DP / Backtracking:
- Idea is to also iterate thru all possible combos - does filter out ones that are too big
- But this one does take extra time appending the combinations to make more
  - actually, no. each partial combination is only possibly appended to at most n times
- Time: O(num partial combinations * n)
- Space: O(num partial combinations * partial combo size) (big)
- like if we did the backtracking but didn't pop, but rather just appended a whole new soln.

distinct int array candidates
target 
Return list of unique combos of candidates that sum to target
- can choose same number unlimited times
- <150 combos sum to target - maybe optimize?


Basically do a search alg? Each active config is a set of numbers - next is choose to add
another number, cannot add if over the sum. Store in hashmap of arrays?

Runtime: Hard to analyze
- for each element, start inserting it into every thing, multiple times too. Multiple appends
- Only insert once for each number, but go in ascending order. This works:
proof: consider a combo with more than 1 of the num. if we insert in order, sum - num will be complete. Then
handle.
- O(target * combinations to insert * numCandidates)

Space: O(possible combinations, n!)


Tactic: Backtracking alg, recursive, and build the curr combo dynamically to save space. Also only add curr index and onwards.

"""

def tryCombinations(candidates, target, lastAddedIndex, currentCombination, rollingSum, solutions):
  # At this point, combination should still be valid and in progress

  # Also only add last added thing and onwards
  for i in range(lastAddedIndex, len(candidates)):

    if (candidates[i] + rollingSum == target):
      solutions.append(currentCombination + [candidates[i]])
    elif (candidates[i] + rollingSum < target):
      # now, add
      currentCombination.append(candidates[i])
      tryCombinations(candidates, target, i, currentCombination, rollingSum + candidates[i], solutions)
      # once finished, pop off
      currentCombination.pop()

def combinationSumBacktracking(candidates, target):
  # state for backtracking
  # Initial config = start with each num
  currentCombination = []
  solutions = []
  tryCombinations(candidates, target, 0, currentCombination, 0, solutions)
  return solutions



def combinationSum(candidates, target):
  # 1. create the map from 0 to target
  combinations = [[] for _ in range(target + 1)] # combinations[val] = combinations that sum to val

  # 2. for each number in candidates, go thru all values with combos in it and add and write soln.
  for num in candidates:
    for prevVal in range(len(combinations)):
      if ((prevVal == 0 or len(combinations[prevVal]) != 0) and (prevVal + num) <= target): # if first item or non-empty list, add
        # Append num to each combination group, and extend the combinations for the new val.
        # Only extend each value once.
        if (prevVal == 0):
          combinations[prevVal + num].append([num])
        else:
          combinations[prevVal + num].extend([x + [num] for x in combinations[prevVal]])

  return combinations[target]

# testing
def validate(candidates, target, expected):
  # combinationsResult = combinationSum(candidates, target)
  combinationsResult = combinationSumBacktracking(candidates, target)
  combinationsResult.sort()
  expected.sort()
  if (combinationsResult != expected):
    print("Test Failed")
    print("Result: ")
    print(combinationsResult)
    print("Expected: ")
    print(expected)
    print()
  
validate([1], 6, [[1, 1, 1, 1, 1, 1]])
validate([1, 3], 3, [[1, 1, 1], [3]])



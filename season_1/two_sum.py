# Results: 
# Runtime: 87ms 65.78%
# Memory Usage: 15.4 9.08%

# int array nums
# integer target
# return indices of two numbers so they add to target
# Can assume each input has exactly 1 solution, cannot repeat elements
# Can return elements in any order

# Restrictions on number size? Overflow concerns?
# can nums be empty, and sum 0? -> no

# Ideas
# Brute force: test every pair, O(n^2)
# DP: Preprocess array and hashmap (target - A[i]) -> i, so on second run thru, just check if value key exists and if so, return.
# - skip if current key = hashed key index result, since cannot use same

from shutil import ExecError


def twoSumSolve(arr, target):
  hashmap = {}

  # First loop to add values to dict
  for i, num in enumerate(arr):

    # if there is a solution, first will be added, then second must match.
    if (num in hashmap): # Handles duplicate numbers since we check before adding
      return [i, hashmap[num]]

    hashmap[target - num] = i
  
  raise ExecError("Should not reach here. Solution doesn't exist for " + str(arr))

def validate(arr, target, expected):
  result = twoSumSolve(arr, target)
  result.sort()
  expected.sort()
  if (result != expected):
    print("Expected: ", end='')
    print(expected)
    print("Result: ", end='')
    print(twoSumSolve(arr, target))


validate([2, 7, 11, 15], 9, [0, 1])
validate([5, 5, 2, 34, 453], 10, [1, 0])
validate([-100, -20], -120, [1, 0])
validate([1, 2, 3, 4, 5, 6], 11, [4, 5])
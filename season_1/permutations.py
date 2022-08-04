# Results:
# Runtime: 46ms 85.75%
# Memory Usage: 14.1MB 58.61%

"""
Permutations
Given array of distinct ints, return all possible permutations

Brute force: go item by item, choose one of the n and remove and continue.
- could do a backtracking alg here, and reuse solutions / keep memory efficient

"""

def tryPermutations(numSet, currentPermutation, solutions):
  # if finished, no more numbers
  if (len(numSet) == 0):
    solutions.append(currentPermutation.copy())
  else:
    # Not finished, continue adding.
    numsToTest = list(numSet)
    for num in numsToTest:
      currentPermutation.append(num)
      numSet.remove(num)
      tryPermutations(numSet, currentPermutation, solutions)
      numSet.add(num)
      currentPermutation.pop()
  
def permutations(nums):
  numSet = set(nums)
  solutions = []
  currentPermutation = []
  tryPermutations(numSet, currentPermutation, solutions)
  return solutions

def validate(nums, expected):
  result = permutations(nums)
  if (result != expected):
    print("Test Failed")
    print("Result: ")
    print(result)
    print("Expected: ")
    print(expected)


validate([1, 2], [[1, 2], [2, 1]])
validate([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    

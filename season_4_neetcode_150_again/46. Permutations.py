"""


https://leetcode.com/problems/permutations/description/

- distinct integers, return all possible permutations
- do dfs? for each position, choose all available

O(n factorial)

"""

def solve(nums):
  available = set(nums)
  solns = []
  curr = []

  def dfs(num):
    # num is in available
    available.remove(num)
    curr.append(num)

    if len(available) == 0:
      solns.append(curr.copy())
    else: # continue searching
      nextAvailable = list(available)
      for x in nextAvailable:
        dfs(x)

    curr.pop()
    available.add(num)
  
  for x in nums:
    dfs(x)
  return solns
    





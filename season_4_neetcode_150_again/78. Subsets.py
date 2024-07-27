"""

78. Subsets

- given unique elements
- return all possible subsets, including empty set

Idea:
- for each thing, add or not
- make array and copy over, backtracking

O(2**n)

"""

def solve(nums):
  solns = [[]]
  curr = []

  def dfs(i):
    if i >= len(nums): return

    # Add i
    curr.append(nums[i])
    solns.append(curr.copy())
    dfs(i+1)

    # or without i
    curr.pop()
    # soln alr inside
    dfs(i+1)
  
    return

  dfs(0)

  return solns




def solve(nums):
  solns = [[]]

  for x in nums:
    solns += [soln + [x] for soln in solns]
  
  return solns



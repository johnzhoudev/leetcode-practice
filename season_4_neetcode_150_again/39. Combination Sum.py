"""

https://leetcode.com/problems/combination-sum/

distinct int candidates
target int target
all unique combinations of candidates summing to target
- can choose number from candidates any number of times

Ideas:
- search alg, but track nums used and numbers left to use
- at each state, choose which one to add
- if goes over, break


"""

def solve(candidates, target):
  solns = []

  curr = []
  total = 0

  def dfs(idx):
    nonlocal curr
    nonlocal total
    if idx >= len(candidates): return

    # If invalid, over target
    if total + candidates[idx] > target: return

    # Add
    curr += [candidates[idx]]
    total += candidates[idx]
    
    if total == target:
      solns.append(curr.copy())
      # don't continue
    
    # Else continue
    for i in range(idx, len(candidates)):
      dfs(i)
    
    # Remove and return
    total -= candidates[idx]
    curr.pop()
    return
    
  
  for i in range(len(candidates)):
    dfs(i)
  return solns
    

    




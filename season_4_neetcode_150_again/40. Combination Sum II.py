"""

40. Combination Sum II

all unique combos summing to target
duplicate nums
each num can only be used once
No duplicate combinations

Ideas:
- sort first
- subsets ii but only add if hit target, and don't continue if over total

Tactic: Like subsets ii, either add next if dupe or continue past

"""


def solve(candidates, target):

  candidates.sort()
  solns = []
  state = []
  total = 0

  def dfs(i):
    nonlocal total
    num = candidates[i]
    state.append(num)
    total += num

    if total == target:
      solns.append(state.copy())
    elif total < target:
      for k in range(i+1, len(candidates)):
        if k == i + 1 or candidates[k] != candidates[k-1]:
          dfs(k)
    
    state.pop()
    total -= num
  
  for i in range(len(candidates)):
    if i == 0 or candidates[i] != candidates[i-1]:
      dfs(i)
  
  return solns



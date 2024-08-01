"""

90. Subsets II

- if could contain duplicates, return power set

Ideas:
- same, just keep set of lists and check? or use frozen list?
- or, easily, when going just choose how many of each you want to add. Do a prelim sort
- either add or skip to next one

Tactic: Easy=turn to unique nums and keep count, and advance for each count. Use idx. Another=dfs, but either dfs next OR advance to next non dupe.

"""

from collections import defaultdict

def solve(nums):
  solns = [[]]
  state = []
  nums.sort()

  def dfs(idx):
    num = nums[idx]
    
    state.append(num)
    solns.append(state.copy())

    for i in range(idx+1, len(nums)):
      if i != idx + 1 and nums[i] == nums[i-1]: continue
      dfs(i)
    
    state.pop()

  for i in range(len(nums)):
    if i == 0 or nums[i] != nums[i-1]:
      dfs(i)
  
  return solns



def solve(nums):
  solns = [[]]
  state = []
  
  uniqueNums = list(set(nums))
  numsDict = defaultdict(lambda : 0)
  for num in nums:
    numsDict[num] += 1

  def dfs(i):
    # add this num
    num = uniqueNums[i]

    numNums = numsDict[num]

    for _ in range(numNums):
      state.append(num)
      solns.append(state.copy())

      for k in range(i+1, len(uniqueNums)):
        dfs(k)
    
    for _ in range(numNums):
      state.pop()
    
  
  for i in range(len(uniqueNums)):
    dfs(i)
  
  return solns
      






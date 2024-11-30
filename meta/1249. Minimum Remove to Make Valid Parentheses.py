"""
- closing bracket, have to remove if no matching opening brackets
- opening bracket, no matching closing bracket - have to remove as well

- 

Time: O(n)
O(n) (((((((((

"""

def solve(s):
  stack = [] # (idx, type of bracket)
  bracketsToRemove = set()

  # first pass, stack of all brackets and their indices
  for idx, c in enumerate(s):
    if (c == '('):
      stack.append((c, idx))
    elif c == ')':
      if len(stack) > 0:
        stack.pop()
      else:
        bracketsToRemove.add(idx)
  
  # could be some opening brackets
  for c, idx in stack:
    bracketsToRemove.add(idx)
  
  # 2nd pass, create the output string
  outputStr = ""
  for idx, c in s:
    if idx in bracketsToRemove:
      continue
    outputStr += c
  
  return outputStr

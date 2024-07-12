"""

1717. Maximum Score From Removing Substrings

Ideas:

- search alg on each string, which ab or ba to remove?
- Or some DP storing what the substrings are?

- Is there ever a scenario not to play greedy and remove larger if possible?
- if same, remove randomly bc always able to collapse
- if diff, and can remove larger, do it. 

Suppose you get more points for removing ba than ab. the danger is if you do ba, then miss out on more opportunity to do ba.
- but never the case since always will exhaust a or b in each set, and removing just joins other sides which doesn't reduce opportunity

baabaaaab

TLE??

- case is when aaaaaaaabbbbbbbbbb
- check for this case and totally remove

Idea better: Just like valid parentheses, but with 2 stacks. 

Tactic: Greedy to add best score. To deal with aaaaabbbbb case, use stack like valid parentheses. Can be done in 2 passes shuffling between 2 stacks.

"""

def solve(s, x, y):
  if x < y:
    return solve(s[::-1], y, x) # reverse order
  
  # do first pass to get all ab
  totalScore = 0
  stackLeft = []
  for c in s:
    if c != 'b':
      stackLeft.append(c)
    else: # is b, try to reduce
      if stackLeft and stackLeft[-1] == 'a':
        stackLeft.pop()
        totalScore += x
      else:
        stackLeft.append(c)
  
  # Now prioritize other one
  stackRight = []
  while stackLeft:
    c = stackLeft.pop()
    if c != 'b':
      stackRight.append(c)
    else:
      if stackRight and stackRight[-1] == 'a':
        totalScore += y
        stackRight.pop()
      else:
        stackRight.append(c)
  
  return totalScore
      

print(solve("cdbcbbaaabab", 4, 5))

def solve(s, x, y):
  # greedy remove larger
  prioritizeAB = x > y

  # Use a stack
  def removeABOrBA(s, c1, c2):
    numRemoved = 0
    substrings = s.strip('|').split('|')

    newStrings = []

    for string in substrings:
      newString = ""
      stack = []
      for c in string:
        if c == c1:
          stack.append(c1)
        elif c == c2 and stack:
          stack.pop()
          numRemoved += 1
        else: # just c2
          newString += c2
      while stack:
        newString += stack.pop()
      newStrings += [newString]

    return '|'.join(newStrings), numRemoved

  def removeSplittingStrings(s):
    result = ""
    currentlySplitting = False
    for i in range(len(s)):
      if s[i] != 'a' and s[i] != 'b' and not currentlySplitting:
        currentlySplitting = True
        result += '|'
      elif s[i] == 'a' or s[i] == 'b':
        result += s[i]
        currentlySplitting = False
    return result

  totalScore = 0
  s = removeSplittingStrings(s)

  # first try to remove AB, then BA if none. If both cannot, do nothing.
  while True:
    if prioritizeAB:
      c1 = 'a'
      c2 = 'b'
      multiplier = x
      otherMultiplier = y
    else:
      c1 = 'b'
      c2 = 'a'
      multiplier = y
      otherMultiplier = x

    s, numRemoved = removeABOrBA(s, c1, c2)
    totalScore += numRemoved * multiplier

    if numRemoved == 0:
      s, numRemoved = removeABOrBA(s, c2, c1)
      totalScore += numRemoved * otherMultiplier

      if numRemoved == 0: break
  
  return totalScore

print(solve("cdbcbbaaabab", 4, 5))
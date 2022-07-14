# Results:
# Runtime: 51ms 41.19%
# Memory Usage: 13.9MB 69.80%

# Idea 1: Need to make sure open brackets are closed, and correctly closed. Inner closed first, before outer.
# Can use stack, push bracket types on stack and pop when encounter closed bracket. if matching, all good.
# O(n) time, O(k) space where k is number of brackets

def isValid(s):
  stack = []
  bracketMap = {
    "(": ")",
    "{": "}",
    "[": "]",
  }

  for c in s:
    # if (c == '(' or c == '[' or c == '{'):
    if (c in bracketMap):
      stack.append(c)
    else:
      if (len(stack) == 0): return False
      openingBracket = stack.pop()
      if (bracketMap[openingBracket] != c): return False
  
  # at end, stack must be empty
  return len(stack) == 0

def validate(s, expected):
  if (isValid(s) != expected):
    print("Expected: " + str(expected))
    print("Result: " + str(isValid(s)))
    print(s)


validate("()", True)
validate("([])", True)
validate("([]", False)
validate("([)]", False)
validate("([][])", True)
validate("{}[]()}", False)
validate("{{}[]()}", True)
validate("(((((((((())))))))))", True)

"""

125. Valid Palindrome

lowercase
remove non alpha numeric

.lower()
.isalnum()

2 pointers

Tactic:
.lower() and .isalnum(), 2 pointers

"""

def solve(s):
    s = ''.join([c.lower() for c in s if c.isalnum()])
    
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]: return False
        left += 1
        right -= 1
    
    return True

# solve("asfdkfja@F#JKFA1231LKJFDJKLASF")


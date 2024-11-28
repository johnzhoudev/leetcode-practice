"""

680. Valid Palindrome II

s 
true if palindrome if del 1 character
- palindrome = forwards backwards same

naive

To choose which one, have to be able to take 1 step

bcaaacbc

Better:
- on first err, just try rest with left removed, then try again with right

Tactic:
No way to tell just from error case which character to take, so just manually test both.
on err, if not removed, solve[left+1:right+1] (minus left) or solve[left:right] (minus right)

"""

def solve(s, removed = False):

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if not removed:
                return solve(s[left+1:right+1], removed=True) or solve(s[left:right], removed=True)
            else:
                return False
        
        left += 1
        right -= 1
        
    return True

def solve(s):

    left = 0
    right = len(s) - 1
    removed = False
    while left < right: 
        print(s[left], s[right], left, right)

        # mismatch
        if s[left] != s[right] and not removed:
            # try and resolve
            # special case: only 1 char left after remove, or 2 chars
            if s[left+1] == s[right] and ((right - (left + 1) <= 1) or s[left + 2] == s[right - 1]):
                left += 1
            elif s[left] == s[right - 1] and ((right - 1 - (left) <= 1) or s[left + 1] == s[right - 2]):
                right -= 1
            else:
                return False
            # both cannot be done
            removed = True
            assert(s[left] == s[right])
        elif s[left] != s[right]: 
            print(s[left], s[right], left, right)
            return False
        
        left += 1
        right -= 1
        print(s[left], s[right], left, right)
    
    return True

        



print(solve("acxcybycxcxa"))
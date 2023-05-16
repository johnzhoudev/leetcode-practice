"""

https://leetcode.com/problems/plus-one/

Given array of digits
- increment by 1

Ideas:

tactic: use carry! start from lowest and continue. If get to end, append 1 to front.

"""

def solve(digits):

    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
        else:
            return digits # if successfully added, break
    
    # if got to last one, append a new one 
    return [1] + digits
            

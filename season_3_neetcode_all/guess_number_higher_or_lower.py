"""

binary search
1 to n
guess is higher or lower
use guess(int num) api
-1 is greater
1 is less than pick
0 is equal

Tactic: binary search

"""

def guess(n):
    pass

def solve(n):
    left = 1
    right = n

    while 1 <= left and left <= right:
        g = left + (right - left + 1) // 2 # bias right
        comp = guess(g)
        if comp == -1: # greater
            left = g - 1
        elif comp == 1:
            right = g + 1
        else:
            return g
    
    return -1




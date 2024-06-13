"""

https://leetcode.com/problems/complement-of-base-10-integer/description/




"""
print(1 << 2)

def solve(n):
    # reverse using bit arithmetic
    if n == 0: return 1
    x = 0
    base = 1
    while n > 0:
        x += base * (1 - (n & 1))
        n = n >> 1
        base *= 2
    
    return x



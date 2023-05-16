"""

https://leetcode.com/problems/happy-number/

- replace with square of digits
- if 1, stop
- if loops, continue
- keep seen set?

Tactic: use set to keep seen, and adv thru.

"""

def solve(n):
    seen = set()
    while n not in seen:
        if n == 1:
            return True
        seen.add(n)

        new = 0
        while n > 0:
            new += (n % 10) * (n % 10)
            n = n // 10
        n = new

    return False
        
        
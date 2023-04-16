"""

https://leetcode.com/problems/burst-balloons/

- n balloons
- each has a number on it

- burst i, then you get i-1 * i * i+1 coins. if out of bounds, treat as 1

- have to burst all balloons. What order?
- could do search alg, but then all permutations. n!

- search alg with memoization, just set of items left. O(2^n)

Smaller cases:
- [3, 5] - which to burst first?
    - 3, then 5 shows up twice

- [1, 3, 5] - 3, 15, 15
- [3, 5] - 15, 15 - lost no potential value
- vs [1, 5] - +15, now 5, 5 (lost 20 potential value)

- [3,1,5,8] - 3, 15, 40, 40
- if remove 3, 1,5,8 - +3, 5,40,40  - 10 potential value
- if remove 1, 3,5,8 - +15, 15, 120, 40 - gained potential value

"""
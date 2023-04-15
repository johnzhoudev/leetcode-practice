"""

https://leetcode.com/problems/burst-balloons/

- n balloons
- each has a number on it

- burst i, then you get i-1 * i * i+1 coins. if out of bounds, treat as 1

- have to burst all balloons. What order?
- could do search alg, but then all permutations. n!

- search alg with memoization, just set of items left. O(2^n)

"""
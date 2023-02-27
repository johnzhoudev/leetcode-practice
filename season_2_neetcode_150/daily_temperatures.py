"""

https://leetcode.com/problems/daily-temperatures/

num days to wait for a warmer temperature

Ideas:

brute force O(n^2) look ahead

monotonic decreasing stack
- but thing is, every elt only gets pushed and popped once on there. so overall runtime O(n)
space: O(n) worst case

"""


"""

https://leetcode.com/problems/minimum-interval-to-include-each-query/

size of interval is right - left + 1

queries array
- want to find size of smallest interval i s.t. query value contained in i. else -1
- everything is too big to hash.

Brute force: O(nq), check each interval

Operations
- sorting intervals, O(n log n)

- say you were able to look up 

"""
"""

https://leetcode.com/problems/non-overlapping-intervals/

Ideas:
- greedy? go thru, and remove interval that overlaps with the most intervals?
    - but how to determine?
- overlap count? remove until overlap count is 0 for all remaining

O(n^2), go thru and for each interval, count how many it overlaps with. store.
- 

"""
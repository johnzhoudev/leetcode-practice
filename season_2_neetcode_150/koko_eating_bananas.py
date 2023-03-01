# Results:
# Runtime: 387ms 95.29%
# Memory Usage: 15.2MB 99.92%

"""
https://leetcode.com/problems/koko-eating-bananas/

piles[i] bananas
guards come back after h hours
k = banana per hour eating speed
minimum k such that she can eat all the bananas in h hours

Idea:
- given k, can compute how many hours it takes
    - for each pile, ceil divide by k
    - O(n) time to do for each pile

- max speed is largest pile of bananas
- min speed? 1 banana per hour
- binary search

Total: O(n * log (maxbanana)) time

Fuck this is hard

Tactic: binary search and naievely compute time. Careful with binary search, bias left and keep some results as valid! then round at end if search fails


"""

from math import ceil

def solve(piles, h):

    def computeTime(k):
        totalHours = 0
        for num in piles:
            totalHours += ceil(num / k)
        return totalHours
    
    left = 1
    right = max(piles) # inclusive
    pivot = -1

    while left < right: # if one elt left, don't infinite loop
        pivot = left + (right - left) // 2 # bias left, so if we hit a bunch of valid times, we sweep left
        time = computeTime(pivot)
        if time < h: # too fast. decrease, but still keep viable
            right = pivot # Keep this result as valid!
        elif time > h: # too slow. increase speed
            left = pivot + 1
        else: # if exactly equal, try for less
            right = pivot
        
    # if get to this point, do rounding
    time = computeTime(pivot)
    return pivot if time <= h else pivot + 1
    





    




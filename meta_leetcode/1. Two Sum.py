"""

1. Two Sum


indices, add up to target
cannot use same elt twice

Use a hash table
- take difference as key
- value will be index

one pass to build hash table, and as we build, we check

O(n) time and space

Tactic:
1 pass hash table, track difference.

"""

def solve(nums, target):
    ht = {}

    for idx,num in enumerate(nums):
        if num in ht: return (idx, ht[num])
        ht[target - num] = idx
    
    raise RuntimeError()
"""

128. Longest Consecutive Sequence

put all elts into a set, then for each element count up and cache

Tactic: Check if smaller elt is in set. if not, then start of sequence. Count up. O(1) space!


"""

def solve(nums):
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num-1 in num_set:
            continue
        length = 0
        while num in num_set:
            length += 1
            num += 1
        best = max(best, length)
    return best
        

def solve_old(nums): # This gets TLE but should work!!! :(())
    num_set = set(nums)
    cache = {}
    best = 0
    for num in num_set: # Deduplicate
        if num in cache: # Already parsed
            continue

        length = 1
        curr = num
        while curr + 1 in num_set:
            if curr + 1 in cache:
                length += cache[curr + 1]
                break # done
            curr += 1
            length += 1
        cache[num] = length
        best = max(best, length)
    return best
    
        


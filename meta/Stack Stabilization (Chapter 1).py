"""

Stack Stabilization (Chapter 1)

n inflatable discs
ith disc from top having radius ri inches
unstable if at least one disc radius >= underneath

- can deflate discs, by integer
- positive integer radius

min number of discs to deflate?

list given from top to bottom

Just walk thru, keep track of last and if needs to shrink
- if get to <= 0, -1

"""

def solve(n, r):
    last = r[-1]
    numShrinks = 0
    for i in range(len(r) - 2, -1, -1):
        disk = r[i]
        if disk >= last:
            last = last - 1
            if (last <= 0): return -1 # impossible shrink
            numShrinks += 1
        else:
            last = disk
    
    return numShrinks

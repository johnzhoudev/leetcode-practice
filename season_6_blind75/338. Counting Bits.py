"""

338. Counting Bits

use previous to count?

max_bit_count = 1, 2, 3...
once reached max bit count, increase and add all previous

Tactic: Once reached max bit count, reset idx to 0 and next item is 1 + res[idx] (reusing old numbers)

Tricky to implement!

"""

def solve(n):
    res = [0]

    idx = 0 # Idx of current number to add to next number
    last_largest_idx = 0 # Last largest idx
    for i in range(n):
        if idx > last_largest_idx: # Haven't added idx yet
            idx = 0
            last_largest_idx = i

        res.append(res[idx] + 1)

        idx += 1
    return res

print(solve(5))





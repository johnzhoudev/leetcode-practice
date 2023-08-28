"""

given l and r nums, count num odd numbers

tactic: left odd, right even, take num numbers div bty 2


"""

def solve(l, r):
    if l % 2 == 0: l += 1
    if r % 2 != 0: r += 1

    return (r - l + 1) // 2
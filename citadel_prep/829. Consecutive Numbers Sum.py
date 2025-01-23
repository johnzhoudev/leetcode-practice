"""

829. Consecutive Numbers Sum

consecutive numbers meet n

sliding window? - too many, n <= 10^9...or maybe O(n) okay?


consecutive numbers: ((min + max) / 2) * n = total

n = (max - min) + 1

((min + max) / 2) * (max - min + 1) = total, given min and max

O(n) math solution?

Other soln, different equation. don't use max or min

n = k + k + 1 + ... + k + (i - 1) (so i terms)
Then n = k * i + (i (i - 1) / 2)
=> so as long as n - (i (i - 1) / 2) is divisible by i, we have soln since we can calc k

need n > i(i-1) / 2 (i or k can't be zero), thus we only try sqrt(n) combos

Tactic: 
n = k + (k + 1) + ... + k + (i - 1). So n - (i (i - 1) / 2) == ki gives soln. Only have to test n > i i-1 / 2.

"""
import math

def solve(n):
    cnt = 0
    i = 1
    while (i * (i-1)) // 2 < n:
        if (n - (i * (i-1) // 2)) % i == 0:
            cnt += 1
        i += 1
    return cnt
        

def solve(n):

    def eval(k):
        disc = 2 * n + (k * k) - k
        a = math.floor(math.sqrt(disc))
        return a * (a + 1) == disc
    
    total = 0
    for i in range(1, n + 1):
        if eval(i): total += 1
    return total


print(solve(5))
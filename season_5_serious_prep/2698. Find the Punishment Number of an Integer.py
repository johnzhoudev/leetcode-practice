"""

2698. Find the Punishment Number of an Integer

- i^2, need to sum digits to i
- just do search alg?


Optimizations:
- check if target < 0 or num < target
- only take 1, 2 or 3 digits (use moduolo?) since number < 1000
- Or just hardcode 29 numbers
"""

def solve(n):

    def canReachTarget(k: list[int], target: int, start):
        curr = 0

        if target < 0: return False

        for idx in range(start, len(k)):
            curr = curr * 10 + k[idx]

            if target - curr < 0:
                return False

            if curr == target and idx == len(k) - 1:
                return True
            elif canReachTarget(k, target - curr, idx + 1):
                return True
        
        return False

    def isPunishmentNumber(k):
        kq = str(k**2)
        digits = [int(x) for x in kq]
        return canReachTarget(digits, k, 0)

    for i in range(1001):
        if isPunishmentNumber(i):
            print(i)

    tot = 0
    for i in range(n+1):
        if isPunishmentNumber(i):
            tot += i**2
    return tot


solve(38)

def solve(n):
    nums = [0,
        1,
        9,
        10,
        36,
        45,
        55,
        82,
        91,
        99,
        100,
        235,
        297,
        369,
        370,
        379,
        414,
        657,
        675,
        703,
        756,
        792,
        909,
        918,
        945,
        964,
        990,
        991,
        999,
        1000]
    tot = 0
    for num in nums:
        if num <= n:
            tot += num**2
    return tot


solve(2)

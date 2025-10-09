"""

50. Pow(x, n)

calc x ^ n

binary exponentiation

"""

def solve(x, n):
    if n < 0:
        return 1/solve(x, -n)
    carry = x
    total = 1

    while n:
        if (n & 1) == 1:
            total *= carry
        n >>= 1
        carry *= carry
    return total


print(solve(2, 4))
print(solve(2, 0))
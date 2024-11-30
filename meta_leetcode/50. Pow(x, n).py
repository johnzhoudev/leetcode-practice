"""

50. Pow(x, n)

Do some binary exponentiation

calculate x ^ n

x^n = x^1 * x^2 * x^4 * ... 
where x^i present if n = 2^i +...

what if n is negative?
- calculate divisor as well

Tactic:
Binary exponentiation!


"""

def solve(x, n):

    if n < 0:
        divisor = solve(x, -n)
        return 1 / divisor
    
    assert(n >= 0)

    acc = 1 
    xacc = x

    while n:
        # ones digit in n, add xacc
        if n & 1: 
            print(xacc)
            acc *= xacc
        n >>= 1

        xacc *= xacc
    
    return acc
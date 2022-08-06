"""
Implement pow(x, n) calculates x ^ n

-2^31 <= n <= 2^31
-100 <= x <= 100

Best way? Divide and conquer? or DP?
x ^ 10
x1 ^ x1 = x2 * x2 = x4 * x4 = x8 * x2 = x10
Doubling
use binary representation
need to calculate up to floor(log base 2 (n))

Better than naive way


"""

def quickLog(n):
  comparer = 1
  while (n < )

def pow(x, n):
  # 1. figure out states we need to calculate
  numSubproblems = 

x = 7
x = x >> 2
print(x)
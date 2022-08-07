# Results:
# Runtime: 50ms 45.96%
# Memory Usage: 13.9MB 68.27%

"""
Implement pow(x, n) calculates x ^ n

-2^31 <= n <= 2^31
-100 <= x <= 100

Best way? Divide and conquer? or DP?
x ^ 10
x1 ^ x1 = x2 * x2 = x4 * x4 = x8 * x2 = x10
Doubling
use binary representation
need to calculate up to floor(log base x (n))

How to handle negative exponents?
- just remove neg, calculate regularly, then put 1/

Fractional exponents?

Better than naive way


"""

# n must be non-neg here
# x must also be positive
# Gets log, floored
def quickLog(n, base = 2):
	assert n >= 0
	assert base > 0

	logValue = 0
	comparer = 1

	while (n >= comparer):
		comparer *= base
		logValue += 1
	
	return logValue - 1

# print(quickLog(82, 3))
# print(quickLog(2))
# print(quickLog(3))
# print(quickLog(5))
# print(quickLog(22))

def pow(x, n):

	# 0. if n is negative, flip the bit and record
	isNegativeExponent = n < 0
	if (isNegativeExponent):
		n *= -1

  # 1. figure out states we need to calculate
	numSubproblems = quickLog(n)

	# 2. calculate subproblems
	subproblems = [None for _ in range(numSubproblems + 2)]
	subproblems[0] = 1

	if (len(subproblems) > 1):
		subproblems[1] = x

	for i in range(2, len(subproblems)):
		subproblems[i] = subproblems[i-1] * subproblems[i-1]
	
	# 3. merge using binary rep of n as which subproblems to multiply with
	total = 1
	power = 1 # start at first power, since that corresponds to the 1's digit

	while (n > 0):
		shouldMultiplySubproblem = n % 2 # use modulo, bitwise or doesn't work well
		if (shouldMultiplySubproblem):
			total *= subproblems[power]
		power += 1
		n = n >> 1 # will eventually terminate
	
	return total if not isNegativeExponent else 1/total

# x = 7
# x = x >> 2
# print(x)
# print('hello')
# print(7 % 2)
# pow(3, 20)

def validate(x, n, expected):
	result = pow(x, n)
	if (result != expected):
		print("Test failed:")
		print(x)
		print(n)
		print("Result: " + str(result))
		print("Expected: " + str(expected))

validate(1, 1, 1)
validate(1, 100, 1)
validate(2, 2, 4)
validate(2, 3, 8)
validate(5, 3, 125)
validate(10, 5, 100000)

for i in range(-5, 20):
	for j in range(-5, 20):
		if (i == 0 and j < 1): continue
		validate(i, j, pow(i, j))

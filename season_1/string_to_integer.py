# Results:
# Runtime: 51ms 56.71%
# Memory Usage: 14.1MB 30.01%

# string to 32 bit signed integer
# 1. Read in and ignore any whitespace
# 2. next char - or +, if not end of string. Read in if either, determines if pos or neg.
# 3. read in chars until next non-digit read or EOF
# 4. convert digits to integer
# 5. clamp
# 6. return result

# ' ' is a whitespace
# Idea: keep pointer to string. When reading chars, mult by 10 and add. 

def isDigit(c):
	return '0' <= c and c <= '9'

def charToInt(c):
	return int(c)

class OutOfBounds(Exception):
	pass

def myAtoi(s):

	i = 0
	sum = 0
	sign = 1

	def inc():
		nonlocal i
		i += 1
		if (len(s) <= i):
			raise OutOfBounds()

	if (len(s) == 0):
		return 0

	try:
		# ignore leading whitespace
		while (s[i] == ' '): inc()

		# check if next is + or - and read in
		if (s[i] == '-'):
			inc()
			sign = -1
		elif (s[i] == '+'):
			inc()
		
		# read in chars until next non-digit read or EOF
		# convert digits to integer
		while (isDigit(s[i])):
			sum *= 10
			sum += int(s[i])
			inc()

	except OutOfBounds:
		pass

	sum *= sign

	# clamp
	if (sum < -2**31):
		return -2**31
	elif (sum > 2**31 - 1):
		return 2**31 - 1
	else:
		return sum


def validate(s, expected):
	if (myAtoi(s) != expected):
		print("Expected: " + str(expected))
		print("Result: " + str(myAtoi(s)))

validate("4", 4)
validate("0", 0)
validate("-5", -5)
validate("1540", 1540)
validate("    1 540", 1)
validate("    -1 540", -1)
validate("    -15x40", -15)
validate("    -15", -15)
validate("    +15 ", 15)
validate("    -15", -15)
validate("-2147483648", -2147483648)
validate("-2147483649", -2147483648)
validate("3147483649", 2147483647)



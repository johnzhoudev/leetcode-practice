# Results:
# Runtime: 77ms 70.68%
# Memory Usage: 14.2MB 28.26%

# Take string and row len
# write in zigzag pattern: down, rightup, down...
# then return as if read from left to right

# What happens if row len > string len? - returns string as regular.
# no spaces in s
# 1 <= numRows <= 1000

# Idea 1: Make huge numRows x ?? 2d array, and fill in going down and up / right.
# Wasted space: 
# Parsing may take longer

# Idea 2: Can we do a linked list?
# - Adding to linked list 1, 2, 3, 2, 1, 2, 3 and so on
# So just make numRows linked lists, and add!
# O(n) runtime since each char added O(1) and read off once, no random whitespace

def convert(s, numRows):
	# create linked lists
	rows = [[] for _ in range(numRows)]

	# Add to rows
	currentRow = 0
	direction = 1
	for c in s:
		rows[currentRow] += c

		# If next step is out of bounds, reverse direction
		if (currentRow + direction < 0 or currentRow + direction >= numRows):
			direction = -direction

		currentRow += direction
	
	# Read off the word
	resultStr = ""
	for row in rows:
		for c in row:
			resultStr += c

	return resultStr

def validate(s, numRows, expected):
	if (convert(s, numRows) != expected):
		print("Expected: " + expected)
		print("Result: " + convert(s, numRows))

validate("PAYPALISHIRING", 4, "PINALSIGYAHRPI")
validate("A", 1, "A")
validate("ABCDEF", 2, "ACEBDF")
# Given n pairs of brackets, generate all combos in array string

# Ideas:
# 1. DP: Easy way to reuse solutions, ( + inner + ) + rest, inner + rest = 8. unique too.
# state[i] = all brackets with i pairs -> How long to solve for each? O(n^2) to iterate thru inner and rest combos * n  times * size of solns O(2^n)
# state[0] = ['']
# O(n^3 * 2^n) time, space O(n * 2^n)
# Pretty good, already using solutions

# Other ideas:

def generateParenthesis(n: int):

	state = [[] for _ in range(n + 1)]

	# base case
	state[0] = [""]

	# dp step
	for i in range(1, n + 1):
		for inner in range(0, i): # all possible values for inner
			rest = i - inner - 1
			innerBrackets = state[inner]
			restBrackets = state[rest]

			state[i].extend(["(" + inside + ")" + outside for inside in innerBrackets for outside in restBrackets])

	return state[n]

# Search Algorithm theory
# Basically, print the brackets from left to right
# Have to start with left opening bracket (
# then could close bracket if num open is > 0 using )
# or add another ( if not over

"""
eg. n = 3
()()()
(())()
()(())
((()))
Covers all possibilities
"""
def generateParenthesis2(n):
	numBrackets = 0
	numOpen = 0

	states = [(0, 0, "")]
	solutions = []

	while (len(states) != 0):
		(numBrackets, numOpen, string) = states.pop()

		if (numBrackets == n and numOpen == 0):
			solutions.append(string)
			continue

		if (numBrackets < n):
			states.append((numBrackets + 1, numOpen + 1, string + "("))

		if (numOpen > 0):
			states.append((numBrackets, numOpen - 1, string + ")"))
	
	return solutions

for i in range(8):
	# print(generateParenthesis(i))
	# print(generateParenthesis2(i))

	arr1 = generateParenthesis(i)
	arr2 = generateParenthesis2(i)
	if (set(arr1) != set(arr2)):
		# print(arr1)
		print("Not equal " + str(i))
		# print(arr2)







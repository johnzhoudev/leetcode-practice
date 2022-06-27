# Results:
# Runtime: 70ms 84.80%
# Memory Usage: ms,MB of

# Given string s
# Find longest substring no repeating characters
# s = "abcabcbb", out = abc
# Substring = must be continuous

# Notes:
# no repeating characters
# If null string, return 0
# What happens if multiple same length longest? -> return 1st occurrence? -> output length

# Ideas: Brute force: try all possible substrings -> O(n^2) * O(n)
# Idea 2: DP: 
# d[i, j] = longest substr start i ending at position j with unique stuff, hashmap of repeated chars
# - hashmaps are constant size since const number of ascii symbols
# d[i, j+1] = if you can add s[j] to d[i, j]. else None
# d[i, 0] = 1, { s[i] } base case
# as you go just keep track of max
# O(n^2)

# Idea 3: Rolling interval: Start at front and start adding to hashmap, if cannot add, delete last letters.
# 2 pointers, to start and end
# if can add next, increment end and add to set. Else remove start char from set and increment.
# track largest num.
# O(n) time, every char gets added and deleted at most 2x
# eliminates

def longestSubstr(s):
	if (len(s) == 0):
		return 0

	start = end = 0 # exclusive end
	longest = 0
	charSet = set()

	while (end < len(s)):
		# try and add s[end + 1]
		c = s[end]

		while c in charSet:
			# remove last from set
			charSet.remove(s[start])
			start += 1

		end += 1 # add first since newlength includes end added
		charSet.add(c)
		if (end - start > longest):
			longest = end - start

	return longest

def validate(s, expected):
	if (longestSubstr(s) != expected):
		print("Expected: " + str(expected))
		print("Result: " + str(longestSubstr(s)))

validate("abcabcbb", 3)
validate("bbbbb", 1)
validate("pwwkew", 3)
validate("asdf", 4)
validate("aasdf", 4)
validate("", 0)
validate("asdffjkl;1234567890", 15)
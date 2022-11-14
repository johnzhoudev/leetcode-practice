# Results:
# Runtime: 585ms 78.67%
# Memory Usage: 26MB 68.15%

"""
- array nums
- return true if a value appears at least twice in array
- false if every elt is distinct

Ideas:
- use a set, check if elements exist or not
O(n) time, O(n) space

Do in O(1) space? Impossible, have to remember if an elt is in the array
"""

def containsDuplicate(nums):
	numSet = set()
	for num in nums:
		if num in numSet:
			return True
		numSet.add(num)
	return False
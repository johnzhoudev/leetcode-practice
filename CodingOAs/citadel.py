"""
Array of n integers point
integer k
can increment point[i] by k, or decrement. We perform either of the operations once for each point

Perform an operation on each point[i] where diff b/w max and min values in array after all ops is minimal

must perform an operation

Ideas:

Brute Force:
- compute all possibilities - 2^n possible
	- for each possibility, O(n) time, can compute and keep track.

Only want min and max - so can sort array
- Actually, min will always be bounded by min value in the array, and max. So really just increment min, and decrement max.
- that's best you can do. 
- O(n) time to get min and max

- Any other numbers, what if they go out of bounds? k could be any size...
- Doesn't work, in case they get incremented past size.

- always adding or subtracting k - so we can process min and max on all numbers, given we add / sub k.
- each num will have a max and min value

A solution:
- get min and max for each value
- need to pick closest together

Start with all hi - flip down largest

Sort, then subtract all from lowest, then start flipping up. and go and calculate min each time
O(n log n)

O(n) solution???

"""

def solve(point, k):
	return False

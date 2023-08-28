"""

non-neg x
return sqrt x roudned to nearest int, non neg
no built in exponent func

Idea:
- no way to ballpark
- binary search? based on high or low
- O(x) time, O(1) space
- can we narrow in faster?
- we could also use gradient descent...???
- looking for integer with square strictly less or equal to

Tactic: Binary Search, Bias right to not hit infinite loop.
"""

def solve(x):
    # just do binary search, both inclusive
    left = 0
    right = x
    while left <= right:
        # if one number left, return
        if right - left + 1 == 1:
            return left # same number

        # pivot = (right + left) // 2 # bias left
        pivot = (right + left + 1) // 2 # bias right so we can eliminate the right ones
        if pivot * pivot > x: # must pivot left
            right = pivot - 1
        elif pivot * pivot < x:
            left = pivot # maintain pivot, still valid
        else:
            return pivot



"""

163. Missing Ranges

sorted number
also a range
number is missing if x is in range and x not in nums

return shortest sorted list of ranges exactly covering all missing numbers

Idea:
- sliding window? iter thru nums, and add the range inbetween
prev

Tactic:
Tricky! prev = lower - 1 and append upper + 1, then if range, append (prev + 1, num - 1). Hard to handle lower / upper edge cases

"""

def solve(nums, lower, upper):
    prev = lower - 1 # minus 1 here so we append prev + 1

    output = []
    nums.append(upper + 1) # final upper bound

    for num in nums:
        if num - prev > 1: # more than 1 inc
            output.append((prev + 1, num - 1))
        prev = num

    return output



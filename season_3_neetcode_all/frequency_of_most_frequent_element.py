"""

https://leetcode.com/problems/frequency-of-the-most-frequent-element/

one operation - pick index of nums and increment element by 1
can perform k operations
return maximum possible frequency of element after k operations
- can increment the same number multiple times

Ideas:
- optimal solution is one of
    - pick a number, and try and increment as many numbers as you can to get to that number

Brute force
- O(n^2)
- sort list
- for every number, of smaller numbers, how many can you increment to get to right value - check O(n) other values

can maybe do the second pass in O(n) time, after sorting. rolling window
- while you have budget, add until no more.
- then to move on to next number, add difference between prev and next number * num numbers to budget (shaving off) 
- continue until the end

O(n log n) (sort required) with smart rolling window

Do we need the sort? Hash table, count number of values - but then don't know what values are around it...

yolo O(n log n), hard to do without sort

Trick: keep track of sum and curr * num in range, if larger than k, can't fit

"""

# fixed sliding window (grow only)
# idea is since you're looking for max size, keep window size and shift if invalid instead of shrink

def solve(nums, k):
    nums.sort()

    # 

# Shrinkable sliding window
# standard, open while valid, shrink while invalid 
def solve(nums, k):
    nums.sort()

    # Sliding window, slide left
    right = len(nums) - 1
    left = right # inclusive
    maxFreq = 1
    budget = k

    while right >= 0:

        # expand
        while left - 1 >= 0 and budget - (nums[right] - nums[left - 1]) >= 0:
            budget -= (nums[right] - nums[left - 1])
            left -= 1
        
        maxFreq = max(maxFreq, right - left + 1)

        # shrink and retry
        # reset
        if right - 1 < left:
            right -= 1
            left = right
            budget = k
        else: # correct
            diff = nums[right] - nums[right - 1]
            right -= 1
            budget += diff * (right - left + 1)
    
    return maxFreq


def solve(nums, k):
    # sort list
    nums.sort()

    # go thru from back and keep budget
    bestFrequency = 1

    currIdx = len(nums) - 1
    budget = k
    nextEltIdx = currIdx - 1
    freq = 1

    while nextEltIdx >= 0 and currIdx >= 0: # haven't added next yet
        curr = nums[currIdx]

        while nextEltIdx >= 0:
            # potentially add next elt idx to budget
            if budget - (curr - nums[nextEltIdx]) < 0: # if can't fit in budget
                break

            budget -= (curr - nums[nextEltIdx])
            freq += 1
            nextEltIdx -= 1

        bestFrequency = max(bestFrequency, freq)

        # now want to decrement currIdx
        currIdx -= 1 # try next
        freq -= 1 # removing last one
        budget += (curr - nums[currIdx]) * freq # budget correction

        # reset nextEltIdx and budget if past
        if currIdx <= nextEltIdx:
            nextEltIdx = currIdx - 1
            budget = k
            freq = 1
    
    return bestFrequency


print(solve([1000], 5))
"""

1004. Max Consecutive Ones III

can flip at most k 0's

max number of consecutive 1's in an array?


Idea:
sliding window / queue
- parse consecutive 1's 
- put onto queue with num 0's to pop if off
- when spaces of 0's, sum up
- next group of 1's, if k is non zero, keep going
    - else pop queue and add k's 

keep rolling sum of number of 1's
return

O(n) time
O(1) space

What if just used 2 pointers
- expand when you can
- pop when you have to

Tactic:
Sliding window: use for loop on right! and while num zeroes > k, remove left. 

"""

def solve(nums, k):
    zeroes = 0
    left = 0
    result = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        result = max(result, right - left + 1)
    return result
        

def solve(nums, k):

    num0 = 0 # num 0's
    left = 0
    # expand out, once range is large, keep that large.
    for right in range(len(nums)):
        num0 += 1 - nums[right]

        if num0 > k:
            num0 -= 1 - nums[left]
            left += 1
    return len(nums) - 1 - left



# cleaner sliding window, use exclusive right
def solve(nums, k):

    left = 0
    right = 0 # exclusive
    counts = {
        0: 0,
        1: 0
    }

    best = 0

    while right <= len(nums):

        if counts[0] > k:
            # advance left
            counts[nums[left]] -= 1
            left += 1
        else:
            # advance right
            if right < len(nums):
                counts[nums[right]] += 1
            right += 1
        
        if counts[0] <= k:
            best = max(best, counts[0] + counts[1])
    
    return best

        
def solve(nums, k):
    counts = {
        0: 1 - nums[0],
        1: nums[0]
    }

    best = 1 if k > 0 else nums[0]

    left = 0
    right = 0 # inclusive

    while right < len(nums):

        if counts[0] > k:
            # must advance left
            counts[nums[left]] -= 1
            left += 1

            if left >= len(nums): break

            if right < left:
                right = left # move right too
                counts[nums[right]] += 1
            continue
        
        # still okay, so expand right
        right += 1
        if right >= len(nums): break
        counts[nums[right]] += 1

        if counts[0] <= k:
            best = max(best, counts[1] + counts[0]) # flipped 0's good too
    
    return best


            






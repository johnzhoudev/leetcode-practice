"""

300. Longest Increasing Subsequence

Idea:
- dp[i] = longest subsequence length ending in i
- go thru previous, and take max
O(n^2)

Idea 2:

- list of lengths, binary search to insert
- list of lengths must be in increasing order of ending note
    - if larger list end is smaller, must be better
- When adding a number, will never corrupt list

"""

def solve2(nums):
    dp = [1 for _ in range(len(nums))] # length of longest sequence ending in that number

    for idx, num in enumerate(nums):
        best = 1
        for idx2, length in enumerate(dp[:idx]):
            if nums[idx2] < num:
                best = max(best, length + 1)
        dp[idx] = best
    
    return max(dp)





def solve(nums):
    lengths = [float('-inf')] # Len 0 is -infinity, anything greater
    # endings of subsequences

    def update_length(num):
        left = 0
        right = len(lengths) - 1

        while left < right: # should reduce to one
            pivot = left + (right - left + 1) // 2 # Bias right
            ending = lengths[pivot] 
            if ending < num: # go right
                left = pivot
            else: # go left
                right = pivot - 1
        
        # edge cases: if num is smaller than all, have to be longer than -inf 0 length
        # if number is bigger than all, will be on last one
        assert left == right
        if left + 1 == len(lengths):
            lengths.append(num)
        else:
            lengths[left + 1] = min(lengths[left + 1], num)

    for num in nums:
        update_length(num)
    
    return len(lengths) - 1

        




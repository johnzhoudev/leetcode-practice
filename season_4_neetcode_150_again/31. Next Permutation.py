"""

31. Next Permutation

next lexicographically larger permutation
- must be in place and use constant memory
- basically how can you

Lexicographically larger: x > y if, at the first position x differs from y, xi > yi
- permutations though...

[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]


1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321

- move larger number forwards, everything afterwards sorted
- when section from back is all decreasing, smallest larger number forwards and sort back
- reverse back section, swap and reverse

- count from back, make sure all decreasing.
- swap smallest larger number forwards
- reverse back

O(k) time
O(1) space

123

321

Tactic:
Find first thing not increasing from right, swap that with smallest value on right larger than swap, and reverse right side.
"""

def solve(nums):
    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(i, j):
        while i < j:
            swap(i, j)
            i += 1
            j -= 1

    # go from back and figure out which leftmost elt to swap (suddenly decreasing)
    currIdx = len(nums) - 1
    while (currIdx - 1 >= 0 and nums[currIdx - 1] >= nums[currIdx]):
        currIdx -= 1
    
    if currIdx == 0: # all decreasing, just reverse all
        reverse(0, len(nums) - 1)
        return

    swapIdx = currIdx - 1

    # do one more pass to find item to swap with
    for i in range(len(nums)-1, currIdx-1, -1): # go backwards, first one that's larger, that's the swap
        if nums[i] > nums[swapIdx]:
            swap(i, swapIdx)
            break
    
    # Done swap, now we need to just reverse the end portion
    reverse(currIdx, len(nums) - 1)


# print out all permutations so we can see
def allPermutations(n):
    def dfs(s):
        if len(s) == n:
            print(s)
        else:
            for i in range(1, n + 1):
                if str(i) in s: continue
                dfs(s + str(i))
    dfs("")

allPermutations(4)

x = [] 
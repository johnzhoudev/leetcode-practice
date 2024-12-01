"""

31. Next Permutation

- kind of like sorting lexicographically

1 2 3 4
1 2 4 3

1 3 2 4
1 3 4 2

1 4 2 3
1 4 3 2

2 1 3 4
2 1 4 3 

2 3 1 4
2 3 4 1

2 4 1 3
2 4 3 1 

3 1 2 4
...

4 3 2 1
- nothing larger, so just reverse

- each time, want to swap a smaller number on left with bigger number on right
    - so find rightmost smaller number that can be swapped with smallest biggest number to right?
    - swap forward, swap with smallest number larger than it
    - then just reverse order of end

Tactic:
First thing not increasing from right = swap idx. Then find smallest thing larger than it on the right. And reverse after.
Or, forward pass look at pairs.


"""

def solve(nums):

    idxToSwap = -1
    toSwapTo = -1

    for i in range(0, len(nums) - 1):
        # increasing order, could swap
        if nums[i] < nums[i+1]:
            idxToSwap = i
            toSwapTo = i + 1
        
        # also want to check which element is the biggest one smaller
        if idxToSwap != -1 and nums[idxToSwap] < nums[i+1]:
            toSwapTo = i + 1
    
    # now perform swap and reverse rest - back should be in increasing order
    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def reverse(i):
        end = len(nums) - 1
        start = i

        while start < end:
            swap(start, end)
            start += 1
            end -= 1
    
    if idxToSwap != -1:
        swap(idxToSwap, toSwapTo)
        reverse(idxToSwap + 1) # everything after
    else:
        reverse(0)
    
    return nums

print(solve([1, 2, 3]))







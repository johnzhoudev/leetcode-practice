"""

https://leetcode.com/problems/find-the-duplicate-number/

- exactly one repeated number
- const extra space
- cannot modify array
- numbers 1 to n

Idea:
- treat as linked list, advance to different numbers
- repeated number is start of cycle

- for each num, run fast and see if it hits number again n+1 steps
- O(n^2) time, eh - have to be able to do better. else just do a pass for each possible val

Idea2: 
- sum, missing is val

Idea 3: Complicated math



"""

def solve(nums):
    curr = len(nums) # index of current value
    for _ in range(len(nums) - 1):
        curr = nums[curr - 1]
    
    # advance until hit curr again, to get loop
    loopSize = 1
    oldCurr = curr
    curr = nums[curr-1]
    while curr != oldCurr:
        curr = nums[curr-1]
        loopSize += 1
    
    # then 2 ptrs, follow
    fast = len(nums)
    for _ in range(loopSize):
        fast = nums[fast - 1]
    prevSlow = None
    slow = len(nums)
    while fast != slow:
        prevSlow = slow
        slow = nums[slow - 1]
        fast = nums[fast - 1]
    
    return nums[prevSlow - 1] 




def solve(nums):
    x = sum(nums)
    return x - int((len(nums)) * ((len(nums) - 1) / 2))

# TODO: Finish this

def solve(nums):

    start = 1
    for _ in range(len(nums)):
        start = nums[start - 1] # first iter, 0 points to this num
        fast = nums[start - 1]
        for _ in range(len(nums) - 1):
            if fast == start:
                return fast
            fast = nums[fast - 1]
    
    raise RuntimeError()


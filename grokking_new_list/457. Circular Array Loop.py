"""

457. Circular Array Loop
https://leetcode.com/problems/circular-array-loop/description/

- find if there exists a loop
- don't count cycle of size 1

just follow in order and maintain seen array
- if cycle of size 1, doesn't count.
- Must have a loop, so just check if all ends are cycles of size 1

- For each start, maintain set of visited 
- if seen something, loop exists
- if not, add visit to already seen

Tactic: Tortise and hare?

"""

# If visited, zero out in nums
def solve(nums):
    n = len(nums)

    for i in range(len(nums)):
        slow = i
        fast = i
        isForward = nums[i] > 0

        def advance(i, isForward, erase=False): # ret -1 if loop ends
            if i == -1: return -1

            # Check direction
            if isForward and nums[i] < 0: return -1
            if not isForward and nums[i] > 0: return -1


            prev = i
            next = (i + nums[i]) % n

            # Potentially erase curr
            if erase:
                nums[prev] = 0

            if next == prev:
                return -1

            return next

        while True:
            slow = advance(slow, isForward)
            fast = advance(advance(fast, isForward), isForward)
            if fast == -1: break # loop ended or direction failed

            if slow == fast: # loop!
                return True
        
        # If loop ended, zero out
        curr = i
        isForward = nums[i] > 0
        while curr != -1:
            curr = advance(curr, isForward, erase=True)

    return False



def solve(nums):
    n = len(nums)

    visited = set()

    for i in range(len(nums)):

        if i in visited:
            continue

        seen = set()

        curr = i
        lastSeen = -1
        isForward = nums[curr] > 0

        # explore until either seen or reached start
        while curr not in visited and curr != lastSeen:

            if curr in seen: # A loop!
                return True

            seen.add(lastSeen)
            lastSeen = curr
            curr = (curr + nums[curr]) % n # takes sign of divisor

            if isForward and nums[curr] < 0: break
            if not isForward and nums[curr] > 0: break
        
        # At end, add all seen
        for node in seen:
            visited.add(node)
    
    return False
        
    

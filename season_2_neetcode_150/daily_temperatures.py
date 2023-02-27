# Results:
# Runtime: 1451ms 52.41%
# Memory Usage: 27.8MB 96.32%

"""

https://leetcode.com/problems/daily-temperatures/

num days to wait for a warmer temperature

Ideas:

brute force O(n^2) look ahead

monotonic decreasing stack
- but thing is, every elt only gets pushed and popped once on there. so overall runtime O(n)
space: O(n) worst case

Tactic: Monotonic decreasing stack, iterate from back. if encounter something larger, smaller stuff in stack can be popped

"""

def solve(temps):
    # setup state
    result = [0 for _ in range(len(temps))]
    highestTemp = [] # start from back, last is highest temp
    # monotonically decreasing.

    for i in range(len(temps) - 1, -1, -1):
        temp = temps[i]

        # find higher temp
        # pop from highest temp until temp higher
        while highestTemp:
            otherTemp, idx = highestTemp.pop()

            if otherTemp > temp:
                highestTemp.append((otherTemp, idx))
                # add result
                result[i] = idx - i # num days to wait
                break
        
        # if not found
        # if len(highestTemp) == 0:
        #     result[i] = 0
        
        # add current
        highestTemp.append((temp, i))
    
    return result


            







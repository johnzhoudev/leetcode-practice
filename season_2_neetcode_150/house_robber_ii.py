"""

https://leetcode.com/problems/house-robber-ii/


- same as house robber except houses are in a circle, so last house neighbour of first house

h h h r
r h h r

XXXXXXX - this is not correct.
- first and last house both robbed, x
    - how to deal with this?
    - can just remove one. right. consider optimal, has all these cases. 
- only 1 is robbed, okay.
- both not robbed, also okay.

- As we build, prefer answers that don't use first

- so solve, but include if first and last house robbed. then adjust.

si = si-3 + hi, si-2 + hi, si-1

Tactic: do regular solve on nums[1:] and nums[:-1], and return max. Asymptotically, fine.

"""

def solve(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    elif len(nums) == 3:
        return max(nums[0], nums[1], nums[2]) # no wrap around

    # guaranteed at least 3 nums 
    def robOG(nums):
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        s0 = nums[0]
        s1 = nums[1]
        s2 = nums[0] + nums[2]

        for x in range(3, len(nums)):
            tmp = max(s2, s1 + nums[x], s0 + nums[x])
            s0 = s1
            s1 = s2
            s2 = tmp
        
        return s2
    
    return max(robOG(nums[1:]), robOG(nums[:-1]))


# bad solve. Not correct.
def solve(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    elif len(nums) == 3:
        return max(nums[0], nums[1], nums[2]) # no wrap around
    
    states = [
        (nums[0], True),
        (nums[1], False),
        (nums[0] + nums[2], True)
    ]

    for x in range(3, len(nums)):
        tmp = (0, True)
        for i in range(len(states)):
            if (i == 0 or i == 1):
                if states[i][0] + nums[x] > tmp[0]:
                    tmp = (states[i][0] + nums[x], states[i][1])
                elif states[i][0] + nums[x] == tmp[0] and tmp[1] == True:
                    tmp = (states[i][0] + nums[x], states[i][1]) # switch even if equal

            elif i == 2:
                if states[i][0] > tmp[0]:
                    tmp = (states[i][0], states[i][1])
                elif states[i][0] == tmp[0] and tmp[1] == True:
                    tmp = (states[i][0], states[i][1])
        states[0] = states[1]
        states[1] = states[2]
        states[2] = tmp
    
    # last didn't use last num, so okay
    if states[2] == states[1]:
        return states[2][0]
    elif states[2][1] == False: # doesn't include first, so okay to return
        return states[2][0]
    else:
        return states[2][0] - min(nums[0], nums[-1])




    

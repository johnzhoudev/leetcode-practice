"""

https://leetcode.com/problems/house-robber/

- cannot rob adjacent houses
- max money without alerting the police?

if considering to rob house, must be robbed 1 between or 2 inbetween. if 3, then rob middle too.
r h h h h
r h h r
h h h r

Idea:
- search alg / dp
- s[i] = max money if robbing houses up to and including i
- either rob the house and the 1st or 2nd house, or rob the 3rd house and skip the 4th.
- s[i] = max(s[i-2] + h[i], s[i-3] + h[i], s[i-1])

Tactic: s[i] = max money if robbing houses up to and including i, s[i] = max(s[i-2] + h[i], s[i-3] + h[i], s[i-1]). - either rob the house and the 1st or 2nd house, or rob the 3rd house and skip the 4th.
"""

def solve(nums):
    if len(nums) <= 3:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return max(nums[0] + nums[2], nums[1])
    
    s0 = nums[0]
    s1 = nums[1]
    s2 = nums[0] + nums[2]

    for x in range(3, len(nums)):
        tmp = max(s0 + nums[x], s1 + nums[x], s2)
        s0 = s1
        s1 = s2
        s2 = tmp
    
    return s2



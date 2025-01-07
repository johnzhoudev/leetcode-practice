"""

136. Single Number


each elt appears twice except for 1

linear runtime
const extra space

Tactic:
bitwise xor!

"""

def solve(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor

print(solve([2, 2, 1]))
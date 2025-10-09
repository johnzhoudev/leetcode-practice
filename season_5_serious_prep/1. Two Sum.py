"""

1. Two Sum

keep dict of values needed

"""

def solve(nums, target):
    state = {}
    for idx, num in enumerate(nums):
        if num in state:
            return idx, state[num]
        state[target-num] = idx
    raise RuntimeError("Terrible")
    

    
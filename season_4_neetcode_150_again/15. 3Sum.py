"""

15. 3Sum

3 nums not same sum to target

Ideas:
- target - num => reduce to 2sum, 2 pointers method close in
O(n^2)
- or use hash hap

"""

def solve(nums):
    # build hashmap
    hmap = {}

    # no rpts, i < j
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            key = 0-nums[i]-nums[j]
            if key not in hmap: hmap[key] = []
            hmap[key].append((i, j))
    
    output = set()

    for i in range(len(nums)):
        key = nums[i]
        if key not in hmap: continue
        for i2, i3 in hmap[key]:
            if i < i2:
                k1, k2, k3 = sorted([key, nums[i2], nums[i3]])
                output.add((k1, k2, k3))
    
    return list(output)
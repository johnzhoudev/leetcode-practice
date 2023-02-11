"""

https://leetcode.com/problems/3sum/

return all triplets, values summing to x
soln set cannot contain duplicate triplet values. 

Idea: O(n^2), take hashes like 2sum, then go one more time

"""

def solve(nums, target):
    # state
    hashMap = {}

    for idx1, num in enumerate(nums):
        for idx2 in range(idx1 + 1, len(nums)):
            # if idx1 == idx2: continue
            num2 = nums[idx2]
            if target - num - num2 not in hashMap:
                hashMap[target - num - num2] = [(num, num2)]
            else:
                hashMap[target - num - num2] += [(num, num2)]
    
    # For uniqueness, have 3 sets for sorted num combos. check if in

    s1 = set()
    s2 = set()
    s3 = set()

    def isSoln(n1, n2, n3):
        nonlocal s1
        nonlocal s2
        nonlocal s3
        return n1 not in s1 and n2 not in s2 and n3 not in s3


    # now do one more pass
    solns = []
    for num in nums:
        if num in hashMap:
            for num1, num2 in hashMap[num]:

                [n1, n2, n3] = sorted([num, num1, num2])

                if not isSoln(n1, n2, n3):
                    continue

                solns.append((n1, n2, n3))
                s1.add(n1)
                s2.add(n2)
                s3.add(n3)

    return solns




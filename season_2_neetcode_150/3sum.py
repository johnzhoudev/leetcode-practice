"""

https://leetcode.com/problems/3sum/

return all triplets, values summing to x
soln set cannot contain duplicate triplet values. 

Idea: O(n^2), take hashes like 2sum, then go one more time
- For last loop, maintain a set of tuples and check if in.
- O(log soln size)

Idea2: What if we sorted nums?
- -10, -4, -2, 0, 2, 4, 6, 12

- take every 2 combos, and see if target is in nums and not same - can use set
    - O(n^2) as well

- Can consider less combos with a sliding window
    - put all into set with idx
    - from left and right, check, and see if neg or pos. see if 

Idea 3:
x + y + z = w => x + y = w - z
- for each num, solve 2sum for w-z
- can sort first and do 2 pointers, or build hashmap
- duplicate triplet values? pivot is always the smallest value
    - use a set

Tactic: Rearrange equation, turn into 2sum. Also sorting helps, don't need hash table. Uniqueness, make 1st elt and left not dup
"""

def solve3(nums, target):
    nums.sort()
    # results = set()
    results = []
    for idx, num in enumerate(nums):
        # Skip duplicate first element
        if idx > 0 and num == nums[idx - 1]:
            continue

        passTarget = target - num

        left = idx + 1
        right = len(nums) - 1

        while left < right:

            # if ((left > idx + 1) and (nums[left - 1] == nums[left])):
            #     left += 1
            #     continue
            # if ((right < len(nums) - 1) and (nums[right + 1] == nums[right])):
            #     right -= 1
            #     continue

            sum = nums[left] + nums[right]
            if (sum == passTarget):
                # results.add((num, nums[left], nums[right]))
                results += [(num, nums[left], nums[right])]
                left += 1
                right -= 1

                # since we already make sure first number isn't duplicated, all we need to do is make sure
                # during the sweep that at least one of the numbers isn't duplicated. Not both. and only care
                # when we're adding
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

            elif (sum < passTarget):
                left += 1
            elif (sum > passTarget):
                right -= 1
    
    # print(results)
    # return list(results)
    return results









# def solve2(nums, target):
#     hashmap = {}
#     for idx, num in nums:
#         if num in hashmap:
#             hashmap[num] += [idx]
#         else:
#             hashmap[num] = [idx]

#     for idx1 in range(len(nums)):
#         for idx2 in range(idx1 + 1, len(nums)):
#             num1 = nums[idx1]
#             num2 = nums[idx2]

#             if target - num1 - num2 in hashmap:
#                 for idx3 in hashmap[target - num1 - num2]:
#                     if idx3 != idx1 and idx3 != idx2:
#                         # now have a valid soln, but make sure not duplicated




# Time limit exceeded
def solve(nums, target):
    # state
    hashMap = {}

    for idx1 in range(len(nums)):
        for idx2 in range(idx1 + 1, len(nums)):
            # if idx1 == idx2: continue
            num1 = nums[idx1]
            num2 = nums[idx2]
            if target - num1 - num2 not in hashMap:
                hashMap[target - num1 - num2] = [(idx1, idx2)]
            else:
                hashMap[target - num1 - num2] += [(idx1, idx2)]
    
    # For uniqueness, have 3 sets for sorted num combos. check if in

    solns = set()

    # now do one more pass
    for idx3, num3 in enumerate(nums):
        if num3 in hashMap:
            for idx1, idx2 in hashMap[num3]:

                if idx3 == idx1 or idx3 == idx2:
                    continue

                num1 = nums[idx1]
                num2 = nums[idx2]
                [n1, n2, n3] = sorted([num3, num1, num2])

                if (n1, n2, n3) in solns:
                    continue

                solns.add((n1, n2, n3))

    return solns




"""

78. Subsets

return all possible subsets, no duplicates
all numbers are unique

Take all sets, either add or don't add number. 

Tactic:
Build off previous subsets

"""

def solve(nums):
    subsets = [[]]

    for num in nums:
        newSubsets = []
        for subset in subsets:
            newSubsets.append(subset + [num])
        subsets.extend(newSubsets)
    
    return subsets
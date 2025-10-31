"""

18. 4Sum

return all numbers that sum to target, nums must be distinct


2 sum trick is with a hash map, O(n)
3 sum , O(n^2) to reduce proble
So 4 sum, O(n^3)? reduce to 3 sum?

This is pretty slow. How to cut down?

"""

def solve2(nums, target):
    output = set() # Deduplicate

    def sum2(start_i, nums, target, elts): # nums[i:] valid
        seen = set() # set of other elts encountered
        for i in range(start_i, len(nums)):
            if target - nums[i] in seen:
                output.add(tuple(sorted(elts + [nums[i], target - nums[i]]))) # Dedupe by sorting and tuple
            seen.add(nums[i])
    
    def sumn(start_i, nums, target, elts, n):
        seen = set()
        
        for i in range(start_i, len(nums)):

            if nums[i] in seen:
                continue # Skip duplicates
            # Remove nums[i]
            if n == 3:
                sum2(i+1, nums, target - nums[i], elts + [nums[i]])
            else:
                sumn(i+1, nums, target - nums[i], elts + [nums[i]], n-1)
            seen.add(nums[i])
    
    sumn(0, nums, target, [], 4)
    return list(output)


def solve(nums, target):
    output = set() # Deduplicate

    def sum2(start_i, nums, target, elts): # nums[i:] valid
        seen = set() # set of other elts encountered
        for i in range(start_i, len(nums)):
            if target - nums[i] in seen:
                output.add(tuple(sorted(elts + [nums[i], target - nums[i]]))) # Dedupe by sorting and tuple
            seen.add(nums[i])
    
    def sum3(start_i, nums, target, elts):
        seen = set()
        
        for i in range(start_i, len(nums)):

            if nums[i] in seen:
                continue # Skip duplicates
            # Remove nums[i]
            sum2(i+1, nums, target - nums[i], elts + [nums[i]])
            seen.add(nums[i])
    
    def sum4(start_i, nums, target, elts):
        seen = set()

        for i in range(start_i, len(nums)):
            # Remove nums[i]
            if nums[i] in seen:
                continue # Skip duplicates
            sum3(i+1, nums, target - nums[i], elts + [nums[i]])
            seen.add(nums[i])
    
    sum4(0, nums, target, [])
    return list(output)

    



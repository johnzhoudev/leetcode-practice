"""

46. Permutations

Just gonna do a search alg

"""

def solve(nums):
    output = []
    num_set = set(nums)

    def search(num_set, curr):
        if len(num_set) == 0:
            output.append(curr[:])
            return
        
        for num in list(num_set):
            num_set.remove(num)
            curr.append(num)
            search(num_set, curr)
            curr.pop()
            num_set.add(num)
    
    search(num_set, [])
    return output

print(solve([1, 2, 3]))
        
        





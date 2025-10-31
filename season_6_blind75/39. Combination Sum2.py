"""

39. Combination Sum

candidates are all positive
need to sum to target

dfs

O(2^n) time, O(n) space

"""

def solve(candidates, real_target):
    output = []

    def dfs(i, target, elements=[]):
        """
        either continue adding candidates[i], or continue
        """
        if i == len(candidates):
            return # Can't add

        if target == 0:
            output.append(elements[:])
            return
        elif target < 0:
            return # Not possible
        
        # Add candidates[i]
        elt = candidates[i]
        elements.append(elt)
        dfs(i, target - elt, elements)
        elements.pop()

        # do search on next
        dfs(i+1, target, elements)
    
    dfs(0, real_target)
    
    return output





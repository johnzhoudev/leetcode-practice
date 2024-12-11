"""

169. Majority Element

return majority element
- appears more than floor(n / 2) times

linear time and O(1) space?

Boyer Moore Majority Vote Alg


Tactic:
Boyer Moore Majority Vote: Take first num as candidate. Count++ when same, -- when diff. If count 0, next num becomes new candidate.

"""

def solve(nums):

    currNum = None
    count = 0

    for num in nums:
        if currNum is None:
            currNum = num
            count = 0

        if num == currNum:
            count += 1
        else:
            count -= 1
        
        # cancelled out, next elt should be better
        if count == 0:
            currNum = None
    
    return currNum
            

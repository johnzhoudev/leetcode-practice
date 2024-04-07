"""

return numbers sorted in lex order

O(n) alg, use O(1) extra space

1 to 9


make tree and do traversal?
Or, build number and increase lexicographically

- start at 1
- first try to move digit left if 0's on left
    - mult by 10 until over. if over, just quit.
- try adding. if over, skip to next tens and divide until not over
- then add in least sig dig until remainder 0
- if remainder 0 after add, divide by 10 until remainder not 0

- try and shift left. if cannot, inc smallest

Works, but damn there's an easier way to think about it

DFS but don't keep state!!!!!

To DFS, first if possible mult by 10
- if not possible, then check if possible to add 1
    - if last digit is 9, then must divide by 10 before adding. Also same if max reached
    - then add 1

Tactic: Right idea, DFS but just use number. Mult by 10 when possible, and before adding 1, check if adding results in a 10 or num == n and divide by 10
"""

def solve(n):
    num = 1
    output = []

    for i in range(n):
        output.append(num)

        if num * 10 <= n:
            num *= 10
        else:
            while num % 10 == 9 or num == n:
                num //= 10
            num += 1
    
    return output



def solve(n):
    num = 1
    count = 0
    soln = []

    # returns success, val
    def tryMoveDigitLeft(x):
        new = x * 10
        if new > n:
            return False, x
        else:
            return True, new
    
    def tryInc1(x):
        new = x + 1

        # If 0, divide until remainder is not 0
        while new % 10 == 0:
            new //= 10
            assert(new != 0)
        
        if new > n:
            # Go to next and divide
            new += 10
            new //= 10
            while new % 10 == 0:
                new //= 10
                assert(new != 0)

        return new
    

    while count < n:
        soln += [num]
        count += 1

        # Now advance num
        isSuccess, newNum = tryMoveDigitLeft(num)
        if isSuccess:
            num = newNum
        else:
            num = tryInc1(num)
    
    return soln

        





"""

227. Basic Calculator II

s is expression
- eval
- int division, truncate towards 0

+, -, *, /

- first, parse to get num, op, num op, ...
- 1st pass to get multiplication and division out of the way
- 2nd pass to add or subtract intermediate sums

TODO: https://leetcode.com/problems/basic-calculator-iii/description/

Tactic:
Use stack, or remember last num added. On mult or division, pop from stack. Then return sum. Or, just 
add directly, and on mult / division, subtract lastNum. Tricky!!

"""

def solve(s):
    currNum = 0
    sign = '+'
    lastNum = 0
    total = 0

    for c in s+'+': # add extra character to force final num to be added
        if c.isnumeric():
            currNum = currNum * 10 + int(c)
        elif c in ('*', '/', '-', '+'):
            if sign == '*':
                total -= lastNum
                lastNum = (currNum * lastNum)
                total += lastNum
            elif sign == '/':
                total -= lastNum
                lastNum = (int(lastNum / currNum))
                total += lastNum
            elif sign == '-':
                lastNum = -currNum
                total += (-currNum)
            else:
                lastNum = currNum
                total += (currNum)

            sign = c
            currNum = 0

    return total

def solve(s):
    currNum = 0
    sign = '+'
    stack = []
    for c in s+'+': # add extra character to force final num to be added

        if c.isnumeric():
            currNum = currNum * 10 + int(c)
        elif c in ('*', '/', '-', '+'):
            if sign == '*':
                stack.append(currNum * stack.pop())
            elif sign == '/':
                stack.append(int(stack.pop() / currNum))
            elif sign == '-':
                stack.append(-currNum)
            else:
                stack.append(currNum)

            sign = c
            currNum = 0

    return sum(stack)

# Best: No stack
def solve(s):
    total = 0
    lastNum = -1

    currNum = -1
    operation = ''

    def addCurrNumToTotal():
        nonlocal currNum
        nonlocal lastNum
        nonlocal operation
        nonlocal total

        if currNum == -1: return # do nothing

        if operation == '*':
            total -= lastNum # get lastnum out of total
            lastNum = (currNum * lastNum)
            total += lastNum
        elif operation == '/':
            total -= lastNum # get lastnum out of total
            lastNum = (int(lastNum / currNum))
            total += lastNum
        elif operation == '-':
            lastNum = -currNum
            total += (-currNum)
        else:
            lastNum = currNum
            total += (currNum)
        
        currNum = -1

    for c in s:
        if c.isnumeric():
            if currNum == -1: currNum = 0
            currNum *= 10
            currNum += int(c)
            continue

        addCurrNumToTotal()

        if c == '*' or c == '/' or c == '+' or c == '-':
            operation = c

    addCurrNumToTotal()
        
    return total

print(solve("2*3+4"))

# Better stack, no need for first parse
def solve(s):
    stack = []

    currNum = -1
    operation = ''

    def addToStack():
        nonlocal currNum
        nonlocal operation
        nonlocal stack

        if operation == '*':
            stack.append(currNum * stack.pop())
        elif operation == '/':
            stack.append(int(stack.pop() / currNum))
        elif operation == '-':
            stack.append(-currNum)
        else:
            stack.append(currNum)
        
        currNum = -1

    for c in s:
        if c.isnumeric():
            if currNum == -1: currNum = 0
            currNum *= 10
            currNum += int(c)
        elif c == '*' or c == '/' or c == '+' or c == '-':
            if currNum != -1:
                addToStack()
            operation = c
        elif currNum != -1: # space or something
            # num finished
            addToStack()

    if currNum != -1:
        addToStack()
        
    return sum(stack)


# print(solve("2*3+4"))

def solve(s):

    # first parse
    equation = []
    idx = 0
    currNum = None
    while idx < len(s):
        if s[idx].isnumeric():
            if currNum is None: currNum = 0
            currNum *= 10
            currNum += int(s[idx])
        elif s[idx] in ['+', '-', '/', '*']:
            if currNum is not None: equation.append(currNum)
            equation.append(s[idx])
            currNum = None
        else:
            if currNum is not None: equation.append(currNum)
            currNum = None

        idx += 1
    # final number
    if currNum is not None: equation.append(currNum)
    
    # Now do first pass for * and /
    newEquation = []
    idx = 0
    while idx < len(equation):
        # push numbers onto equation, if special operator, grab next num and push
        if equation[idx] == '*':
            nextNum = equation[idx + 1] 
            lastNum = newEquation.pop()
            newEquation.append(nextNum * lastNum)
            idx += 1
        elif equation[idx] == '/':
            nextNum = equation[idx + 1] 
            lastNum = newEquation.pop()
            newEquation.append(int(lastNum / nextNum)) # towards 0
            idx += 1
        else:
            newEquation.append(equation[idx])
        
        idx += 1
    
    # final, take rolling sum of + and -   
    result = newEquation[0]
    idx = 1
    while idx < len(newEquation):
        if newEquation[idx] == '+':
            result += newEquation[idx + 1]
            idx += 1
        else:
            result -= newEquation[idx + 1]
            idx += 1
        
        idx += 1
    
    return result

            

# solve("123 + 34 / 2 * 12")
# print(int(-8 / 3))




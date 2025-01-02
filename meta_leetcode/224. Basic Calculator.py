"""

224. Basic Calculator

- evaluate expression and return result
- only + - spaces and brackets

Can parse rolling as you go
- keep operand
- stack of brackets
- skip whitespace

(1 + (2 - (3 - 4) + 5))

Stack of monomials?

"""

# Dicey
# def solve(s):
#     total = 0
#     op = '+'
#     currNum = 0

#     bracketStack = []

#     for c in s+'+':
#         if c.isnumeric():
#             currNum = currNum * 10 + int(c)
#         elif c in ('+', '-'):
#             # add last
#             if op == '+': total += currNum
#             else: total -= currNum

#             currNum = 0
#             op = c
#         elif c == '(':
#             bracketStack.append((total, op))
#             total = 0
#             currNum = 0
#             op = '+'
#         elif c == ')':
#             prevTotal, prevOp = bracketStack.pop()
#             if prevOp == '+':
#                 total = prevTotal + total
            



def solve(s):
    total = 0
    op = 1 # mult by before adding
    curr = 0
    bracketStack = []

    for c in s:
        if c == ' ':
            continue
        elif c == '(':
            bracketStack.append((total, op)) # store previous total and operand
            total = 0
            curr = 0
            op = 1
        elif c == ')':
            # cleanup last digit
            total += op * curr
            lastTotal, lastOp = bracketStack.pop()
            total = lastTotal + lastOp * total # add bracketed value

            curr = 0
            op = 1 # reset op

        elif c == '+':
            total += curr * op
            curr = 0
            op = 1

        elif c == '-':
            total += curr * op
            curr = 0
            op = -1

        else: # number
            x = int(c)
            curr = curr * 10 + x
    
    # At end, if curr not 0, add
    return total + op * curr

print(solve("1  -(3 - 4 - (5 + 2))"))

print(eval("1  -(3 - 4 - (5 + 2))"))

            




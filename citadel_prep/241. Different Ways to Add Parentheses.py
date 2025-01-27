"""

241. Different Ways to Add Parentheses

expression of numbers and operators
all possible results from compute with different orders

+ - or *

num op num op num op ...

on op, can apply on next term
- but lots of choices on what next term could be
- search algorithm? dfs


Some memoization / cache here...

"""

def solve(expr):
    output = []

    # First, just parse to make op and numbers
    i = 0
    num = 0
    newExpr = []
    while i < len(expr):
        while i < len(expr) and expr[i].isalnum():
            num = num * 10 + int(expr[i])
            i += 1
        
        newExpr.append(num)
        num = 0
        if i == len(expr): break
        newExpr.append(expr[i]) # op
        i += 1
    # print(newExpr)

    # Now do a dfs with memoization, cache the expr
    cache = {}
    def dfs(i, total, op, target): # the start of the next. target is what to apply op to in case of mult
        nonlocal cache
        nonlocal output
        nonlocal newExpr

        for k in range(i, len(newExpr), 2): # skip 2 at a time
            num = newExpr[k]

            if op == '+':
                target += num
            elif op == '-':
                target -= num
            else:
                target *= num
            
            if k+1 >= len(newExpr): # last term, so add
                print(total, target)
                output.append(total + target)
            else:
                op = newExpr[k+1] # next op on target

                # also do a dfs for other combos
                dfs(k + 2, total + target, op, 0)
    dfs(0, 0, '+', 0)
    return output

print(solve("2-1-1"))
# print(solve("2*3-4*5"))


        
            


        

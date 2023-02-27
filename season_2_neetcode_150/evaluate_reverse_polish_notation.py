# Results:
# Runtime: 63ms 90.22%
# Memory Usage: 14.3MB 93.89%

"""

https://leetcode.com/problems/evaluate-reverse-polish-notation/


reverse polish notation: 3 2 + = 3 + 2
- division truncates towards 0
- no div by 0
- + - * / 

For now, don't worry about pemdas. would it even be a problem?

Idea:
- recursive eval of expressions? parse from back, and see?
    - or reverse first
- function to eval expression, returns result and end of expression index?

Time: O(n), each expr parsed once
Space, idk. Callstack, 

Idea2: Use a stack, push things on and if encounter an operator, pop and eval

Tactic: Use a stack, and pop right / left from stack if hit operator

"""

def solve2(tokens):
    # use stack
    stack = []
    operators = "+-*/"

    for token in tokens:
        if token in operators:
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            if token == "*":
                stack.append(left * right)
            if token == "/":
                stack.append(int(left / right))
        else:
            stack.append(int(token))
    
    return stack[0]


# a = "12"
# b = "-12"
# print(a.isnumeric())
# print(b.strip("-").isdigit())



def solve(tokens):
    tokens.reverse()

    def evalExpr(tokens, i):

        # case 1, it's a number
        if (tokens[i].strip('-').isdigit()):
            return (int(tokens[i]), i + 1)

        op = tokens[i]
        left, nextI = evalExpr(tokens, i + 1)
        right, nextI = evalExpr(tokens, nextI)

        if (op == "+"):
            return left + right, nextI
        elif (op == "-"):
            return left - right, nextI
        elif (op == "*"):
            return left * right, nextI
        else:
            return int(left / right), nextI
    
    return evalExpr(tokens, 0)[0]
        
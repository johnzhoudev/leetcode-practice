"""

415. Add Strings

add strings that are numbers - both non-neg integers
Cannot convert to int or anything

Just do carries and stuff

Tactic:
Like sum 2 integer linked lists. If without + or -, use bit approach

"""

def solve(num1, num2):

    output = ""

    carry = 0
    num1 = num1[::-1]
    num2 = num2[::-1]
    idx = 0

    # must iterate backwards
    while idx < len(num1) or idx < len(num2):
        if idx < len(num1):
            d1 = num1[idx]
        else:
            d1 = "0"
        if idx < len(num2):
            d2 = num2[idx]
        else:
            d2 = 0
    
        tot = int(d1) + int(d2) + carry
        carry = tot // 10
        output += str(tot % 10)
        idx += 1
    
    if carry != 0:
        output += str(carry)
    
    return output[::-1]

print(solve("123", "123"))
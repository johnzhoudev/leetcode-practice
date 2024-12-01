"""

282. Expression Add Operators

string of digits
insert +, -, * between digits to get to target

return all possibilities

Feel like we need a search algorithm
number can contain multiple digits

What would a search alg look like?
inbetween each digit - can insert, or not
    - no leading 0 numbers though => can only concat

O(3^n) if there are n digits
- not to mention evaluating it, though you could do this like the other question

Dynamic programming?
- dp[i] = set of sums you can get combining 
- but multiplying throws everything off because you can't deduce what sum is based off the other stuff

Only 10 digits in num

Search algorithm maybe the best bet


adding a digit is equivalent to mult by 10 

Tactic:
What the fuck. Track total, lastNumberAdded, lastNumberMultiplied. On operand append, +, *, -, can figure out and dfs.
"""

def solve(num, target):
    # preappend first digit
    total = int(num[0]) # sums
    lastNumberAdded = int(num[0])
    lastNumberMultiplied = int(num[0]) # lastNumberAdded is a product and last num multiplied was this

    output = []

    # keep iterating on num[i:] (haven't added num[i] yet)
    def dfs(i, equation, total, lastNumberAdded, lastNumberMultiplied, isLeadingZero=False):

        if i == len(num):
            if total == target:
                output.append(equation)
            return 
        
        # Otherwise not at end, so make a choice

        # choose to just append digit

        # can only append to a non-zero number
        if not isLeadingZero:
            xy = lastNumberAdded // lastNumberMultiplied # divide out last number
            newLastNumberMultiplied = lastNumberMultiplied * 10 + (int(num[i]) if lastNumberMultiplied >= 0 else -int(num[i])) # add digit
            newLastNumberAdded = xy * newLastNumberMultiplied
            newTotal = total - lastNumberAdded + newLastNumberAdded
            dfs(i + 1, equation + num[i], newTotal, newLastNumberAdded, newLastNumberMultiplied, isLeadingZero)

        # Choose to * 
        newLastNumberMultiplied = int(num[i])
        newLastNumberAdded = lastNumberAdded * int(num[i])
        newTotal = total - lastNumberAdded + newLastNumberAdded
        dfs(i + 1, equation + '*' + num[i], newTotal, newLastNumberAdded, newLastNumberMultiplied, num[i] == '0')

        # choose to +
        newLastNumberAdded = int(num[i])
        newLastNumberMultiplied = newLastNumberAdded
        newTotal = total + newLastNumberAdded
        dfs(i+1, equation + '+' + num[i], newTotal, newLastNumberAdded, newLastNumberMultiplied, num[i] == '0')

        # choose to -
        newLastNumberAdded = -int(num[i])
        newLastNumberMultiplied = newLastNumberAdded
        newTotal = total + newLastNumberAdded
        dfs(i+1, equation + '-' + num[i], newTotal, newLastNumberAdded, newLastNumberMultiplied, num[i] == '0')


    dfs(1, num[0], total, lastNumberAdded, lastNumberMultiplied, num[0] == '0')

    # for expr in output:
    #     print(expr)

    return output

output = set(solve("123456789", 45))

def addOperators(num: 'str', target: 'int') -> 'List[str]':
    N = len(num)
    answers = []
    def recurse(index, prev_operand, current_operand, value, string):

        # Done processing all the digits in num
        if index == N:

            # If the final value == target expected AND
            # no operand is left unprocessed
            if value == target and current_operand == 0:
                answers.append("".join(string[1:]))
            return

        # Extending the current operand by one digit
        current_operand = current_operand*10 + int(num[index])
        str_op = str(current_operand)

        # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
        # valid operand. Hence this check
        if current_operand > 0:

            # NO OP recursion
            recurse(index + 1, prev_operand, current_operand, value, string)

        # ADDITION
        string.append('+'); string.append(str_op)
        recurse(index + 1, current_operand, 0, value + current_operand, string)
        string.pop();string.pop()

        # Can subtract or multiply only if there are some previous operands
        if string:

            # SUBTRACTION
            string.append('-'); string.append(str_op)
            recurse(index + 1, -current_operand, 0, value - current_operand, string)
            string.pop();string.pop()

            # MULTIPLICATION
            string.append('*'); string.append(str_op)
            recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
            string.pop();string.pop()
    recurse(0, 0, 0, 0, [])    

    return answers

out2 = set(addOperators("123456789", 45))

# for x in out2:
#     if x not in output:
#         print(x)

for x in output:
    if x not in out2:
        print(x)


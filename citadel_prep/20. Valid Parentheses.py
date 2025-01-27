"""

20. Valid Parentheses


"""

def solve(s):
    stack = []
    open = ('(', '{', '[')

    closedMap = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for c in s:
        if c in open:
            stack.append(c)
        else:
            if not stack or stack.pop() != closedMap[c]: return False
    return len(stack) == 0
"""

1249. Minimum Remove to Make Valid Parentheses

- other characters don't count

- if encounter ) with no opening, remove
- if encounter ( with no closing, remove. can only see at end

Idea:
- go thru with stack, figure out. 

Actually return string, damn
- keep stack and idx of open brackets
- keep set of closing brackets to remove

O(n) time
O(1) space

"""

def solve(s):
    state = []
    toRemove = set()

    for idx, c in enumerate(s):
        if c == ')':
            if not state:
                toRemove.add(idx)
            else:
                state.pop()
        elif c == '(':
            state.append(idx)
    
    for idx in state: toRemove.add(idx)

    result = ''.join([s[i] for i in range(len(s)) if i not in toRemove])
    return result
            
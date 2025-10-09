"""

22. Generate Parentheses

generate all combos of well formed parentheses

recursively - gen all combos of 1, 2, ... paren
then for n, it's ([n-1]), () before or () after - have to dedupe with set

Or backtracking, to generate either open or close one?

Better: Either open or close

Tactic: Backtrack, either open or close paren. Track num open and num total

"""

def solve(n):
    output = []

    def backtrack(state, num_open, num_total):

        if num_total == n and num_open == 0:
            output.append(state)
        elif num_total > n:
            return # done
        
        if num_open > 0: # try adding closed bracket
            backtrack(state + ')', num_open - 1, num_total)
        # Add open bracket
        backtrack(state + '(', num_open + 1, num_total + 1)
    
    backtrack("", 0, 0)
    return output

print(solve(4))
        
        



def solve(n):
    paren = {}
    paren[0] = set() # blank string
    paren[0].add("")
    for i in range(1, n + 1):
        state = set()

        for left in range(i): # paren to left
            for middle in range(i - left): # i - left = remaining paren you could have
                for left_p in paren[left]:
                    for middle_p in paren[middle]:
                        for right_p in paren[i - middle - left - 1]:
                            state.add(f"{left_p}({middle_p}){right_p}")
        paren[i] = state
    
    return list(paren[n])

# print(solve(4))




"""

39. Combination Sum

all unique combos where the numbers sum to target

Search alg?
O(output)

For each element, either use or don't
Can do iterative

Tactic: Backtrack to find all combos. Either use candidates[i] or not.

"""

def solve(candidates, target):
    output = []

    def dfs(i, total, state): # searches candidates[i:], including i

        if total == target:
            output.append(state.copy())
            return
        
        if i >= len(candidates) or total > target: # Prune
            return

        # Skip candidates[i]
        dfs(i+1, total, state)

        # Use candidates[i]
        state.append(candidates[i])
        total += candidates[i]
        dfs(i, total, state)
        total -= candidates[i]
        state.pop()
    
    dfs(0, 0, [])
    return output
        
print(solve([2,3,6,7], 7))
        




        
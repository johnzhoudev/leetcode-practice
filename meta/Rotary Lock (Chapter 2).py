"""

same as rotary lock 1
2 locks

can select with either

min time required  to select all ints

Ideas:

- brute force way, search alg, but that's O(2^m) which is big

states: lock keys, ith step
- dfs(left key, right key, step)
- m possible values for step
- at most m different keys that you encounter, 
- at a certain step, 2m different states

O(m^2) alg

Is the idea iteration?

start with states, and for each iteration, generate new states? at most m^2 different states

So it WAS stack overflow!

Tactic:
Can do memoization (leftnum, rightnum, step). Or, just keep dict of (left, right) = min steps and each iter, update all. Min M^2 cases per thing
O(m^3)?

"""

def solve(n, m, c):
    # keys are states, value is moves to get to state
    states = {}
    states[(1, 1)] = 0

    def calcDistance(a, b):
        if a > b: return calcDistance(b, a)
        # a <= b
        return min(b - a, n - (b - a))
    
    for target in c:
        newStates = {}
        for x, y in states:
            if (target, y) not in newStates:
                newStates[(target, y)] = calcDistance(x, target) + states[(x, y)]
            else:
                newStates[(target, y)] = min(newStates[target, y], calcDistance(x, target) + states[(x, y)])

            if (x, target) not in newStates:
                newStates[(x, target)] = calcDistance(target, y) + states[(x, y)]
            else:
                newStates[(x, target)] = min(newStates[x, target], calcDistance(target, y) + states[(x, y)])

        states = newStates
    
    best = float('inf')
    for state in states:
        best = min(states[state], best)
    return best


def solve(n, m, c):
    # memoization

    state = {} # min number of steps to get to end at left, right, step

    def calcDistance(a, b):
        if a > b: return calcDistance(b, a)
        # a <= b
        return min(b - a, n - (b - a))

    def dfs(left, right, step):
        if step >= len(c): return 0 # done already

        if (left, right, step) in state:
            return state[(left, right, step)]
        
        # calculate manually
        target = c[step]
        res = min(calcDistance(left, target) + dfs(target, right, step + 1), calcDistance(right, target) + dfs(left, target, step + 1))
        state[(left, right, step)] = res

        return res
    
    return dfs(1, 1, 0)


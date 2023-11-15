"""

https://leetcode.com/problems/baseball-game/

Baseball Game

empty record
- operations arr
- int x = new score of x
- + is sum of previous two scores
- D is double of previous score
- C is invalidate previous score

return sum of all scores

only track previous
invalidate means track all

"""

def solve(operations):
    scores = []
    for op in operations:
        if op == '+':
            scores += [scores[-1] + scores[-2]]
        elif op == 'D':
            scores += [scores[-1] * 2]
        elif op == 'C':
            scores.pop()
        else:
            scores += [int(op)]

    return sum(scores)


def solve1(operations):
    scores = []
    total = 0
    for op in operations:
        if op == '+':
            scores += [scores[-1] + scores[-2]]
        elif op == 'D':
            scores += [scores[-1] * 2]
        elif op == 'C':
            total -= scores.pop()
            continue
        else:
            scores += [int(op)]

        total += scores[-1]
    
    return total

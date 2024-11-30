"""

Scoreboard Inference (Chapter 2)

points 1, 2, 3

1 
2 or 1 1 
3 or 12 or 21 or 111
4 = 2 2 or 3 1 
5 = 3 2

Doesn't it generalize?

x = 3s + 2 or 1 or 0

Lets say we used this strategy, get max number of 3's and add a 2 if we need it or a 1 if we need it
- ie if ever a number % 3 is 1 or 2

then to make more efficient, well, we can't. since that would mean removing a 3, and then can't make last number. So can't remove any.

Case:
4 and 2
- 2, 2

6 and 4
- 3 3 1

Consider this:
8 = 3 + 1 + 3 + 1
3 + 3 = 6
3 + 1 = 4

More Notes:
- say largest number is all 3's, and you also have a 1 and 2. Can replace one 3 with the 1 and 2.
- Say largest number is all 3's + 1. And you have a 2. Can replace a 3 and 1 with a 2. ONLY if no 1, and no largest - 1 (still needs all 3's)
    - in fact, can do this for all numbers that are 1 mod 3, except 1

Tactic:
See above. Fancy number tricks.

"""

def solve(n, s):
    has1 = False
    need1 = False
    need2 = False
    largestMinus1 = False

    largest = max(s)

    for num in s:
        if num == 1: has1 = True
        if num % 3 == 1: need1 = True
        if num % 3 == 2: need2 = True
        if num == largest - 1: largestMinus1 = True
    

    if largest % 3 == 0 and need1 and need2: # 
        return largest // 3 + 2 - 1 # just use 1 and 2 instead of the last 3
    elif largest % 3 == 1 and need2 and not has1 and not largestMinus1:
        # shortcut, can get rid of a 3 and a 1 and add a second 2
        return largest // 3 + 1
    
    return largest // 3 + (1 if need1 else 0) + (1 if need2 else 0)

print(solve(1, [2, 4]))

# # incorrect
# def solve(n, s):
#     need1 = False
#     need2 = False
#     for num in s:
#         if num % 3 == 1: need1 = True
#         elif num % 3 == 2: need2 = True
#     largest = max(s)
#     return largest // 3 + (1 if need1 else 0) + (1 if need2 else 0)

# print(1 % 3)
# print(2 % 3)
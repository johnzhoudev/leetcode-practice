"""
WIP - this doesn't work...

https://leetcode.com/problems/multiply-strings/

num1 and num2 as strings
return product

Just do standard way
- have car
- O(n^2)

Or, divide and conquer
- divide into half and half
- top half 
- not true.
- whatever, just do brute force way

- Have accumulated sum, for each letter, mult by each other and add and mult by 10

"""

def solve(num1, num2):
    acc = 0
    num1 = reversed(num1)
    num2 = reversed(num2)

    for idx, d in enumerate(num2):
        d = int(d) * (10 ** idx)
        for idx2, d2 in enumerate(num1):
            d2 = int(d2) * (10 ** idx2)
            acc += d * d2
    
    return acc


print(solve("5", "51"))
        

"""

118. Pascal's Triangle

given integer, return first numrows of pascals triangle

1
11
121
1331
14641

Iteratively generate

Tactic:
Add previous pairs. Use Coroutine / generator! Nice and easy!


"""

def pascal():
    yield [1]
    yield [1, 1]
    last = [1, 1]

    while True:
        curr = [1]
        for i in range(len(last) - 1):
            curr.append(last[i] + last[i+1])
        curr.append(1)
        yield curr
        last = curr
            

def solve(numRows):
    output = []

    gen = pascal()

    for i in range(numRows):
        output.append(next(gen))
    return output



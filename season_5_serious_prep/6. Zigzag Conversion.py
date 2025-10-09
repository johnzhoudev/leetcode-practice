"""

6. Zigzag Conversion


Make rows and go up and down

"""

def solve(s, numRows):
    if numRows == 1:
        return s

    state = ["" for _ in range(numRows)]

    direction = 1 # 1 or -1
    idx = 0

    for c in s:
        state[idx] += c

        idx += direction

        if idx == numRows - 1 or idx == 0:
            direction *= -1 # change direction for next jump
    
    return ''.join(state)


def solve(x):
    # 32 bits
    y = 0
    for i in range(32):
        y <<= 1
        y |= (x & 1)
        x >>= 1
    return y
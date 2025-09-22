"""

2429. Minimize XOR

Idea: count bits each and add bits while 


2


100111
100100

"""

def solve(num1, num2):
    def getSetBits(num):
        setbits = 0
        while num != 0:
            setbits += num & 1
            num >>= 1
        return setbits

    sbn1 = getSetBits(num1)
    sbn2 = getSetBits(num2)

    out = num1
    bitmask = 1

    while sbn1 != sbn2:
        bit = num1 & 1

        if sbn1 > sbn2: # at this position, how many more set bits are in num1?
            # needs to be empty
            out &= (~bitmask)
            pass
        elif sbn1 < sbn2: # sbn1 < sbn2, so less bits in num1 than num2. Therefore must set this one
            out |= bitmask
            sbn2 -= 1
        else:
            break # if equal, can return early


        if bit == 1:
            sbn1 -= 1 # now past this set bit.

        # advance
        num1 >>= 1
        bitmask *= 2

    # set remaining bits if 
    
    return out

solve(1, 12)
        
        
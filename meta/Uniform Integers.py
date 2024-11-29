"""

Uniform Integers

- all digits same

closed form solution?

for every hundred, there's 9 uniform integers

75 
300
- leading digit indicates which one you're at

- determine which order of magnitude a number is
- take final digit and do checks
- 

Tactic:
- modulo and // arithmetic to get order of magnitude, etc. need numBelow and numOnOrBelow to make ranges.

"""

def solve(a, b):

    # order is 10^order
    def getUniformInt(digit, order):
        total = digit
        while order > 0:
            total *= 10
            total += digit
            order -= 1
        return total

    # returns order of magnitude, and calculates number of terms below it in order of magnitude (9 for each order)
    def getOrderOfMagnitude(a):
        originalNum = a
        order = -1
        largestDigit = a % 10 # ones digit

        while True:
            if a <= 0: break
            largestDigit = a
            order += 1
            a //= 10
        
        numBelow = largestDigit if getUniformInt(largestDigit, order) < originalNum else largestDigit - 1
        numOnOrBelow = largestDigit if getUniformInt(largestDigit, order) <= originalNum else largestDigit - 1
        
        return order, numBelow, numOnOrBelow

    orderA, numBelowA, _ = getOrderOfMagnitude(a)
    orderB, numBelowB, numOnOrBelowB = getOrderOfMagnitude(b)

    if orderA == orderB: return numOnOrBelowB - numBelowA
    else:
        total = 9 - numBelowA # a's order
        total += 9 * (orderB - orderA - 1) + numOnOrBelowB
        return total

print(solve(75, 300))
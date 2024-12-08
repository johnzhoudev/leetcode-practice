"""

65. Valid Number


Formally, a valid number is defined using one of the following definitions:

1. An integer number followed by an optional exponent. - could have leading 0's
    - An integer number is defined with an optional sign '-' or '+' followed by digits.

2. A decimal number followed by an optional exponent.
    - A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.

Digits followed by a dot '.' followed by digits.

A dot '.' followed by digits.

An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

- pass in terminate sign

Tactic:
DFA - State machine, with maps to each state. Or, use coroutine! Coroutine, only have 1 boolean.

"""

class Failure(Exception):
    def __init__(self):
        super()

class Valid(Exception):
    def __init__(self):
        super()

class Terminate:
    def __init__(self):
        pass
    
    def isdigit(self):
        return False

def isValidNumber():

    c = yield

    # first handle sign - case for both decimal and int numbers
    if c == '-' or c == '+':
        c = yield
    
    hasDigits = False

    # at this point, must be digits. So parse
    while c.isdigit():
        hasDigits = True
        c = yield
    
    # if no more digits, must be either decimal or e
    if c == '.':
        c = yield

        if not hasDigits and not c.isdigit():
            raise Failure # must be followed by a digit

        # continue parsing number
        while c.isdigit():
            hasDigits = True
            c = yield

    if c == 'e' or c == 'E':

        if not hasDigits:
            raise Failure

        # parse exponent
        c = yield

        # now parse integer number
        if c == '-' or c == '+':
            c = yield
        
        # must have a digit afterwards
        if not c.isdigit():
            raise Failure
        
        while c.isdigit():
            c = yield
    
    if not hasDigits:
        raise Failure

    # now c must be terminated
    if not isinstance(c, Terminate):
        raise Failure

    raise Valid

def solve(s):
    try:
        validator = isValidNumber()
        next(validator) # prime

        for c in s:
            validator.send(c)
        
        validator.send(Terminate())
        return False # no valid exn yet
    except Failure:
        return False
    except Valid:
        return True




print(solve("+"))
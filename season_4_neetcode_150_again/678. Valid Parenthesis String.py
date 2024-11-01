"""

678. Valid Parenthesis String

()*
- ( must have corresp )
- * can be ( or ) or empty string

is valid?

Valid parentheses, which can solve using a stack
- 

(*))
*)

* could be ( or ) 

- * treated as nothing, but we count them
- we do valid parentheses as usual
- if we try to pop with ) and no (, can use star
- at end, if any 

- what if we, on a *, just tried to pop the ( chars
    - but we count them
    - and if we encounter a ) that can't pop, we use one of teh popped chars
- if no ( to pop, we add * as a ( and inc left bracket star counter, can be dec at end

think that works
O(n)
O(1) space

Better: just take max and min open bracket count. 
    - either too many ) -> max open bracket should reduce to >= 0. if neg at any point, fail
    - or ( with no ) - take min open bracket count
    - Tricky, always inc cMax but cMin, can't go below 0

Tactic:
Keep counts of open brackets, closed*, empty* and open*. For each ()* handle counts accordingly. Try with *=>), then empty, then (
Or, keep max and min bracket count checking 2 cases: if too many )))), cMax < 0 => fail. If too many ((( at end, cmin must == 0.

"""

def solve(s):
    cMax = 0
    cMin = 0

    for c in s:
        if c == '(':
            cMax += 1
            cMin += 1
        elif c == ')':
            if cMax == 0: return False
            cMax -= 1
            if cMin > 0: cMin -= 1
        else: # *
            cMax += 1
            if cMin > 0: cMin -= 1

    
    return cMax >= 0 and cMin == 0

def solve(s):
    numOpenBrackets = 0
    numClosedStars = 0
    numEmptyStars = 0
    numOpenStars = 0

    for c in s:
        if c == '(':
            numOpenBrackets += 1
        elif c == ')':

            if numOpenBrackets > 0:
                numOpenBrackets -= 1
            elif numClosedStars > 0:
                numClosedStars -= 1
                numEmptyStars += 1
            elif numEmptyStars > 0:
                numEmptyStars -= 1
                numOpenStars += 1
                # captured by open star
            else:
                return False # invlaid
        else: # star

            if numOpenBrackets > 0:
                numOpenBrackets -= 1
                numClosedStars += 1
            else:
                numEmptyStars += 1
    
    return numOpenBrackets == 0






"""

408. Valid Word Abbreviation

abbreviate - replace non adj non empty substr with length, no leading 0

given word and abbreviation, matches?


greedy, just walk thru

Tactic:
Kind of tricky. Use num parsing trick, and advance if new char. Make sure to check at end! return wordIdx == len(word)

"""

def solve(word, abbr):

    wordIdx = 0

    num = 0
    for c in abbr:
        if c.isnumeric():
            if num == 0 and int(c) == 0: return False   # in case invalid
            num = num * 10 + int(c)
        else:
            # if num just parsed, advance
            if num != 0:
                wordIdx += num
                num = 0
            
            if wordIdx >= len(word): return False
            
            # check char
            if c != word[wordIdx]: return False
            wordIdx += 1
    
    if num != 0:
        wordIdx += num
        num = 0
    
    return wordIdx == len(word)




"""

131. Palindrome Partitioning

all possible partitions of palindromes

Start with individual letters - all palindromes
- then, either join same letters one after the other, OR join 2 different
    - to avoid dupes, only join 1 letter at a time
- so it's either join same letter once, or join 2 that are diff.
- either 1 letter join right, or from middle with 1 letter

aa b a b aa

- search alg for each case
    - dfs, for each elt in the string, see if you can join

Alternative idea:
- process substrings from the front. loop thru, if (0, i) is substring, keep and process rest.

Is this really the fastest runtime? Potentially optimize with cache?

Tactic: Easiest way: Check if beginning is palindrome, and dfs on remaining. Use cache too to check if palindrome. Or, more complicated way, start all single letters
and join. Must join to right, only with single letters, etc. too many details.
"""

def solve(s):
    output = []

    cache = set()

    def isPalindrome(s):
        nonlocal cache
        if s in cache: return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        
        cache.add(s)
        return True

    def dfs(curr, remaining):
        nonlocal output

        if not remaining:
            output.append(curr.copy())

        for i in range(1, len(remaining) + 1):
            if isPalindrome(remaining[:i]):
                curr.append(remaining[:i])
                dfs(curr, remaining[i:])
                curr.pop()
    
    dfs([], s)
    return output

def solve(s):
    output = []
    palindromes = [c for c in s]

    def isSameLetter(s):
        letter = s[0]
        for c in s:
            if c != letter: return False
        return True

    def dfs(palindromes, k):
        output.append(palindromes.copy())

        for i in range(k, len(palindromes)):

            # try join on right if same letter
            if i+1 < len(palindromes) and len(palindromes[i+1]) == 1 and isSameLetter(palindromes[i]) and palindromes[i][0] == palindromes[i+1][0]:
                newPalindromes = palindromes[:i] + [palindromes[i] + palindromes[i+1]] + (palindromes[i+2:] if i+2 < len(palindromes) else [])
                dfs(newPalindromes, i)
            
            # or try and join two if different letters
            if i-1 >= 0 and i+1 < len(palindromes) and len(palindromes[i-1]) == 1 and len(palindromes[i+1]) == 1 and palindromes[i-1] == palindromes[i+1] and (palindromes[i][0] != palindromes[i-1] or not isSameLetter(palindromes[i])):
                newPalindromes = palindromes[:i-1] + [palindromes[i-1] + palindromes[i] + palindromes[i+1]] + (palindromes[i+2:] if i+2 < len(palindromes) else [])
                dfs(newPalindromes, i-1)
        

    dfs(palindromes, 0)
    return output


print(solve("aaa"))


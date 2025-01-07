"""

1408. String Matching in an Array

words
return all strinsg in words that is a substring of another word


Idea:
- brute force, for each word, check if it's in another word

There must be a faster way...

Better: Store trie of all substrings for all words, and check?

TODO:
- Suffix tree impl
- KMP Impl

"""

def solve(words):

    def isSubstring(w1, w2): # is w1 a substring of w2
        return w1 in w2
        for start in range(len(w2) - len(w1) + 1):
            i = start
            j = 0
            while j < len(w1):
                if w2[i] != w1[j]:
                    break
                i += 1
                j += 1

            if j == len(w1): return True
        return False
    
    words.sort(key = len)
    # print(words)

    output = []

    # Go thru and compare smaller to larger
    for idx, word in enumerate(words):
        for comp in words[idx+1:]:
            if isSubstring(word, comp):
                output.append(word)
                break

    return output


    print(isSubstring("leetcode", "leetcode"))

print(solve(["asdf", "s", "ji23ofj32"]))
            

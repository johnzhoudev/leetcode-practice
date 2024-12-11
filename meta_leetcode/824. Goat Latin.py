"""824. Goat Latin

sentence
-sep by spaces

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".

If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Tactic:
straightforward, python fancy string stuff

"""

def solve(sentence):
    words = sentence.split(" ")
    output = []

    for idx, word in enumerate(words):
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            output.append(word + "ma" + ((idx+1) * 'a'))
        else:
            output.append(word[1:] + word[0] + "ma" + ((idx+1) * 'a'))
    
    return ' '.join(output)

print(solve("apple pear"))
    
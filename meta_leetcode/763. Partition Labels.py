"""

763. Partition Labels


Each letter appears in at most 1 part
- must merge

- keep hash table of letter and previously seen?

Is this a union find?

"ababcbacadefegdehijhklij"

a b a b

Seen - characters in other sections

Greedy
- hash map of letter to last occurrence
- when you add a letter, must be last

O(n) to build last, then O(n) to make list
O(26 space)

Tactic: Greedy, last idx

"""

def solve(s):
    last = {}
    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        if c not in last:
            last[c] = i
    
    # Now greedily add
    output = []
    curr = 0
    size = 0
    end = 0 # inclusive

    while curr < len(s):
        size += 1 # add a number
        end = max(end, last[s[curr]])
        if curr == end: # you're done!
            output.append(size)
            size = 0

        curr += 1
    
    return output

        



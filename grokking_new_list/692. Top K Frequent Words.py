"""

https://leetcode.com/problems/top-k-frequent-words/description/

Idea:
- count strings - O(n)
- maintain min heap with k things - O(n log k)

Tip: overwrite __lt__() for custom comparator in heap

"""

class Node:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __repr__(self):
        return f"{self.count},{self.word}"
    
    def __lt__(self, other):
        if self.count == other.count: return self.word > other.word
        return self.count < other.count


import heapq # min heap
from collections import defaultdict
def solve(words, k):
    wordCount = defaultdict(lambda : 0)

    for word in words:
        wordCount[word] += 1
    
    heap = []
    for word, count in wordCount.items():
        heapq.heappush(heap, Node(count, word))
        if len(heap) > k:
            print(heap)
            heapq.heappop(heap)
    
    output = []
    while heap:
        tempOut = []
        level = heap[0].count
        # For each level, pop into array
        print(heap)
        while heap and heap[0].count == level:
            tempOut.append(heapq.heappop(heap).word)
        print(tempOut)
        output.append(tempOut)
    
    output.reverse()
    finalOutput = []
    for words in output:
        words.reverse()
        for word in words:
            finalOutput.append(word)

    return finalOutput

        
print(Node(2, "i") < Node(2, "love"))
test = []
heapq.heappush(test, Node(2, "i"))
heapq.heappush(test, Node(2, "love"))
print(heapq.heappop(test))
print(heapq.heappop(test))
# test = []
# heapq.heappush(test, (1, "abcd"))
# heapq.heappush(test, (1, "asdf"))

# print(heapq.heappop(test))
# print(heapq.heappop(test))



# print(solve(["test", "test", "asdf", "asdfjk"], 3))
print(solve(["i","love","leetcode","i","love","coding"], 2))
print("love" < "i")
    

# 1st solution
# Results:
# Runtime: 606ms 53.27%
# Memory Usage: 58.1MB 5.2%

"""

https://leetcode.com/problems/longest-consecutive-sequence

Must be O(n)

- can create a graph, add characters to links if consecutive?
- Then just count the components and see which one is longest?
- given a number n, either add to chain from in front or behind.

- Create a dictionary hashing characters to graph components, with just a size.
    - given n, if already in dictionary, don't do anything. 

- Merging sets? or use doubly linked lists since can just append. but would you have to overwrite all entries?

- Or, just do a graph. Adjacency hash table, 
    - hash table takes character and gives what it maps to. only maps if the number exists
    - can just do a dfs afterwards to determine size. O(n)
    - for each number, add to hash table and check neighbours. if exists, add adjacency links

O(n) time to add each thing and connections since each number has at most 2 links, and O(n) space too because of that.

Idea 2:
- Build a hash set
- check if num - 1 is in set. if not, start of a sequence. so check sequentially. 
- take max

Tactic: Either build adjacency list and dfs, or make set of nums and check if left not in. then check all right
"""

def solve2(nums):
    numSet = set(nums)
    
    largest = 0
    for num in nums:
        if num - 1 in numSet:
            continue # not end
        else:
            curr = num
            size = 0
            while curr in numSet:
                size += 1
                curr += 1
            if size > largest:
                largest = size
    
    return largest


def solve(nums):
    # add characters to graph adjacency list
    adjList = {} # number to set of adjacent numbers

    for num in nums:

        if num not in adjList:
            # Add an entry, and link left and right if exists

            left = num - 1
            right = num + 1

            adjList[num] = set()

            # add links
            if left in adjList:
                adjList[left].add(num)
                adjList[num].add(left)
            if right in adjList:
                adjList[right].add(num)
                adjList[num].add(right)
    
    # all entries added, now do dfs and find longest part
    visited = set()

    def dfs(start):
        nonlocal visited
        nonlocal adjList

        if (start in visited):
            return 0

        size = 0 # start
        stack = [start]

        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            size += 1

            stack.extend(list(adjList[curr]))

        return size

    largest = 0
    for num in nums:
        newSize = dfs(num)
        if newSize > largest:
            largest = newSize
    
    return largest

            

            


            


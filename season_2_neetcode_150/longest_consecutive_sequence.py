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

"""
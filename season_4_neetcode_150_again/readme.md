# Neetcode 150 Tips

Leetcode Progression Ideas:

- Neetcode 150, finish by end of august - 3-4 q a day
    - Notes on common tactics for each part and example questions
- Grokking finish list randomly - 3q a day?
- Neetcode All, do randomly - 3 q a day?

# Tactics

## Intervals
- Finding number of days / rooms needed for intervals, sort by end and greedy, append to largest possible endtime - Meeting Schedule II
- Inserting interval, collect left and right and overlap min max - 57. Insert Interval
- Merging Intervals - sort and add, if overlapping then min max merge with last. - 56. Merge Intervals 
- Removing until non overlapping - Greedily take with earliest end - 435. Non-overlapping intervals
- HARD: Intervals and queries - 1851 Minimum interval to include each query

## Backtracking
- General backtracing with subsets - 39. Combination sum, 78 Subsets, 46 permutations
- Subsets backtracing with duplicates, use idx and count - or either add, or advance to next non dupe. - 90 subsets ii, 40. combination sum 2
- Grid backtracking - 79. word search
- Palindrome partitioning - try to see if prefix is palindrome, and recurse on remaining.
- N Queens grid backtracking, advance row and use y intercept to track diagonals

## Basic Graphs
- DFS - number of islands 200 / max area of island 695
- DFS Clone Graph - 133 Clone Graph
- BFS from multiple points - Walls and Gates